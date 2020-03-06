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

    # user_in_group=serializers.SerializerMethodField()

    class Meta:
        model = Group
        # fields = ["uuid","name","user_in_group","column"]
        fields = "__all__"

    # def get_user_in_group(self,instance):
    #     # return instance.user_in_group
    #     # return ', '.join([x for x in str(instance.user_in_group)])
    #     user_list = []
    #     for user in instance.user_in_group.all:
    #         user_list.append(str(User.objects.get(username=user)))
    #     return user_list


    def create(self, validated_data):
        users_data = validated_data.pop('user_in_group') 
        columns_data = validated_data.pop('column')
        name=validated_data.pop('name')

        group = super().create(validated_data)
        group.user_in_group.set(users_data)
        group.column.set(columns_data)
        return group        


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
        fields = ["uuid","pub_user","content","pub_group","column","importance_level","column","deadline"]

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
# {"name": "test from json","user_in_group": ["5b20f990-97ef-41a6-8b30-2d8b785605aa","556d47a5-8e08-4bdb-8af9-a1b39c3f6c96"],"column": [1]}