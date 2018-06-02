from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField


class NoteForm(FlaskForm):
    body = TextAreaField('Note')
    submit = SubmitField('Add Note')


class DeleteNotes(FlaskForm):
    submit = SubmitField('Clear notepad')
