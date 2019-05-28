from flask import Blueprint

tools_bp = Blueprint('tools', __name__, subdomain='tools')


@tools_bp.route('/')
def tools_index():
    
    return 'tools inddex hello you .'