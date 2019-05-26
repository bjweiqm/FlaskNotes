from flask import Blueprint

user_bp = Blueprint('user', __name__, url_prefix='/user')


@user_bp.route('/profile/')
def profile():

    return '个人中心'

@user_bp.route('/settings/')
def settings():

    return '设置中心'

