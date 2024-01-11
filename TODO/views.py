from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet
from .models import TODO , Project 
from .serializers import ProjectModelSerializer , TODOModelSerializer
from rest_framework.pagination import LimitOffsetPagination
from .filters import Projectfilter
from rest_framework.response import Response
from rest_framework import status

class ProjectLimetPaginator(LimitOffsetPagination):
    default_limit = 10

class TODOLimetPaginator(LimitOffsetPagination):
    default_limit = 20


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    # filter_fields = ['project_name']
    # filter_class = Projectfilter
    pagination_class = ProjectLimetPaginator

    def get_queryset(self):
        qveryset = Project.objects.all()
        name = self.request.query_params.get('name',None)
        if name:
            qveryset = qveryset.filter(name_contains = name)
        return qveryset  

class TODOModelViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer
    filter_fields = ['project']
    pagination_class = TODOLimetPaginator

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.active = False        
            instance.save()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT) 