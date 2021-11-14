from flask import Flask, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap

from forms import DataForm
from predict import get_form_data, predict
import pickle

app = Flask(__name__)
bootstrap = Bootstrap(app)

# app.run(host='0.0.0.0', port=5000, debug=True) 

app.config['SECRET_KEY'] = 'DAT158'


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])

def index():

    form = DataForm()
    if form.validate_on_submit():
        for fieldname, value in form.data.items():
            session[fieldname] = value

        data = get_form_data(session)
 
        pred = predict(data)
        return redirect(url_for('index'))
    return render_template('index.html', form=form)


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
    
if __name__ == "__main__":
    app.run(debug=True)