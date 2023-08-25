import sys
from allow_braces import fixer, console, TestClass

import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        return
    
    file = sys.argv[1]
    
    try:
        with open(file, 'r') as f:
            code = f.read()
    except FileNotFoundError:
        print(f"File '{file}' not found.")
        return

    cx = code.replace('const ', '').replace('var ', '').replace('let ', '').replace('string ', '').replace('// ', '# ')
    cx = cx.replace('function', 'def').replace('new', '')
    cx = cx.replace('//', '"""').replace('//', '"""')
    cx = cx.strip()

    try:
        fixer(cx)
    except NameError as e:
        variable_name = str(e).split("'")[1]
        error_message = f"Uncaught ReferenceError: {variable_name} is not defined"
        console.error(error_message)
    except SyntaxError as e:
        value_that_cause_error = str(e.text).strip()
        error_message = f"Uncaught SyntaxError: {e.msg} '{value_that_cause_error}'"
        console.error(error_message)
    except TypeError as e:
        console.error(f"Uncaught TypeError: {str(e).replace('.__init__()', '').replace('required positional argument: ', 'argument ').replace('missing', 'needs')}")

if __name__ == "__main__":
    main()
