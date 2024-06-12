from rest_framework import viewsets
from . import models
from . import serializers
# Create your views here.

class VideoApiViewSet(viewsets.ModelViewSet):
    queryset = models.Video.objects.all()
    serializer_class = serializers.VideoSerializer
