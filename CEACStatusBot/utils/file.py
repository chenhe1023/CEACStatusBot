import os

FILE_NAME = "status.txt"

def read():
    try:
        with open(FILE_NAME, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return ""
    except IOError:
        return f"Error: There was an issue reading the file '{FILE_NAME}'."

def write(content):
    try:
        with open(FILE_NAME, 'w') as file:
            file.write(content)
        return f"Successfully wrote to '{FILE_NAME}'."
    except IOError:
        return f"Error: There was an issue writing to the file '{FILE_NAME}'."
