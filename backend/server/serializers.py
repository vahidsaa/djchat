from rest_framework import serializers
from server.models import Category, Server, Channel


class ChannelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Channel
        fields = "__all__"



class ServerSerializer(serializers.ModelSerializer):
    #related_name = channel_server  - va chon channel ha mitone ziad bashe az many=True estefade.
    channel_server = ChannelSerializer(many=True)

    class Meta:
        model =Server
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"