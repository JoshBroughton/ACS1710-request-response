from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user"""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal"""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_desert>')
def favorite_dessert(users_desert):
    """Display a message to the user that changes based on their favorite dessert"""
    return f'How did you know I liked {users_desert}?'

if __name__ == '__main__':
    app.run(debug=True)
