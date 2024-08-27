from flask import Blueprint, render_template

bp = Blueprint('user', __name__, url_prefix='/user')

@bp.route('/register', methods=['GET'])
def register():
    return render_template('register_user.html')
