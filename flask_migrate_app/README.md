# 项目结构重构

run ： 运行文件入口
config  配置文件入口

## 循环引用

Python循环引用解决方案？

1. 创建仓库 init
2. 生成脚本 migrate
3. 生成库 upgrade

## flask-migrate

1. 安装 `pip install flask-migrate`

2. 在manage中的代码

    ```python
    from flask_script import Manager
    from run import app
    from ext import db
    from models import User  # 需要把映射到服务器中的模型导入到manage.py文件中
    from flask_migrate import Migrate, MigrateCommand

    manager = Manager(app)
    # 用来绑定APP 和 db到flask_migrage 的
    Migrate(app, db)
    # 添加Migrate的所有命令到db下
    manager.add_command('db', MigrateCommand)


    if __name__ == "__main__":
        manager.run()
    ```

3. flask-migrate常用命令
    1. 初始化一个环境：`python manage.py db init`
    2. 自动检测模型，生成迁移脚本：`python manage.py db migrate`
    3. 将迁移脚本映射到数据库中：`python manage.py db upgrade`
    4. 更多命令：`python manage.py db --help`
