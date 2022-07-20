from flask import Flask, render_template

app = Flask(__name__)

@app.route('/test')
def test():
    return "Home Page"

@app.route('/test/about/')
def about_test():
    return "About Page"

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about', strict_slashes=False)
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)
