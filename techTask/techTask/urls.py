from django.contrib import admin
from rest_framework import routers
from django.urls import path, include, re_path
from women.views import *

router = routers.DefaultRouter()
router.register(r'api/v1/women', WomenAPIList)
router.register(r'api/v1/women', WomenAPIUpdate)
router.register(r'api/v1/womendelete', WomenAPIDestroy)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/women/', WomenAPIList.as_view()),
    path('api/v1/women/<int:pk>/', WomenAPIUpdate.as_view()),
    path('api/v1/womendelete/<int:pk>/', WomenAPIDestroy.as_view()),
]
