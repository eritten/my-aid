from flask import session, redirect, url_for, render_template, request
from . import main
from .forms import LoginForm


@main.route('/', methods=['GET', 'POST'])
def index():
    """Login form to enter a room."""
    name = request.args.get("name")
    room_name = request.args.get("room_name")
    if request.method == "POST":
        session['name'] = name
        session['room'] = room_name
        return redirect(url_for('.chat'))
#    elif request.method == 'GET':
#        form.name.data = session.get('name', '')
#        form.room.data = session.get('room', '')
    return render_template('index.html', name=name, room_name=room_name)


@main.route('/chat')
def chat():
    """Chat room. The user's name and room must be stored in
    the session."""
    name = session.get('name', '')
    room = session.get('room', '')
    if name == '' or room == '':
        return redirect(url_for('.index'))
    return render_template('chat.html', name=name, room=room)
