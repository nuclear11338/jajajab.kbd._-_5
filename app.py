from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy movie list
movies = [
    {"title": "Movie 1", "url": "https://example.com/movie1.mp4", "poster": "https://via.placeholder.com/150"},
    {"title": "Movie 2", "url": "https://example.com/movie2.mp4", "poster": "https://via.placeholder.com/150"},
    {"title": "Movie 3", "url": "https://example.com/movie3.mp4", "poster": "https://via.placeholder.com/150"},
]

@app.route('/')
def home():
    user_id = request.args.get('user_id')
    return render_template('movies.html', movies=movies, user_id=user_id)

if __name__ == '__main__':
    app.run(debug=True)
