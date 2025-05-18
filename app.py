from flask import Flask, render_template, request
import io
import sys
from compiler.parser import parser

app = Flask(__name__)
from compiler.parser import symbol_table
...
symbol_table.clear()  # ✅ Clear variables before parsing


@app.route("/", methods=["GET", "POST"])
def index():
    output = ""
    if request.method == "POST":
        from compiler.parser import symbol_table
        symbol_table.clear()

        code = request.form["code"].replace('\r\n', '\n').strip()

        old_stdout = sys.stdout
        sys.stdout = mystdout = io.StringIO()

        try:
            for line in code.strip().split("\n"):
                if line.strip():
                    parser.parse(line + '\n')  # Ensure valid newline
        except Exception as e:
            print(f"Error: {str(e)}")

        sys.stdout = old_stdout
        output = mystdout.getvalue()

        if not output.strip():
            output = "Compilation finished! (But no output)"

    return render_template("index.html", output=output)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False, port=5050)
