from flask import Blueprint, request, render_template

hello_bp = Blueprint('hello', __name__)

@hello_bp.route('/', methods=['GET'])
def hello():
    name = request.args.get('name', 'Invitado')
    return render_template('hello.html', name=name)