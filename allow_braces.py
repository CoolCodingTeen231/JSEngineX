import re
import os
import importlib
import requests

true = True
false = False
null = None

def replacerLogic(txt: str) -> str:
    a = str(txt).replace("True", "true")
    b = str(txt).replace("False", "false")
    c = str(txt).replace("None", "null")
    return c
class TestClass:
    def __init__(self, test) -> None:
        self.test = test
    def tryTest(self):
        print(self.test)

def String(txt) -> str: return str(txt)
def TypeInput(begin):return input(begin)
def fetch(url, response_type):
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json() if response_type == 'json' else response.text
        return data
    except requests.exceptions.RequestException as e:
        console.error(e)
    except TypeError as exa:
        console.error(exa)
class console:
    loga = None
    @classmethod
    def log(cls, message):
        cls.loga = message
        print(replacerLogic((cls.loga)))
    @staticmethod
    def error(text):
        print("\033[91m" +  replacerLogic(text) + "\033[0m")
    @staticmethod
    def warn(text):
        print("\033[93m" +   replacerLogic(text) + "\033[0m")
    @staticmethod
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
def eval(code):
    exec(str(code).strip())

def require(package):
    package = str(package).replace('.js', '')
    globals()[package] = importlib.import_module(package)

def fixer(input_code):
    pattern = r'(def|class)\s+(\w+)\s*\((.*?)\)\s*{([^}]+)}'
    
    def replace_function(match):
        keyword = match.group(1)
        name = match.group(2)
        parameters = match.group(3)
        body = match.group(4)

        if keyword == 'def':
            new_definition = f'def {name}({parameters}):'
        elif keyword == 'class':
            new_definition = f'class {name}({parameters}):'
        indented_body = '\n'.join(['    ' + line.strip() for line in body.split('\n')])
        return f'{new_definition}\n{indented_body}'
    output_code = re.sub(pattern, replace_function, input_code)
    exec(output_code.strip())
def typeof(txt):
    if isinstance(txt, str):
        console.log("string")
    if isinstance(txt, int):
        console.log('number')
    if isinstance(txt, bool):
        console.log('boolean')