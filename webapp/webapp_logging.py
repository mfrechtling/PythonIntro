from flask import Flask, render_template, request
import mymodule

app = Flask(__name__)

def log_request(req: 'flask_request', res: str) -> None:
    with open('webapp.log', 'a') as log:
        print(req, res, file=log)

def log_db(functionname, req: 'flask_request', res: str) -> None:
    """Log details of the web request to DB."""
    dbconfig = {'host': 'localhost',
            'user': 'app_user',
            'password': 'abcdefgh',
            'database': 'webapp_log',
            'use_pure': True}
    import DBTools
    with DBTools.MySqlConnection(dbconfig) as cursor:
        _SQL = """insert into log 
        (functionname, sentence, letters)
        values
        (%s, %s, %s)"""
        cursor.execute(_SQL, (functionname,
            req.form['sentence'],
            req.form['letters']))


@app.route('/')
def home() -> 'html':
    return render_template('entry.html', page_title = 'Play with functions')

@app.route('/findcommonletters', methods=["POST"])
def findcommonletters() -> 'html':
    results = mymodule.find_common_vowels(request.form['sentence'], request.form['letters'])
    #log_request(request, results)
    log_db('findcommonletters', request, results)
    return render_template('results.html', results_title='Common letters', the_results=results)


@app.route('/countvowels', methods=["POST"])
def countvowels() -> 'html':
    results = mymodule.count_vowels(request.form['sentence'])
    #log_request(request, results)
    log_db('countvowels', request, results)
    return render_template('results.html', results_title='Vowel count', the_results=results)

app.run()
