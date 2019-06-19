from wtforms import Form, IntegerField, StringField, FileField
from wtforms.validators import Length, InputRequired
from flask_wtf.file import FileAllowed, FileRequired


class UploadForm(Form):
    # 过滤文件
    avatar = FileField(validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif'])])
    desc = StringField(validators=[InputRequired()])
