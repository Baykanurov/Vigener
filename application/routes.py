from application.app import app
from flask import request, render_template
from application.forms.ui_forms import LoginForm
from application.function.vigenereCipher import encryptMessage, decryptMessage
from application.function.vigenereHacker import hackVigenere


@app.route('/', methods=['GET', 'POST'])
def base():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        if request.method == 'POST' and request.form.get('key') and request.form.get('encrypt'):
            form.redactor2.data = encryptMessage(request.form.get('key'), request.form.get('redactor1'))
            return render_template('index.html', title="Виженер", form=form)

        elif request.method == 'POST' and request.form.get('key') and request.form.get('decrypt'):
            form.redactor2.data = decryptMessage(request.form.get('key'), request.form.get('redactor1'))
            return render_template('index.html', title="Виженер", form=form)

        elif request.method == 'POST' and request.form.get('vzlom'):
            result = hackVigenere(request.form.get('redactor1'))
            form.redactor2.data = result
            return render_template('index.html', title="Виженер", form=form)

        elif request.method == 'POST' and request.form.get('splash'):
            text1 = request.form.get('redactor1')
            text2 = request.form.get('redactor2')
            form.redactor2.data = text1
            form.redactor1.data = text2
            return render_template('index.html', title="Виженер", form=form)

        elif request.method == 'POST' and request.form.get('clear1'):
            form.redactor1.data = ""
            return render_template('index.html', title="Виженер", form=form)

        elif request.method == 'POST' and request.form.get('clear2'):
            form.redactor2.data = ""
            return render_template('index.html', title="Виженер", form=form)

    return render_template('index.html', title="Виженер", form=form)

