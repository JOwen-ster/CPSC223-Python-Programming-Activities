import calculator
import json

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError as vE:
            print(vE)
    

def main():
    print('Welcome User!')
    print('Please enter float value')
    num1 = get_float_input('Please enter a number: ')
    num2 = get_float_input('Please enter a number: ')
    results = {
        'num1': num1,
        'num2': num2,
        'Addition': calculator.add(num1,num2),
        'Subtraction': calculator.subtract(num1,num2),
        'Multiplication': calculator.multiply(num1,num2),
        'Division': calculator.divide(num1,num2)
    }

    filename = input('Enter a filename for the JSON')
    try:
        with open(filename, 'w') as file:
            json.dump(results, file)
            print(F'Saved to {filename}')
    except ValueError as vE:
        print(vE)






