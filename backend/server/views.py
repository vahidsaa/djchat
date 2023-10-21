from django.shortcuts import render
from server.models import Category, Channel, Server
from server.serializers import ServerSerializer, CategorySerializer
from rest_framework import viewsets
from rest_framework.response import Response


class ServerListViewSet(viewsets.ViewSet):
    
    queryset = Server.objects.all()
   
    def list(self, request):
        
        #capture category (exteract that up)
        category = request.query_params.get("category")
        by_user = request.query_params.get("by_user") == "true"
        qty = request.query_params.get("qty")
        if category:
            #bejaye mostaghim fillter kardane querryset ( queryset = Server.objcets.all().filter(...))
            #va mishe bahash ba code (?category=2) category 2 ro faghat namayesh bede
            # self.queryset = self.queryset.filter(category=category) # ba in dastor az id estefade mishe
            self.queryset = self.queryset.filter(category__name=category)

        #vaghti in darkhast ba ?by_user=true omad faghat server haye marbot be on admino neshon bede
        if by_user:
            user_id = request.user.id
            self.queryset = self.queryset.filter(member=user_id)

        #baraye id on server? ya faghat 2 ta neshon bede ya qty=3 seta server neshon bede
        if qty:
            self.queryset = self.queryset[: int(qty)]

        serializer = ServerSerializer(self.queryset, many=True)
        return Response(serializer.data)