from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ddc49a5dbbc9ede1b9a12cdf2a1fb159'  # Needed for flask apps

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


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Flash message
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Flash message
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'Successfully logged in for {form.email.data}!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Incorrect login details for {form.email.data}!', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)