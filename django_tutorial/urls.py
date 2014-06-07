from django.conf.urls import patterns, include, url
from rest_framework import routers
from quickstart import views
from django.contrib import admin
admin.autodiscover()

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('groups', views.GroupViewSet)

urlpatterns = patterns('',
    url('^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls))
)
