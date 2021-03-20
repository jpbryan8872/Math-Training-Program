"""
Creator: Jonathan Bryan
Description: Math training program with different operators that scales with levels
"""

import random


def generate_question(operators, level, number_of_terms):
    """Generates question and prints with selected operator"""

    # Define starting variables
    scaling_operators = [['+', '-'], 'x']
    scaling_level = 10
    tally = 0
    final_answer = 0
    used_operator = ""
    problem = ""

    # Print the current level
    print("\nLevel", level)

    # Scale the difficulty by adding another term at scaling level difficulty
    if operators in scaling_operators and level % scaling_level == 0:
        number_of_terms += 1

    for term_number in range(number_of_terms):
        last_number = term_number == number_of_terms - 1

        # Prepare the operator for printing into the question
        last_operator = used_operator
        if type(operators) == list:
            used_operator = operators[random.randint(0, len(operators) - 1)]
        elif last_number:
            used_operator = last_operator
        else:
            used_operator = operators

        # Get a random number for the term
        random_number = random.randint(1, level)

        # Print the question (using addition with strings to create the complete problem)
        problem += str(random_number)
        if not last_number:
            problem += " " + used_operator + " "

        # Tally the final answer
        if term_number == 0:
            tally = random_number
        elif last_number:
            final_answer = calculate_answer(last_operator, random_number, tally)
        else:
            tally = calculate_answer(last_operator, random_number, tally)
    print(problem + ": ", end='')

    # Check the answer and return to main
    correct = check_answer(final_answer)
    if correct == "menu":
        return 0, 2
    elif correct:   # If the answer is correct
        # Multiplying "Correct!" times level to show correct streak
        print("Correct! " * level)
        level += 1
    else:  # If the answer is incorrect
        print("Wrong, the answer to", problem, "is", final_answer, end='.\n')
        level = 1
        number_of_terms = 2
    return level, number_of_terms


def calculate_answer(operator, term, tally):
    """Calculates the answer as the question is generated"""
    # Uses + - * / // % **
    if operator == '+':
        return tally + term
    elif operator == '-':
        return tally - term
    elif operator == 'x':
        return tally * term
    elif operator == '/':
        return tally / term
    elif operator == '//':
        return tally // term
    elif operator == '%':
        return tally % term
    else:
        return tally ** term


def check_answer(final_answer):
    """Checks the input answer against the calculated answer"""

    input_answer = input()

    # Loop to get good input
    check_input = False
    while not check_input:
        # Check for return to menu
        if input_answer == "menu":
            return input_answer
        try:
            input_answer = float(input_answer)
            check_input = True
        except ValueError:
            print("Please input a number. Try again:", end=' ')
            input_answer = input()
    if input_answer != round(final_answer, 2):
        return False
    else:
        return True


def main():
    """Main function that displays the menu"""
    # Declaring starting variables and values
    current_level = 0
    selected_mode = 0
    current_number_of_terms = 2
    valid_modes = ['1', '2', '3', '4', '5']

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
        while selected_mode not in valid_modes:
            selected_mode = input("""
Invalid selection. Please try again.

Select a difficulty:
    1. Addition and Subtraction
    2. Multiplication
    3. Division (rounded to 2 places), floor division, and remainders
    4. Exponents
    5. Quit
""")

        # Begins the question generation and calculation process
        # Passes different mathematical operators as arguments for questions
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


main()
