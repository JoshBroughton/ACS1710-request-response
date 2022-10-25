from flask import Flask
from random import randint

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

@app.route('/madlibs/<adjective>/<noun>')
def mad_libs(adjective, noun):
    """Takes in two strings, an adjective and a noun, and displays a short story with them"""
    return f'It is a little known fact that a {adjective} {noun} was responsible for the fall of Rome.'

@app.route('/multiply/<number1>/<number2>')
def multiply_two_numbers(number1, number2):
    """Takes in two numbers are route variables, validates input, then 
    returns the product of the numbers or an error if they are not numbers"""
    if number1.isdigit() and number2.isdigit():
        product = int(number1) * int(number2)
        return f'{number1} times {number2} is {product}'
    else:
        return 'Invalid inputs. Please try again by entering 2 numbers!'

@app.route('/sayntimes/<word>/<n>')
def say_n_times(word, n):
    """Takes in two strings, a word word and a number n; repeats the word number of times
    Checks input for n to ensure it is numeric; does not check what is entered as word as any
    input will be a string"""
    if n.isdigit():
        out_string = f'{word * int(n)}'
        return out_string
    else:
        return 'Invalid input. Please try again by enetering a word and a number!'

@app.route('/dicegame')
def dice_game():
    roll = randint(1, 6)
    out_string = f'You rolled a {roll}.'
    if roll == 6:
        out_string += ' You won!'
    else:
        out_string += ' You lost!'
    return out_string

if __name__ == '__main__':
    app.run(debug=True)
