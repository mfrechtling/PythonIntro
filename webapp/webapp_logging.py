from flask import Flask, render_template, request
import mymodule

app = Flask(__name__)

def log_request(req: 'flask_request', res: str) -> None:
    with open('webapp.log', 'a') as log:
        print(req, res, file=log)

@app.route('/')
def home() -> 'html':
    return render_template('entry.html', page_title = 'Play with functions')

@app.route('/findcommonletters', methods=["POST"])
def findcommonletters() -> 'html':
    results = mymodule.find_common_vowels(request.form['sentence'], request.form['letters'])
    log_request(request, results)
    return render_template('results.html', results_title='Common letters', the_results=results)


@app.route('/countvowels', methods=["POST"])
def countvowels() -> 'html':
    results = mymodule.count_vowels(request.form['sentence'])
    log_request(request, results)
    return render_template('results.html', results_title='Vowel count', the_results=results)

app.run()
