from parser import parser

def run_code(code):
    for line in code.strip().split('\n'):
        parser.parse(line)

if __name__ == "__main__":
    with open("test_program.txt") as f:
        code = f.read()
        run_code(code)