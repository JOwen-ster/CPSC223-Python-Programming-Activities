# --------------------WRITE YOUR CODE BELOW-------------------#
import os
import re
import math
import random
import statistics
import datetime
import timeit
import reprlib
import pprint
import textwrap
from string import Template
import logging
import heapq


def list_files_in_directory(directory_path : str):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            print(os.path.join(root, file))

def extract_emails(text : str):
    emails : list = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    for email in emails:
        print(email)

def calculate_square_root(number : float):
    print(F"Square root of {number} is {math.sqrt(number)}")

def generate_random_integer(start : int, end : int):
    print(F"Random integer between {start} and {end}: {random.randint(start, end)}")

def calculate_mean_and_stddev(numbers : list):
    print(F"Mean: {statistics.mean(numbers)}, Standard Deviation: {statistics.stdev(numbers)}")

def print_current_datetime():
    print(F"Current date and time: {datetime.datetime.now()}")

def time_function_execution():
    def func():
        return [random.random() for _ in range(100)]
    time_taken = timeit.timeit(func, number=10000)
    print(F"Time taken to execute the function 10000 times: {time_taken} seconds")

def truncate_long_string(text : str):
    print(reprlib.repr(text))

def pretty_print_nested_dict(nested_dict : dict):
    pprint.pprint(nested_dict)

def wrap_text_paragraph(paragraph : str, line_length : int):
    print(textwrap.fill(paragraph, line_length))

def generate_sql_query(table_name : str, columns : str):
    query = Template("SELECT $columns FROM $table_name")
    print(F"Generated SQL Query: {query.substitute(columns=columns, table_name=table_name)}")

def setup_logging():
    logging.basicConfig(filename='app.log', level=logging.INFO)
    logging.info('Started')

def perform_heap_operations(numbers : list):
    heapq.heapify(numbers)
    print(F"Heap list: {numbers}")
    print(F"Smallest number: {heapq.heappop(numbers)}")


# --------------------END OF YOUR CODE------------------------#

'''
CREATE THE BELOW CALLED FUNCTION DEFINITION IN YOUR CODE!
'''

if __name__ == '__main__':

    # Sample data for tasks
    sample_text = "Sample email addresses: abc@example.com, xyz@domain.com"
    sample_numbers = [2, 4, 6, 8, 10]
    sample_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
    sample_paragraph = "This is a long paragraph that needs to be wrapped to multiple lines for better readability."
    sample_number = 12345.67
    sample_table_name = "users"
    sample_columns = "id, name, email"
    sample_numbers_for_heap = [3, 1, 4, 1, 5, 9]

    # Task executions
    list_files_in_directory(".")  # Task 1
    extract_emails(sample_text)  # Task 2
    calculate_square_root(16)  # Task 3
    generate_random_integer(1, 100)  # Task 4
    calculate_mean_and_stddev(sample_numbers)  # Task 5
    print_current_datetime()  # Task 6
    time_function_execution()  # Task 7
    truncate_long_string("This is a very long string that needs to be truncated.")  # Task 8
    pretty_print_nested_dict(sample_dict)  # Task 9
    wrap_text_paragraph(sample_paragraph, 30)  # Task 10
    generate_sql_query(sample_table_name, sample_columns)  # Task 11
    setup_logging()  # Task 12
    perform_heap_operations(sample_numbers_for_heap)  # Task 13
