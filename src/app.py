from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        test_string = request.form['test_string']
        regex = request.form['regex']

        matches = [(match.group(), match.start(), match.end()) for match in re.finditer(regex, test_string)]

        return render_template('index.html', matches=matches)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
