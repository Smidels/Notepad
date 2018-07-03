from flask import render_template, redirect, url_for
from app import app, db
from app.forms import NoteForm, DeleteNotes
from app.models import Note
from collections import OrderedDict


@app.route('/', methods=['GET', 'POST'])
@app.route('/write_note', methods=['GET', 'POST'])
def add_note():
    form = NoteForm()
    if form.validate_on_submit():
        count = len(set(form.body.data.split()))
        note = Note(body=form.body.data, counter_unique_words=count)
        db.session.add(note)
        db.session.commit()
        return redirect(url_for('add_note'))
    return render_template('add_note.html', title='Add Note', form=form)


@app.route('/view_notes', methods=['GET', 'POST'])
def view_notes():
    form = DeleteNotes()
    if form.validate_on_submit():
        Note.query.delete()
        db.session.commit()
        redirect(url_for('view_notes'))


    notes_dict = dict((note.body, note.counter_unique_words) for note in Note.query.all())
    notes = OrderedDict(sorted(notes_dict.items(), key=lambda t: t[1]))
    return render_template('view_notes.html', title='View Notes', notes=notes, form=form)
