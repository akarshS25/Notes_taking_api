from rest_framework import viewsets
from api.models import Note
from api.serializers import NoteSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework.views import APIView
from rest_framework import filters

# Create your views here.
class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    

   

