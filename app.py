from flask import Flask, render_template, request
from compiler.parser import parser  # Adjust import as needed

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    output = ""
    if request.method == "POST":
        code = request.form["code"]
        for line in code.strip().split("\n"):
            try:
                parser.parse(line)
            except Exception as e:
                output += f"Error: {str(e)}\n"
        output += "Compilation finished!"
    return render_template("index.html", output=output)

if __name__ == "__main__":
    app.run(debug=True)
