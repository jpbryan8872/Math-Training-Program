"""
Creator: Jonathan Bryan
Description: Math training program with different operators that scales with levels

Extra resources used:

https://docs.python.org/3/tutorial/errors.html
used for the try function in addition_and_subtraction function to validate the input is an integer

https://docs.python.org/3/library/random.html
used for the random numbers in the equations
"""

import random
import cProfile


def generate_question(used_operator, level, number_of_terms):
    """Generates question and prints with selected operator"""

    # Define starting variables
    scaling_operators = ['+', '-', 'x']
    scaling_level = 2
    total = 0

    # Print the current level
    print("\nLevel", level)

    # Scale the difficulty by adding another term at scaling level difficulty
    if used_operator in scaling_operators:
        if level % scaling_level == 0:
            number_of_terms += 1

    #
    for i in range(number_of_terms):
        if type(used_operator) == list:
            used_operator = used_operator[random.randint(1, len(used_operator)) - 1]
        random_number = random.randint(1, level)
        if i != number_of_terms - 1:
            print(random_number, used_operator, end=' ')
        else:
            print(random_number, ': ', sep='')
        if i == 0:
            total = random_number
        else:
            if used_operator == '+':
                total += random_number
            elif used_operator == '-':
                total -= random_number
            elif used_operator == 'x':
                total *= random_number
            elif used_operator == '/':
                total /= random_number
            elif used_operator == '//':
                total //= random_number
            elif used_operator == '%':
                total %= random_number
            else:
                total **= random_number
    input_answer = input()
    if input_answer == 'menu':
        return 0, 2
    try:
        input_answer = int(input_answer)
    except ValueError:
        print("Please input a number.")
    if input_answer == total:
        print("Correct! " * level)
        level += 1
    else:
        print("Wrong, the answer was", total, end='.\n')
    return level, number_of_terms


def main_func():
    """Docstring"""
    # Declaring starting variables and values
    current_level = 0
    selected_mode = 0
    current_number_of_terms = 2
    modes = ['1', '2', '3', '4', '5']

    # Create main running loop with quit value
    keep_running = True
    while keep_running:
        if current_level == 0:
            current_level = 1
            selected_mode = input("""
Welcome to the Fast Math Training Program!

At any time type "menu" to return here.

Select a difficulty:
    1. Addition and Subtraction
    2. Multiplication
    3. Division (rounded to 2 places), floor division, and remainders
    4. Exponents
    5. Quit

""")

        # Keep asking for input until a valid mode is selected
        while selected_mode not in modes:
            selected_mode = input("""
Invalid selection. Please try again.

Select a difficulty:
    1. Addition and Subtraction
    2. Multiplication
    3. Division (rounded to 2 places), floor division, and remainders
    4. Exponents
    5. Quit

""")

        # Generate a question using the correct operator, also updating the level and number of terms
        if selected_mode == '1':
            current_level, current_number_of_terms = generate_question(['+', '-'],
                                                                       current_level,
                                                                       current_number_of_terms
                                                                       )
        elif selected_mode == '2':
            current_level, current_number_of_terms = generate_question('x',
                                                                       current_level,
                                                                       current_number_of_terms
                                                                       )
        elif selected_mode == '3':
            current_level, current_number_of_terms = generate_question(['/', '//', '%'],
                                                                       current_level,
                                                                       current_number_of_terms
                                                                       )
        elif selected_mode == '4':
            current_level, current_number_of_terms = generate_question('^',
                                                                       current_level,
                                                                       current_number_of_terms
                                                                       )
        else:
            keep_running = False


cProfile.run('main_func()')
