from users.models import User
from todo.models import Group, Todo, Column
from rest_framework import serializers

from users.api.serializers import UserDisplayOnlyUsernameSerializer

# from drf_writable_nested import WritableNestedModelSerializer

class ColumnSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    class Meta:
        model = Column
        fields = ["name"]

# ユーザーをリストに入れる カンマで区切る, 一つ一つをobjects.get()
class GroupSerializer(serializers.ModelSerializer):

    # user_in_group = UserDisplayOnlyUsernameSerializer(many=True)
    #user_in_group_id = serializers.PrimaryKeyRelatedField(
    #    queryset=User.objects.filter(), source='user_in_group', write_only=True)
    #column = ColumnSerializer(many=True)
    #column_id = serializers.PrimaryKeyRelatedField(
    #    queryset=Column.objects.filter(), source='column', write_only=True)

    class Meta:
        model = Group
        # fields = ["uuid","name","user_in_group","column"]
        fields = "__all__"

    def create(self, validated_data):
        users_data = validated_data.pop('user_in_group')
        columns_data = validated_data.pop('column')
        # user = User.objects.get(username=user_data['username'])
        # column = Column.objects.get(name=column_data['name'])
        # group = Group.objects.create(uner_in_group=user, column=column, **validated_data)
        #print("validatedata",users_data)
        #print("columndata",columns_data)
        group = Group.objects.create()
        for user_data in users_data:
            group = Group.objects.add(user_in_group=user_data, **validated_data)
        return group

    # def create(self, validated_data):
    #     users = self.user_in_group
    #     print(users)
    #     columns = self.column
    #     print(validated_data)
    #     # for users_data in validated_data.pop('user_in_group'):
    #     #     # ** ?
    #     #     users.append(Users.object.get(username=**users_data))
    #     # for column_data in validated_data.pop('column'):
    #     #     columns.append(Column.objects.get(name=**column_data))
    #     group = super().create(validated_data)
    #     # group.column.set(columns)
    #     # group.user_in_group.set(users)
    #     return group
        

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        exclude = ['pub_group']


class ContentDetailSerializer(serializers.ModelSerializer):
        
    user_in_group = UserDisplayOnlyUsernameSerializer(many=True, write_only=True)
    pub_in_group = ContentSerializer(many=True, write_only=True)

    class Meta:
        model = Group
        fields = ["uuid","name","user_in_group","pub_in_group"]


class ContentSerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField(read_only=True)
    pub_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model=Todo
        fields = ["uuid","pub_user","content","pub_group","importance_level","column"]

    def validate(self, data):
        group_list = []
        # ここが肝
        # print(self.context['request'].user)
        for item in Group.objects.filter(user_in_group__username= self.context['request'].user).values_list('name', flat=True):
            group_list.append(item)

        if self.context['request'].user.is_superuser:
            return data

        elif not str(data.get("pub_group")) in group_list:
            raise serializers.ValidationError(
                    "あなたはこのグループに投稿できません") 

        return data





# {"name": "try from json","user_in_group": [{"username": "Tom"},{"username": "Jiro"}],"column": [{"name": "TO DO"}]}
# {"username": "Tom"}