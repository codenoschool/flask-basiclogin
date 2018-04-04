from flask import Flask, g, session, abort
from functools import wraps

app = Flask(__name__)
app.secret_key = ";p"
app.session_cookie_secure = True

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if g.user:
            return f(*args, **kwargs)
        else:
            return abort(403)

    return decorated

@app.before_request
def before_request():
    if "username" in session:
        g.user = session["username"]
    else:
        g.user = None

@app.route("/")
def index():

    return "Hello World!"

@app.route("/login")
def test_user():
    session["username"] = "CNS"

    return "Now you're logged in."

@app.route("/logout")
def logout():
    session.pop("username", None)

    return "You're logged out."

@app.route("/home")
@login_required
def home():

    return "Hi, you're a in locked page."

@app.route("/profile")
@login_required
def profile():

    return "Hi, you're logged as %s" % g.user

if __name__ == "__main__":
    app.run(debug=True)
