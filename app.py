from flask import Flask, render_template
import redis

# connect to redis
r = redis.Redis(
  host='helpful-mako-37953.upstash.io',
  port=6379,
  password='AZRBAAIncDEzNDZlNjU0YTViNDE0YmE4YmQ4YWJkZjE1MjU3ZmU2NnAxMzc5NTM',
  ssl=True
)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('html/index.html')

if __name__ == '__main__':
    app.run(debug=True)