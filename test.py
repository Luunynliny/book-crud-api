from pprint import pprint

import requests

BASE_URL = "http://book-api:5000"


def print_section(name):
    print("=" * 40)
    print(name)
    print("=" * 40)


def print_separator():
    print("-" * 40)


def test_get_all_books():
    print("Testing GET /books (Get all books)")
    response = requests.get(f"{BASE_URL}/books")

    print("Response:", response.status_code)
    print("Content:")
    pprint(response.json())

    print_separator()


def test_get_book_by_id(book_id):
    print(f"Testing GET /books/{book_id} (Get book by ID)")
    response = requests.get(f"{BASE_URL}/books/{book_id}")

    if response.status_code == 200:
        print("Response:", response.status_code)
        print("Content:")
        pprint(response.json())
    else:
        print("Response:", response.status_code)
        print("Content:")
        pprint(response.json())

    print_separator()


def test_add_book(book_data):
    print("Testing POST /books (Add a new book)")
    response = requests.post(f"{BASE_URL}/books", json=book_data)

    print("Response:", response.status_code)
    print("Content:")
    pprint(response.json())

    print_separator()


def test_update_book_field(book_id, update_data):
    print(f"Testing PATCH /books/{book_id} (Update book field by ID)")

    response = requests.patch(f"{BASE_URL}/books/{book_id}", json=update_data)

    if response.status_code == 200:
        print("Response:", response.status_code)
        print("Content:")
        pprint(response.json())
    else:
        print("Response:", response.status_code)
        print("Content:")
        pprint(response.json())

    print_separator()


def test_delete_book(book_id):
    print(f"Testing DELETE /books/{book_id} (Delete book by ID)")
    response = requests.delete(f"{BASE_URL}/books/{book_id}")

    if response.status_code == 200:
        print("Response:", response.status_code)
        print("Content:")
        pprint(response.json())
    else:
        print("Response:", response.status_code)
        print("Content:")
        pprint(response.json())

    print_separator()


if __name__ == "__main__":
    print_section("WORKING")

    test_get_all_books()
    test_get_book_by_id(1)
    test_add_book(
        {
            "title": "Le Probleme à Trois Corps",
            "author": "Liu Cixin",
            "genre": "Sci-Fi",
        }
    )
    test_update_book_field(3, {"title": "Vanilla Sky"})
    test_delete_book(2)

    print("NOT WORKING")

    test_get_book_by_id(999)
    test_update_book_field(999, {"title": "This is it"})
    test_update_book_field(3, {"year": "2000"})
    test_delete_book(999)

    response = requests.post(f"{BASE_URL}/reset_books")
    print("Response:", response.status_code)
    print("Content:")
    pprint(response.json())

    test_get_all_books()
