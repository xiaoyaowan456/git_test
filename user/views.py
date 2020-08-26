import datetime

from flask import Blueprint
from flask import request
from flask import redirect
from flask import session
from sqlalchemy.exc import IntegrityError
from flask import render_template

from libs.orm import db
from libs.utils import make_password
from libs.utils import check_password
from libs.utils import save_avatar
from user.models import User


user_bp = Blueprint(
    'user',
    __name__,
    url_prefix='/user',
    template_folder='./templates'
                    )



@user_bp.route('/register', methods=('POST', 'GET'))
def register():
    if request.method == 'POST':
        #get里面没有的空单引号'' 的意义是 如果你没有写里面内容的话，默认是''
        # strip() 的作用是把字符串两边的空白符去掉，但是不会去掉字符串内部的空白符

        nickname = request.form.get('nickname', '').strip()
        password1 = request.form.get('password1', '').strip()
        password2 = request.form.get('password1', '').strip()
        gender = request.form.get('gender', '').strip()
        birthday = request.form.get('birthday', '').strip()
        city = request.form.get('city', '').strip()
        bio = request.form.get('avatar', '').strip()
        now = datetime.datetime.now()  #注册时间

        if not password1 or password1 != password2:
            return render_template('register.html', err='密码不符合要求')

        user = User(
            nickname=nickname,
            password=make_password(password1),
            gender=gender,
            birthday=birthday,
            city=city,
            bio=bio,
            created=now
        )

        #保存头像
        avatar_file = request.files.get('avatar')
        if avatar_file:
            # print(dir(avatar_file.stream))
            # avatar_url = save_avatar(avatar)
            # user.avatar = avatar_url
            user.avatar = save_avatar(avatar_file)

        try:
            #保存到数据库
            db.session.add(user)
            db.session.commit()
            return redirect('/user/login')
        except IntegrityError:
            db.session.rollback()
            # print(e)
            return render_template('register.html', err='您的昵称已被占用')
    else:
        return render_template('register.html')

@user_bp.route('/login', methods=('POST', 'GET'))
def login():
    return render_template('login.html')

@user_bp.route('/logout')
def logout():
    return redirect('/')

@user_bp.route('/info')
def info():
    return render_template('info.html')