from flask import Flask, jsonify, request

app = Flask(__name__)

# List of books
books = [
    {"id": 1, "title": "The King", "author": "J.D. Singh"},
    {"id": 2, "title": "Thinking", "author": "H Lee"},
    {"id": 3, "title": "1984", "author": "George G"},
    {"id": 4, "title": "2024", "author": "George G"},
]

# GET all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)


if __name__ == '__main__':
    app.run(debug=True) 