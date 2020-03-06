
# Userを登録した瞬間に一人用のGroupを作る
# （またアドミン、メンターを入れたグループを作る）この是非について

# テストしていない
# apps.py __init__.pyにも記述

from django.db.models.signals import post_save, pre_save, m2m_changed
from django.dispatch import receiver

from .models import Group
from .models import Todo

import sys
sys.path.append('../')
from users.models import User

@receiver(post_save, sender=User)
# createdは送られたかどうかのTrue、False
# instanceは名前 ニュートンとか
# senderはオブジェクト <class 'users.models.User'>
def post_save_user_signal_handler(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.create(name="personal_todos_for_{}".format(instance)) 
        user=User.objects.get(username=str(instance))
        group.user_in_group.add(user)
        # 1,2,3はそれぞれTO DO, IN PROGRESS, DONE
        group.objects.update(column=1)
        # print(instance)
        # print(created)
        # print(sender)


## ここがうまくいかない デフォルトのカラムをVueがわでユーザーに追加させるのはあり
# @receiver([post_save,m2m_changed], sender=Group)
# def post_save_todo_add_column(sender, instance, created, **kwargs):
#     if created:
#         print("signal fired")

#         print(group)
#         group.column.add(1,2,3)


# post_saveだと発火はするものの追加はされない
# @receiver(pre_save, sender=Group)
# def post_save_todo_add_column(sender, instance, **kwargs):

#     print("pre signal fired")
#     print(instance)
#     # group = Group.objects.get(name = instance.name)
#     # instance.column.add(1,2,3)
#     instance.column.add(1,2,3)
#     instance.profile.save()
