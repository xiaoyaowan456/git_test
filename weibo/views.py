from flask import Blueprint

from flask import render_template
from flask import request
from flask import redirect
from flask import session

# from libs.utils import login_required
from weibo.models import Weibo


# weibo_bp = Blueprint(
#     'weibo',
#      __name__,
#      url_prefix='/weibo',
#      template_folder='./templates'
#                      )
#
# @weibo_bp.route('/index')
# def index():
#     '''微博首页'''
#     return ''
#
#
# @weibo_bp.route('/post')
# @login_required
# def post_weibo():
#     '''发布微博'''
#     pass
#
#
# @weibo_bp.route('/read')
# @login_required
# def read_weibo():
#     '''阅读微博'''
#     pass
#
#
# @weibo_bp.route('/edit')
# @login_required
# def edit_weibo():
#     '''退出微博'''
#     pass
#
#
# @weibo_bp.route('/delete')
# @login_required
# def delete_weibo():
#     '''删除微博'''
#     pass