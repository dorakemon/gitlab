
# Userを登録した瞬間に一人用のGroupを作る
# （またアドミン、メンターを入れたグループを作る）この是非について

# テストしていない
# apps.py __init__.pyにも記述

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Group

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
        # print(instance)
        # print(created)
        # print(sender)

# @receiver(post_save, sender=Todo)
# def Todo

