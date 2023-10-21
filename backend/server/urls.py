from django.urls import path, include
from server import views
from rest_framework.routers import DefaultRouter, SimpleRouter

router = DefaultRouter()
# router.register("api/server/select/", views.ServerListViewSet)
router.register('api/server/select', views.ServerListViewSet )

urlpatterns = [
    path('', include(router.urls)),
] 