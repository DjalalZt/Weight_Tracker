from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Weights
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)


@views.route('/add', methods=['POST', 'GET'])
@login_required
def add(): 
    if request.method == 'GET':
        return render_template("add.html", user=current_user)
    else:
        weight = request.form.get('add')
        num_weight = int(weight)
        if num_weight > 0:
            flash('Weight added successfully!', category='success')
            new_weight = Weights(weight=num_weight, user_id=current_user.id)
            db.session.add(new_weight)
            db.session.commit()
            return redirect(url_for('views.add'))
        else:
            flash('Please enter an non null positive number', category='error')
            return redirect(url_for('views.add'))    


@views.route('/show')
@login_required
def show():
    return render_template("show.html", user=current_user)


##@views.route('/delete-note', methods=['POST'])
##def delete_note():
##    note = json.loads(request.data)
##    noteId = note['noteId']
##    note = Note.query.get(noteId)
##    if note:
##        if note.user_id == current_user.id:
##            db.session.delete(note)
##            db.session.commit()
            
##    return jsonify({})