from flask import Blueprint, render_template, session, request, redirect, url_for, flash, jsonify

from vertexFunction import vertexCall


views = Blueprint("views", __name__)

def checkSession():
    if 'sidebar_state' not in session:
        session['sidebar_state'] = 'open'

@views.route('/')
def index():
    if 'sidebar_state' not in session:
        session['sidebar_state'] = 'open'
    return redirect(url_for('views.home'))

@views.route('/home', methods=['GET'])
def home():
    return render_template('home.html', current_page='home')

@views.route('/home-backup', methods=['GET'])
def homebackup():
    return render_template('home-backup.html', current_page='home-backup')

@views.route('/syntax', methods=['GET'])
def syntax():
    checkSession()
    return render_template('syntax.html', current_page='syntax')

@views.route('/comments', methods=['GET'])
def comments():
    checkSession()
    return render_template('comments.html', current_page='comments')

@views.route('/variables', methods=['GET'])
def variables():
    checkSession()
    return render_template('variables.html', current_page='variables')

@views.route('/variableNames', methods=['GET'])
def variableNames():
    checkSession()
    return render_template('variableNames.html', current_page='variableNames')

@views.route('/assignMultipleValues', methods=['GET'])
def assignMultipleValues():
    checkSession()
    return render_template('assignMultipleValues.html', current_page='assignMultipleValues')

@views.route('/outputVariables', methods=['GET'])
def outputVariables():
    checkSession()
    return render_template('outputVariables.html', current_page='outputVariables')

@views.route('/datatypes', methods=['GET'])
def datatypes():
    checkSession()
    return render_template('datatypes.html', current_page='datatypes')

@views.route('/numbers', methods=['GET'])
def numbers():
    checkSession()
    return render_template('numbers.html', current_page='numbers')

@views.route('/casting', methods=['GET'])
def casting():
    checkSession()
    return render_template('casting.html', current_page='casting')


@views.route('/pythonStrings', methods=['GET'])
def pythonStrings():
    checkSession()
    return render_template('pythonStrings.html', current_page='pythonStrings')

@views.route('/slicingStrings', methods=['GET'])
def slicingStrings():
    checkSession()
    return render_template('slicingStrings.html', current_page='slicingStrings')

@views.route('/modifyStrings', methods=['GET'])
def modifyStrings():
    checkSession()
    return render_template('modifyStrings.html', current_page='modifyStrings')

@views.route('/concatenateStrings', methods=['GET'])
def concatenateStrings():
    checkSession()
    return render_template('concatenateStrings.html', current_page='concatenateStrings')

@views.route('/formatStrings', methods=['GET'])
def formatStrings():
    checkSession()
    return render_template('formatStrings.html', current_page='formatStrings')

@views.route('/escapeStrings', methods=['GET'])
def escapeStrings():
    checkSession()
    return render_template('escapeStrings.html', current_page='escapeStrings')

@views.route('/stringMethods', methods=['GET'])
def stringMethods():
    checkSession()
    return render_template('stringMethods.html', current_page='stringMethods')

@views.route('/booleans', methods=['GET'])
def booleans():
    checkSession()
    return render_template('booleans.html', current_page='booleans')

@views.route('/operators', methods=['GET'])
def operators():
    checkSession()
    return render_template('operators.html', current_page='operators')

@views.route('/tuples', methods=['GET'])
def tuples():
    checkSession()
    return render_template('tuples.html', current_page='tuples')

@views.route('/ifelse', methods=['GET'])
def ifelse():
    checkSession()
    return render_template('ifelse.html', current_page='ifelse')

@views.route('/whileloops', methods=['GET'])
def whileloops():
    checkSession()
    return render_template('whileloops.html', current_page='whileloops')

@views.route('/forloops', methods=['GET'])
def forloops():
    checkSession()
    return render_template('forloops.html', current_page='forloops')

@views.route('/functions', methods=['GET'])
def functions():
    checkSession()
    return render_template('functions.html', current_page='functions')

@views.route('/lambdas', methods=['GET'])
def lambdas():
    checkSession()
    return render_template('lambdas.html', current_page='lambdas')

@views.route('/toggle_sidebar')
def toggle_sidebar():
    return jsonify({'sidebar_state': session.get('sidebar_state', 'collapsed')})

@views.route('/toggleSidebar')
def toggleSidebar():
    # # Toggle sidebar state between 'open' and 'collapsed'
    if session['sidebar_state'] == 'open':
        session['sidebar_state'] = 'collapsed'
    else:
        session['sidebar_state'] = 'open'
    return jsonify({'sidebar_state': session.get('sidebar_state', 'collapsed')})

@views.route('/askVertex', methods=['POST'])
def askVertex():
    message = request.json.get('message')
    if message:
        reply = vertexCall(message)
        return jsonify({'reply': reply}), 200
    else:
        return jsonify({'error': 'No message provided'}), 400


# ? do we need this
@views.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        user_text = request.form['user_text']
        print("User input:", user_text)
    return render_template('chat.html')