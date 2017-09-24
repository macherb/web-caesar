from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <form action="/encrypt" method="post">
        <div>
          <label>Rotate by:</label>
          <input type="text" name="rot" value="0">
        </div>
        <textarea name="text">{0}</textarea>
        <br>
        <input type="submit">
      </form>
    </body>
</html>
"""

@app.route("/encrypt", methods=['POST'])
def encrypt():
    rot = request.form['rot']
    text = request.form['text']
    caesar = rotate_string(text, int(rot))
    return form.format(caesar)

@app.route("/")
def index():
    return form.format("")

app.run()