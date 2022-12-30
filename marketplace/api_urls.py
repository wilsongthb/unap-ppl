from rest_framework import viewsets, serializers, routers
from marketplace import models

class MapMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MapMark
        fields = '__all__'

class MapMarkViewSet(viewsets.ModelViewSet):
    serializer_class = MapMarkSerializer
    queryset = models.MapMark.objects.all()

routes = routers.DefaultRouter()
routes.register(r'map-mark',MapMarkViewSet)
urls = [
    # 
] + routes.urls
