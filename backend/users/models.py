from django.db import models
import uuid

# Create your models here.
class University(models.Model):
    """大学名のモデル"""
    name = models.CharField(verbose_name="大学名", max_length=40)

    class Meta: 
        verbose_name = "大学"
        verbose_name_plural = "大学"

    def __str__(self):
        return self.name


class Faculty(models.Model):
    """大学の学部のモデル"""
    # related_nameは逆参照の時に用いる
    ## university = University.objects.get(name="早稲田大学")
    ## university.university_faculty.all()
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name="university_faculty")
    name = models.CharField(verbose_name="学部名", max_length=40)

    class Meta: 
        verbose_name = "学部"
        verbose_name_plural = "学部"

    def __str__(self):
        return "{} {}".format(self.university, self.name)
        #return self.name


class Course(models.Model):
    """
        コースのモデル  
        primary 1期とかadvanced 1期  
    """
    # 後でManyToMany その期間の人を皆取らないといけない related_name
    name = models.CharField(verbose_name="コース", max_length=40)
    season_name = models.CharField(verbose_name="時期", max_length=10, help_text="何期か")
    department_name = models.CharField(verbose_name="部門", max_length=40, help_text="必要な場合のみ", null=True, blank=True)

    class Meta: 
        verbose_name = "コース"
        verbose_name_plural = "コース"

    def __str__(self):
        if self.department_name == None:
            return "{} {}".format(self.name, self.season_name)
        else:
            return "{} {} {}".format(self.name, self.season_name, self.department_name)

class Place(models.Model):
    """ 開催地のモデル """
    name = models.CharField(verbose_name="開催地", max_length=40)

    class Meta: 
        verbose_name = "開催地"
        verbose_name_plural = "開催地"

    def __str__(self):
        return self.name


# Userモデルの継承
from django.contrib.auth.models import AbstractUser

GENDER = ((1, '男性'), (2, '女性'))

class User(AbstractUser):
    # 名前適当
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    birthday = models.DateField(verbose_name="誕生日", null=True)
    gender = models.IntegerField(choices=GENDER, verbose_name="性別", null=True)

    university_faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name="personal_university_faculty", null=True, verbose_name="大学・学部")

    course = models.ManyToManyField(Course, related_name="personal_course", verbose_name="コース", null=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="personal_place", default=1, verbose_name="開催場所")

    description = models.TextField(max_length=1023, null=True, blank=True, verbose_name="説明")
    # class Meta(AbstractUser.Meta):
    #     swappable = 'AUTH_USER_MODEL'
