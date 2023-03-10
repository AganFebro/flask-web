from flask import Blueprint, render_template, request, flash, jsonify
from datetime import date, datetime, timedelta
from sqlalchemy import func
from flask_login import login_required, current_user
from .models import Note, Note1
from . import db
import json
from flask import url_for,redirect #Tambahan

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/pemasukan', methods=['GET', 'POST'])
@login_required
def pemasukan_input():
    if request.method == 'POST':
        note = request.form.get('note')
        jumlah = request.form.get('jumlah')
        new_note = Note(data=note, jumlah=jumlah, user_id=current_user.id)
        db.session.add(new_note)
        db.session.commit()
        flash('Data pemasukan ditambahkan!', category='success')
        return redirect(url_for('views.pemasukan_input'))

    return render_template("pemasukan.html", user=current_user)

@views.route('/pengeluaran', methods=['GET', 'POST'])
@login_required
def pengeluaran_input():
    if request.method == 'POST':
        jumlah1 = request.form.get('jumlah1')
        note1 = request.form.get('note1')

        new_note1 = Note1(data1=note1, jumlah1=jumlah1, user_id1=current_user.id)
        db.session.add(new_note1)
        db.session.commit()
        flash('Data pengeluaran ditambahkan!', category='success')
        return redirect(url_for('views.pengeluaran_input'))

    return render_template("pengeluaran.html", user=current_user)

@views.route('/delete-note-pemasukan', methods=['POST'])
def delete_note_pemasukan():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route('/delete-note-pengeluaran', methods=['POST'])
def delete_note_pengeluaran():
    note1 = json.loads(request.data)
    noteId1 = note1['noteId1']
    note1 = Note1.query.get(noteId1)
    if note1:
        if note1.user_id1 == current_user.id:
            db.session.delete(note1)
            db.session.commit()

    return jsonify({})

@views.route('/about')
@login_required
def about():
    return render_template("about.html", user=current_user)

@views.route('/pengeluaran')
@login_required
def pengeluaran():
    return render_template("pengeluaran.html", user=current_user)

@views.route('/pemasukan')
@login_required
def pemasukan():
    return render_template("pemasukan.html", user=current_user)

@views.route('/profile')
@login_required
def profile():
    return render_template("profile.html", user=current_user)