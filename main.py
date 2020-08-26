#！/usr/bin/env.python

from flask import Flask
from flask import  render_template
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from libs.orm import db
from user.views import user_bp


#初始化app
app = Flask(__name__)
app.secret_key = r'sdhajlkdhjql22jkjklfdnfui43phj#@#Rdwfjf8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:JUSTDOIT0718@localhost:3306/weibo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # 每次请求结束后都会自动提交数据库中的变动

#初始化manager
manager = Manager(app)

#初始化db 和 migrate
db.init_app(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

#注册蓝图
app.register_blueprint(user_bp)

@app.route('/')
def home():
    '''首页'''
    return 'hello world'




if __name__ == '__main__':
    manager.run()


