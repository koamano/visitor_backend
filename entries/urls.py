from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'entries', views.EntriesView, 'entries')

urlpatterns = [
    path('', include(router.urls))
]