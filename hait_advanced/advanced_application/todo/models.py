from django.db import models

# Create your models here.
from django.conf import settings
import uuid

# ここUUIDかidどっちにする？
class Group(models.Model):
    name = models.CharField(max_length=50, verbose_name="グループ名")
    user_in_group = models.ManyToManyField(settings.AUTH_USER_MODEL,
                               related_name="personal_group")

    class Meta: 
        verbose_name = "グループ"
        verbose_name_plural = "グループ"

    def __str__(self):
        return self.name
    


IMPORTANCE_LEVEL = ((1, 'normal'), (2, 'important'), (3, 'essential'), (4,'crucial'))

DEFAULT_COLUMN = ((1, 'TO DO'), (2, 'IN PROGRESS'), (3, 'DONE'))

# もしかしたらrowが必要かも
class Todo(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.CharField(max_length=255, verbose_name="Todoの中身")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    pub_group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="pub_in_group")

    pub_user = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name="my_pub_todo")

    importance_level = models.IntegerField(choices=IMPORTANCE_LEVEL)

    # ここを動的に変えたいいいい！！！！！
    column = models.IntegerField(choices=DEFAULT_COLUMN)

    class Meta: 
        verbose_name = "Todo"
        verbose_name_plural = "Todo"

    def __str__(self):
        return "{} {}".format(self.pub_user, self.content)
    
