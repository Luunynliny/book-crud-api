from flask import jsonify, request

from app import app

# Dummy data for books
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1", "genre": "Fiction"},
    {"id": 2, "title": "Book 2", "author": "Author 2", "genre": "Non-fiction"},
]


@app.route("/books", methods=["GET"])
def get_books():
    return jsonify(books)


# Get a specific book
@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({"message": "Book not found"}), 404


# Add a new book
@app.route("/books", methods=["POST"])
def add_book():
    new_book = {
        "id": len(books) + 1,
        "title": request.json["title"],
        "author": request.json["author"],
        "genre": request.json["genre"],
    }
    books.append(new_book)
    return jsonify(new_book), 201


# Update a book
@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        book["title"] = request.json["title"]
        book["author"] = request.json["author"]
        book["genre"] = request.json["genre"]
        return jsonify(book)
    return jsonify({"message": "Book not found"}), 404


# Delete a book
@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        books.remove(book)
        return jsonify({"message": "Book deleted"})
    return jsonify({"message": "Book not found"}), 404
