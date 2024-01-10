# flake8: noqa: F811
import pytest
import requests


@pytest.fixture
def base_url():
    return "http://book-api:5000"


@pytest.fixture(autouse=True)
def reset_books(base_url):
    yield
    requests.post(f"{base_url}/reset_books")


def test_get_all_books(base_url):
    res = requests.get(f"{base_url}/books")

    assert res.status_code == 200
    assert res.json() == [
        {
            "id": 1,
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "genre": "Classic",
        },
        {
            "id": 2,
            "title": "Germinal",
            "author": "Victor Hugo",
            "genre": "Historic",
        },
        {
            "id": 3,
            "title": "1984",
            "author": "George Orwell",
            "genre": "Dystopian",
        },
    ]


def test_get_all_books(base_url):
    res = requests.get(f"{base_url}/books")

    assert res.status_code == 200
    assert res.json() == [
        {
            "id": 1,
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "genre": "Classic",
        },
        {
            "id": 2,
            "title": "Germinal",
            "author": "Victor Hugo",
            "genre": "Historic",
        },
        {
            "id": 3,
            "title": "1984",
            "author": "George Orwell",
            "genre": "Dystopian",
        },
    ]


def test_get_book_by_id(base_url):
    res = requests.get(f"{base_url}/books/{1}")

    assert res.status_code == 200
    assert res.json() == {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "genre": "Classic",
    }

    res = requests.get(f"{base_url}/books/{999}")

    assert res.status_code == 404
    assert res.json() == {"message": "Book not found"}


def test_add_new_book(base_url):
    res = requests.post(
        f"{base_url}/books",
        json={
            "title": "Le Probleme à Trois Corps",
            "author": "Liu Cixin",
            "genre": "Sci-Fi",
        },
    )

    assert res.status_code == 201
    assert res.json() == {
        "id": 4,
        "title": "Le Probleme à Trois Corps",
        "author": "Liu Cixin",
        "genre": "Sci-Fi",
    }


def test_update_book(base_url):
    print(requests.get(f"{base_url}/books").json())

    res = requests.patch(
        f"{base_url}/books/{3}",
        json={
            "title": "La Forêt Sombre",
            "author": "Liu Cixin",
            "genre": "Sci-Fi",
        },
    )

    assert res.status_code == 200
    assert res.json() == {
        "id": 3,
        "title": "La Forêt Sombre",
        "author": "Liu Cixin",
        "genre": "Sci-Fi",
    }

    res = requests.patch(
        f"{base_url}/books/{999}",
        json={"title": "La Mort Immortelle"},
    )

    assert res.status_code == 404
    assert res.json() == {"message": "Book not found"}


def test_delete_book(base_url):
    res = requests.delete(f"{base_url}/books/{1}")

    assert res.status_code == 200
    assert res.json() == {"message": "Book deleted"}

    res = requests.delete(f"{base_url}/books/{1}")

    assert res.status_code == 404
    assert res.json() == {"message": "Book not found"}


def test_reset_books(base_url):
    requests.post(
        f"{base_url}/books",
        json={
            "title": "La Mort Immortelle",
            "author": "Liu Cixin",
            "genre": "Sci-Fi",
        },
    )

    res = requests.post(f"{base_url}/reset_books")

    assert res.status_code == 200
    assert res.json() == {"message": "Books reset to initial state"}

    res = requests.get(f"{base_url}/books")

    assert res.status_code == 200
    assert res.json() == [
        {
            "id": 1,
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "genre": "Classic",
        },
        {
            "id": 2,
            "title": "Germinal",
            "author": "Victor Hugo",
            "genre": "Historic",
        },
        {
            "id": 3,
            "title": "1984",
            "author": "George Orwell",
            "genre": "Dystopian",
        },
    ]
