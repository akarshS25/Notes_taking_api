
from django.urls import path,include
from api.views import NoteViewSet
from rest_framework import routers
from api import views


router = routers.DefaultRouter()
router.register(r'notes', NoteViewSet)

urlpatterns = [
    path('',include(router.urls))
]