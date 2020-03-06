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


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        # fields = ["uuid","name","user_in_group","column"]
        fields = "__all__"

    def create(self, validated_data):
        users_data = validated_data.pop('user_in_group') 
        columns_data = validated_data.pop('column')
        name=validated_data.pop('name')

        group = super().create(validated_data)
        group.user_in_group.set(users_data)
        group.column.set(columns_data)
        return group        

    def update(self, instance, validated_data):
        #if validated_data.get('name', instance.name) != "":
        instance.name = validated_data.get('name', instance.name)
        #if validated_data.get('user_in_group', instance.user_in_group) != "[]":
        instance.user_in_group.set(validated_data.get('user_in_group', instance.user_in_group))
        #if validated_data.get('column', instance.column) !="[]":
        instance.column.set(validated_data.get('column', instance.column))
        instance = super().update(instance, validated_data)
        return instance



    # checkkkkkkkkkk
class ContentSerializer(serializers.Serializer):
    class Meta:
        model = Todo
        exclude = ["pub_in_group"]


class ContentDetailSerializer(serializers.ModelSerializer):
        
    user_in_group = UserDisplayOnlyUsernameSerializer(many=True, write_only=True)
    pub_in_group = ContentSerializer(many=True, write_only=True)

    class Meta:
        model = Group
        fields = ["uuid","name","user_in_group","pub_in_group"]


class ContentSerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField(read_only=True)
    pub_user = serializers.StringRelatedField(read_only=True)
    deadline = serializers.DateTimeField(required=False)

    class Meta:
        model=Todo
        fields = ["uuid","pub_user","content","pub_group","column","importance_level","column","deadline"]

    def validate(self, data):
        group_list = []
        column_list = []
        # ここが肝
        # print(self.context['request'].user)
        for item in Group.objects.filter(user_in_group__username= self.context['request'].user).values_list('name', flat=True):
            group_list.append(item)
            
        for item in Group.objects.get(name=data.get("pub_group")).column.all().values_list(flat=True):
            column_list.append(item)

        if not data.get("column") in column_list:
            raise serializers.ValidationError(
                    "アクセス許可のあるカラムに含まれていません")       

        elif self.context['request'].user.is_superuser:
            return data

        elif not str(data.get("pub_group")) in group_list:
            raise serializers.ValidationError(
                    "あなたはこのグループに投稿できません") 

        return data

    # def validate_column(self, value):
    #     if value in Column.objects.get():
    #         print("アクセス許可のあるカラムに含まれています")
    #         return data





# {"name": "try from json","user_in_group": [{"username": "Tom"},{"username": "Jiro"}],"column": [{"name": "TO DO"}]}
# {"username": "Tom"}
# {"name": "test from json","user_in_group": ["5b20f990-97ef-41a6-8b30-2d8b785605aa","556d47a5-8e08-4bdb-8af9-a1b39c3f6c96"],"column": [1]}