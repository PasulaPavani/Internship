from flask import Flask, render_template, request,jsonify
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form.get('test_string', '')
    regex_pattern = request.form.get('regex_pattern', '')
    matches = re.findall(regex_pattern, test_string)
    return render_template('results.html', test_string=test_string, regex_pattern=regex_pattern, matches=matches)


@app.route('/validate_email', methods=['POST'])
def validate():
    email = request.form['email']
    email_regex = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(email_regex, email):
        result = "Valid email address"
        color = "green"
    else:
        result = "Invalid email address. Please enter valid MailID"
        color = "red"
    return render_template('validate_email.html', result=result, color=color)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
