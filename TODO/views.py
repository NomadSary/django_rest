from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet
from .models import TODO , Project 
from .serializers import ProjectModelSerializer , TODOModelSerializer
from rest_framework.pagination import LimitOffsetPagination
from .filters import Projectfilter

class ProjectLimetPaginator(LimitOffsetPagination):
    default_limit = 10

class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    # filter_fields = ['project_name']
    filter_class=Projectfilter
    pagination_class = ProjectLimetPaginator

class TODOModelViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer