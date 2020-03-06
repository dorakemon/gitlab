from django.db import models
# Create your models here.
from django.conf import settings
import uuid

IMPORTANCE_LEVEL = ((1, 'normal'), (2, 'important'), (3, 'essential'), (4,'crucial'))

# DEFAULT_COLUMN = ((1, 'TO DO'), (2, 'IN PROGRESS'), (3, 'DONE'))

class Column(models.Model):
    name = models.CharField(max_length=40, unique=False)
    class Meta: 
        verbose_name = "カラム"
        verbose_name_plural = "カラム"

    def __str__(self):
        return self.name
    


# カラムを作って自分が自分のカラム買いに知化しようとするバリデーションをビュー側で作る
class Group(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, verbose_name="グループ名")
    user_in_group = models.ManyToManyField(settings.AUTH_USER_MODEL,
                               related_name="personal_group")
    column = models.ManyToManyField(Column, related_name="column_in_group")

    class Meta: 
        verbose_name = "グループ"
        verbose_name_plural = "グループ"

    def __str__(self):
        return self.name
    

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

    # シグナルでデフォで((1, 'TO DO'), (2, 'IN PROGRESS'), (3, 'DONE'))を入れる
    # 別モデルにする？
    column = models.ForeignKey(Column, related_name="todo_in_column", on_delete=models.CASCADE)
    row = models.IntegerField(null=True, blank=True)

    deadline = models.DateTimeField()

    class Meta: 
        verbose_name = "Todo"
        verbose_name_plural = "Todo"

    def __str__(self):
        return "{} {}".format(self.pub_user, self.content)
    
