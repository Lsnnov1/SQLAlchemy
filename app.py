from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
# import sql alchemy
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
with app.app_context():
# configure database url
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///firstdb'

# initialize sqlalchemy
    db = SQLAlchemy(app)

    # connect app to instance
    db.app = app
    # db.init_app(app)

    app.config['SECRET_KEY'] = "me123"
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
    debug = DebugToolbarExtension(app)


@app.route("/")
def home_page():
    """shows home page"""
    return render_template("home.html")


# from flask import Flask, request, render_template
# from flask_debugtoolbar import DebugToolbarExtension
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)

# # Configure database URL
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///firstdb'

# # Initialize SQLAlchemy with the app
# db = SQLAlchemy(app)
# db.app = app
# # db.init_app(app)

# # Set other configurations
# app.config['SECRET_KEY'] = "me123"
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# debug = DebugToolbarExtension(app)

# @app.route("/")
# def home_page():
#     """Shows home page"""
#     return render_template("home.html")

# if __name__ == "__main__":
#     app.run(debug=True)
