from rest_framework import viewsets, serializers, routers
from marketplace import models, views





routes = routers.DefaultRouter()
routes.register(r'mapmark',views.MapMarkViewSet)
routes.register(r'persona',views.PersonaViewSet)
routes.register(r'unidadmedida',views.UnidadMedidaViewSet)
routes.register(r'producto',views.ProductoViewSet)
routes.register(r'publicacion',views.PublicacionViewSet)
routes.register(r'lugar',views.LugarViewSet)
urls = [
    # 
] + routes.urls
