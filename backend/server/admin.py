from django.contrib import admin

from server.models import Category, Channel, Server



admin.site.register(Channel)
admin.site.register(Server)
admin.site.register(Category)
