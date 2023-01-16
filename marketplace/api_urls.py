from rest_framework import viewsets, serializers, routers
from marketplace import models, views

class MapMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MapMark
        fields = '__all__'

class MapMarkViewSet(viewsets.ModelViewSet):
    serializer_class = MapMarkSerializer
    queryset = models.MapMark.objects.all()
    search_fields = ['label']

routes = routers.DefaultRouter()
routes.register(r'mapmark',MapMarkViewSet)
routes.register(r'persona',views.PersonaViewSet)
urls = [
    # 
] + routes.urls
