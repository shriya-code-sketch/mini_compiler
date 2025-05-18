# Syntax to Execution: Building a Basic Compiler

## Project Overview
This project implements a basic compiler that takes simple arithmetic, relational, logical, assignment, and conditional expressions, while statements cover expression statements, compound blocks, selection statements like if-else and switch-case as input, performs lexical analysis, parsing, and semantic analysis, and outputs the evaluated result. It is designed as part of the Compiler Design coursework to demonstrate key compiler phases and concepts.

## Features##
- Lexical Analysis using PLY
- Parsing with grammar rules for expressions, conditionals, and loops
- Semantic analysis with variable declarations and evaluations
- Support for:
  - Assignments (e.g., a = 5)
  - Arithmetic operations (+, -, *, /)
  - Comparison operators (<, >, ==)
  - if and if-else statements
  - while loops
  - switch cases
- Beautiful, single-page web UI built with Flask and CodeMirror

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

## Future Scope## Future Scope
- Add nested block support (e.g., braces or indentation)
- Implement intermediate code generation
- Introduce switch-case and for loops
- Add syntax error highlights in the UI
- Export output as downloadable files


## Known Issues
- Limited grammar scope
- Semantic checks are basic and may need enhancement for complex programs


Thank you for exploring our compiler project!
