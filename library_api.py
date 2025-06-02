from flask import Flask, request, jsonify

app = Flask(__name__)

# Pre-filled list of books (just like in Cisco lab)
books = [
    {"id": 0, "title": "IP Routing Fundamentals", "author": "Mark A. Sportack"},
    {"id": 1, "title": "Python for Dummies", "author": "Stef Maruch Aahz Maruch"},
    {"id": 2, "title": "Linux for Networkers", "author": "Cisco Systems Inc."},
    {"id": 3, "title": "NetAcad: 20 Years Of Online-Learning", "author": "Cisco Systems Inc."}
]

# GET /books
@app.route('/api/v1/books', methods=['GET'])
def get_books():
    return jsonify(books), 200

# GET /books/{id}
@app.route('/api/v1/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if book:
        return jsonify(book), 200
    else:
        return jsonify({'error': 'Book not found'}), 404

# POST /books
@app.route('/api/v1/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(new_book), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
