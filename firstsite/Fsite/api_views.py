from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from .permissions import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrReadOnly]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAdminOrReadOnly]

class NewsSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializers
    permission_classes = [IsAdminOrReadOnly]

    @action(detail=False, methods=['GET']) # подумать нужна ли нам такая хуйня
    def ajax_query(self, request):
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        if is_ajax:
            paginated_news = Paginator( News.objects.all().order_by('-time_update'), 8)
            query = list(paginated_news.page(request.GET.get('number', 1)).object_list.values())
            serializer = NewsSerializers(query)
            return Response(serializer)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)