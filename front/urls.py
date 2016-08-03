from django.conf.urls import url, include
from django.contrib.auth.models import User
from front.models import Publishers, Authors, Books
from rest_framework import routers, serializers, viewsets


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PublishersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publishers
        fields = ('name')

class PublishersView(viewsets.ModelViewSet):
    #queryset = Publishers.object.all()
    serializer_class = PublishersSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
#router.register(r'books', BookView)
router.register(r'publishers', PublishersView)
#router.register(r'authors', AuthorView)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
