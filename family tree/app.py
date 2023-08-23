# importing modules from flask library
from flask import Flask, render_template

# creating an instance of the class Flask, by providing __name__ keyword as an argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():
    name = ""  # write your name
    age = ""   # write your age

    return render_template('index.html', name=name, age=age)

# define the route to father webpage
@app.route("/father")
def father():
    father_name = ""  # write father's name
    father_age = ""   # write father's age

    return render_template('father.html', name=father_name, age=father_age)

# define the route to mother webpage
@app.route("/mother")
def mother():
    mother_name = ""  # write mother's name
    mother_age = ""   # write mother's age

    return render_template('mother.html', name=mother_name, age=mother_age)

# define the route to friends webpage
@app.route("/friends")
def friends():
    friend_names = ["", "", ""]  # write friend names
    friend_ages = ["", "", ""]    # write friend ages

    return render_template('friends.html', names=friend_names, ages=friend_ages)

# add other routes, if you want

# run the file
if __name__ == '__main__':
    app.run(debug=True)
