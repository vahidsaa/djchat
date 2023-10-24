from django.db import models
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.dispatch import receiver


#for icon
def category_icon_upload_path(instance, filename):
    return f"category/{instance.id}/category_icon/{filename}"



class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    # add icon and banners but firs must be add media
    icon = models.FileField(upload_to=category_icon_upload_path ,null=True, blank='True', )

    #for (if add another icon delete first icon and add new)
    def save(self, *args, **kwargs):
        if self.id: # thats mean we have a image befor
            existing = get_object_or_404(Category, id=self.id)
            if existing.icon != self.icon:
                existing.icon.delete(save=False)
        super(Category, self).save(*args, **kwargs)

    #for if delete category also delete icon with signals
    @receiver(models.signals.pre_delete, sender='server.Category')
    def category_delete_files(sender, instance, **kwargs):
        for field in instance._meta.fields:
            if field.name == "icon":
                file = getattr(instance, field.name)
                if file:
                    file.delete(save=False)


    def __str__(self):
        return self.name




class Server(models.Model):
    name = models.CharField(max_length=100)
    #bejaye User az setting.auth.. estefade kardim hamon useri ke to account tarif kardim + auth_use.. ham to setting.py 
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="server_owner")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="server_category")
    description = models.CharField(max_length=250,blank=True, null=True)
    member = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.name


class Channel(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="channel_owner")
    topic = models.CharField(max_length=100)
    server = models.ForeignKey(Server, on_delete=models.CASCADE, related_name='channel_server')

    #for how saved in database (lower case)
    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super(Channel, self).save(*args, **kwargs)

    
    def __str__(self):
        return self.name