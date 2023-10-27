from app import app, db
from flask import render_template, url_for, redirect, flash
from app.forms import SubmitForm
from app.models import Address

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['GET', 'POST'])
def submission():
    form=SubmitForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        first_name=form.first_name.data
        last_name=form.last_name.data
        phone=form.phone.data
        address=form.address.data
        new_address=Address(first_name=first_name, last_name=last_name, phone=phone, address=address)
        db.session.add(new_address)
        db.session.commit()
        flash("A new address has been entered")
        return redirect(url_for('index'))
    return render_template('submit.html', form=form)
