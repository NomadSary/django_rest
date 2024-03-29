from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet
from .models import TODO , Project 
from .serializers import ProjectModelSerializer , TODOModelSerializer



class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer

class TODOModelViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer