from tortoise.models import Model
from tortoise import fields

class User(Model):
    id = fields.IntFiled(primary_key=True)
    name = fields.CharField(max_length=240)
    email = fields.CharField(max_length=240)
    password = fields.TextField()
    