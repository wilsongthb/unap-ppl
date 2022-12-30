from rest_framework.routers import DefaultRouter
from rest_framework import serializers, viewsets, response
from rest_framework.views import APIView
from basics import models
from django.urls import include, path
from rest_framework import permissions

# from rest_framework.settings import api_settings

# print(api_settings.DEFAULT_AUTHENTICATION_CLASSES)

class FileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.File
        fields = ['id', 'name', 'file', 'size']

class FileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.File.objects.all()
    serializer_class = FileSerializer

def upload_file(req):
    return response.Response('No loko')

#  class FileAbsSerializer(ModelSerializer):
#      file = FileField(blank=True, default='')


class UploadFileView(APIView):
    """
    Ruta para subir archivos, solo post
    * Requiere estar autenticado
    form-data
        - file
    """
    permission_classes = [permissions.IsAuthenticated]
    def get(self, req, format=None):
        return response.Response('only post request is accepted',status=500)
    def post(self, req):
        if 'file' in req.FILES.dict():
            file =  req.FILES['file']
            print('File uploaded: ' + str(file) + ' ' + str(type(file)))
            mimetypeObj, created = models.Mimetype.objects.get_or_create(
                    mimetype=file.content_type
                )
            fileInstance = models.File.objects.create(
                    file=file,
                    name=file.name,
                    size=file.size,
                    mimetype=mimetypeObj
                    )
            return response.Response(FileSerializer(fileInstance).data,status=201)
        else:
            return response.Response({"message":"Error, file not included"}, status=500)

router = DefaultRouter()
router.register(r'file', FileViewSet)

urls = [
    path('upload/', UploadFileView.as_view())
] + router.urls
