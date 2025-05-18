# Syntax to Execution: Building a Basic Compiler

## Project Overview
This project implements a basic compiler that takes simple arithmetic and assignment expressions as input, performs lexical analysis, parsing, and semantic analysis, and outputs the evaluated result. It is designed as part of the Compiler Design coursework to demonstrate key compiler phases and concepts.

## Features
- Lexical Analysis using PLY (Python Lex-Yacc)
- Parser with grammar rules to handle assignments and arithmetic expressions
- Semantic analysis with symbol table management
- Basic error handling for illegal characters and undeclared variables
- Simple web interface using Flask and CodeMirror for code editing and compiling

## Technology Stack
- Python 3
- PLY (Python Lex-Yacc)
- Flask (Web Framework)
- HTML/CSS/JavaScript (Front-end)
- CodeMirror (Code Editor Integration)

## How to Run
1. Clone the repository:
git clone https://github.com/yourusername/compiler-project.git
2. Create and activate a Python virtual environment:
python3 -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
3. Install dependencies:
pip install -r requirements.txt
4. Run the Flask app:
python app.py
5. Open your browser and navigate to:
(http://127.0.0.1:5050)
6. Write or paste your code in the editor and click **Compile** to see the output.

## Project Structure
compiler/ # Contains lexer.py and parser.py
templates/ # HTML templates (index.html)
static/ # CSS, JS, including CodeMirror assets (if not CDN)
app.py # Flask application
requirements.txt # Python dependencies
README.md # Project documentation

## Team Roles
- **Shriya**: Lead Developer and Grammar Designer — defined grammar rules, symbol table, and semantic checks.
- **Riya**: Lexer Developer — implemented the lexical analyzer to tokenize input.
- **Niharika**: Parser Developer — built the parser to construct parse trees and syntax validation.
- **Siddhi**: Web Integration and Testing — developed Flask app, integrated CodeMirror editor, and handled testing and deployment.

## Future Scope
- Extend grammar to support more language constructs (loops, functions, arrays)
- Add intermediate code generation and optimization phases
- Support for detailed error reporting and debugging
- Implement code generation for a target machine or virtual machine
- Enhance the web interface with features like syntax highlighting and auto-completion

## Known Issues
- Limited grammar scope; currently supports only simple arithmetic and assignment
- Semantic checks are basic and may need enhancement for complex programs
- No support for multi-line blocks or nested scopes yet


Thank you for exploring our compiler project!
