from rest_framework import serializers
from users.models import User, Course, Faculty, Place


class CourseSerializer(serializers.ModelSerializer):
    """Userモデルのシリアライザのコースネストの子"""
    
    # ex) primary 1期 applicationコース が分かれているためそれを繋げる自作フィールド
    all_name = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'name', 'season_name', 'department_name', 'all_name']

    def get_all_name(self, instance):
        if instance.department_name == None:
            return "{}{}".format(instance.name, instance.season_name)
        else:
            return "{}{}{}".format(instance.name, instance.season_name, instance.department_name)


class FacultySerializer(serializers.ModelSerializer):
    """Userモデルのシリアライザの学部ネストの子"""

    university = serializers.SerializerMethodField()
    faculty = serializers.SerializerMethodField()
    university_faculty = serializers.SerializerMethodField()

    class Meta:
        model = Faculty
        fields = ['id', 'university', 'faculty', 'university_faculty',]

    def get_university(self, instance):
        return str(instance.university)

    def get_faculty(self, instance):
        return instance.name

    def get_university_faculty(self, instance):
        return "{} {}".format(instance.university, instance.name)


import sys
sys.path.append('../')
from todo.models import Group
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name']



class UserDisplaySerializer(serializers.ModelSerializer):
    gender = serializers.SerializerMethodField()
    place_name = serializers.ReadOnlyField(source='place.name')
    course = CourseSerializer(many=True)
    university_faculty = FacultySerializer()
    # user_group = serializers.SerializerMethodField()

    # ここうまく言った理由謎
    personal_group = GroupSerializer(many=True)

    class Meta:
        model = User
        fields = ["uuid","username","gender","birthday","place_name","course","university_faculty","is_superuser","personal_group"]

    def get_gender(self, instance):
        if instance.gender == 1:
            return "男性"
        if instance.gender == 2:
            return "女性"

class UserDisplayOnlyUsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]



class PlaceDislaySerializer(serializers.ModelSerializer):
    people_count = serializers.SerializerMethodField()

    class Meta:
        model = Place
        fields = ['name','people_count']

    def get_people_count(self, instance):
        return Place.objects.get(name=str(instance.name)).personal_place.all().count()

class PlaceDislayRetrieveSerializer(serializers.ModelSerializer):
    people_count = serializers.SerializerMethodField()
    personal_place = UserDisplayOnlyUsernameSerializer(many=True)

    class Meta:
        model = Place
        fields = ['name','people_count', 'personal_place']

    def get_people_count(self, instance):
        return Place.objects.get(name=str(instance.name)).personal_place.all().count()
    