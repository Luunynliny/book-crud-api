import json
from os import path

from flask import jsonify, request

from app import app

FILE_PATH = path.join(path.dirname(path.abspath(__file__)), "../books.json")


def load_books():
    try:
        with open(FILE_PATH, "r") as file:
            books = json.load(file)
    except FileNotFoundError:
        books = []
    return books


def save_books(books):
    with open(FILE_PATH, "w") as file:
        json.dump(books, file, indent=4)


# API to get all books
@app.route("/books", methods=["GET"])
def get_books():
    books = load_books()
    return jsonify(books)


# Get a specific book
@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    books = load_books()

    book = next((book for book in books if book.get("id") == book_id), None)

    if book:
        return jsonify(book)

    return jsonify({"message": "Book not found"}), 404


# Add a new book
@app.route("/books", methods=["POST"])
def add_book():
    data = request.json
    books = load_books()
    new_book = {
        "title": data["title"],
        "author": data["author"],
        "genre": data["genre"],
    }
    books.append(new_book)
    save_books(books)
    return jsonify(new_book), 201


# Update a book
@app.route("/books/<int:book_id>", methods=["PATCH"])
def update_book_field(book_id):
    data = request.json
    books = load_books()
    for book in books:
        if book.get("id") == book_id:
            for key, value in data.items():
                if key in book:
                    book[key] = value
            save_books(books)
            return jsonify(book)
    return jsonify({"message": "Book not found"}), 404


# Delete a book
@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    books = load_books()
    for index, book in enumerate(books):
        if book.get("id") == book_id:
            del books[index]
            save_books(books)
            return jsonify({"message": "Book deleted"})
    return jsonify({"message": "Book not found"}), 404
