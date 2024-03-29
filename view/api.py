from .models import Video
from rest_framework import serializers, viewsets

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['name', 'videofile']

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer