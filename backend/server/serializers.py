from rest_framework import serializers
from server.models import Category, Server, Channel


class ChannelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Channel
        fields = "__all__"



class ServerSerializer(serializers.ModelSerializer):
    #for adding members fields in apiview first add custome method
    num_members = serializers.SerializerMethodField()
    #related_name = channel_server  - va chon channel ha mitone ziad bashe az many=True estefade.
    channel_server = ChannelSerializer(many=True)

    class Meta:
        model =Server
        # fields = "__all__"
        exclude = ('member',)
    #and must add this def and writhe next def if not call for with_num_members dont show member = null
    def get_num_members(self, obj):
        if hasattr(obj, "num_members"):
            return obj.num_members
        return None
    #befor do that we must pass context in api view in views.py
    def to_representation(self, instance):
        data = super().to_representation(instance)
        num_members = self.context.get("num_members")
        if not num_members:
            data.pop("num_members", None)
        return data

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"