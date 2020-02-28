from todo.models import Group, Todo
from rest_framework import serializers

from users.api.serializers import UserDisplayOnlyUsernameSerializer

class GroupSerializer(serializers.ModelSerializer):

    user_in_group = UserDisplayOnlyUsernameSerializer(many=True)

    class Meta:
        model = Group
        fields = ["id","name","user_in_group"]


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        exclude = ['pub_group']


class ContentDetailSerializer(serializers.ModelSerializer):
        
    user_in_group = UserDisplayOnlyUsernameSerializer(many=True)
    pub_in_group = ContentSerializer(many=True)

    class Meta:
        model = Group
        fields = ["id","name","user_in_group","pub_in_group"]


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



