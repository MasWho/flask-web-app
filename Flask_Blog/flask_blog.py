from flask import Flask, render_template, url_for

app = Flask(__name__)

# Define some psuedo data
# flask.render_template can pass data to posts argument
# The html template rendering engine will then have access to posts and its data
# Can then run a for loop in the html template to display all of the data, that's how we will display blog posts
posts = [
    {
        'author': 'Mason',
        'title': 'blog 1',
        'content': 'first post content',
        'date_posted': 'April 21, 2018'
    },
    {
        'author': 'John',
        'title': 'blog 2',
        'content': 'second post content',
        'date_posted': 'May 21, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)