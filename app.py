from flask import Flask, request, jsonify
import redis
import os

app = Flask(__name__)

# 獲取 Upstash Redis 的 URL 和密鑰
redis_url = os.getenv('UPSTASH_REDIS_URL')
redis_client = redis.from_url(redis_url)

@app.route('/')
def home():
    return "Welcome to the Book Borrowing System"

# @app.route('/books', methods=['GET'])
# def get_books():
#     books = redis_client.lrange('books', 0, -1)
#     books = [book.decode('utf-8') for book in books]
#     return jsonify(books)

# @app.route('/books', methods=['POST'])
# def add_book():
#     new_book = request.json.get('title')
#     redis_client.rpush('books', new_book)
#     return jsonify({'message': 'Book added successfully'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)