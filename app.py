"""Minimal Flask application setup for the SQLAlchemy assignment."""
from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

# These extension instances are shared across the app and models
# so that SQLAlchemy can bind to the application context when the
# factory runs.
db = SQLAlchemy()
migrate = Migrate()


def create_app(test_config=None):
    """Application factory used by Flask and the tests.

    The optional ``test_config`` dictionary can override settings such as
    the database URL to keep student tests isolated.
    """

    app = Flask(__name__)
    app.config.from_object(Config)
    if test_config:
        app.config.update(test_config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Import models here so SQLAlchemy is aware of them before migrations
    # or ``create_all`` run. Students will flesh these out in ``models.py``.
    import models  # noqa: F401
    User = models.User
    Post = models.Post
    @app.route("/")
    def index():
        """Simple sanity check route."""

        return jsonify({"message": "Welcome to the Flask + SQLAlchemy assignment"})

    @app.route("/users", methods=["GET", "POST"])
    def users():
        """List or create users.

        TODO: Students should query ``User`` objects, serialize them to JSON,
        and handle incoming POST data to create new users.
        """
        from models import User
        if request.method == "GET":
            users_list = User.query.all()
            users_list = [{'id': user.id, 'username': user.username} for user in users_list]
            return jsonify(users_list)
    
        if request.method == "POST":
            data = request.get_json()
            if not data or 'username' not in data:
                return jsonify({"error": "Username is required"}), 400
            if user_exists := User.query.filter_by(username=data['username']).first():
                return jsonify({"error": "Username already exists"}), 409
            new_user = User(username=data.get('username'))
            try:
                db.session.add(new_user)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                return jsonify({"error": "Database error occured"}), 500
            return jsonify({'id': new_user.id, 'username': new_user.username}), 201


    @app.route("/posts", methods=["GET", "POST"])
    def posts():
        """List or create posts.

        TODO: Students should query ``Post`` objects, include user data, and
        allow creating posts tied to a valid ``user_id``.
        """
        if request.method == "GET":
            posts = Post.query.all()
            posts = []
            for post in posts:
                posts.append({
                    'id': post.id,
                    'title': post.title,
                    'content': post.content,
                    'user_id': post.user_id,
                    'author' : {
                        'id': post.author.id,
                        'username': post.author.username
                    }
                })
                return jsonify(posts), 200
            
            if request.method == "POST":
                data = request.get_json()
                if not data or 'title' not in data or 'content' not in data or 'user_id' not in data:
                    return jsonify({"error": "Title, content, and user id are required"}), 400
            user = User.query.get(data['user_id'])
            if not user:
                return jsonify({"error": "User not found"}), 404
            new_post = Post(title=data['title'], content=data['content'], user_id=user.id)
            try:
                db.session(new_post)
                db.session.commit()
            except Exception as e:
                return jsonify({"error": "Failed to create user"}), 500
            return jsonify({
                'id' : new_post.id,
                'title' : new_post.title,
                'content' : new_post.content,
                'user_id' : new_post.user_id
            }), 201

    return app


# Expose a module-level application for convenience with certain tools
app = create_app()


if __name__ == "__main__":
    # Running ``python app.py`` starts the development server.
    app.run(debug=True)
