from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views.school_view import SchoolViewSet
from api.views.subsidiary_view import SubsidiaryViewSet

router_post = DefaultRouter()
router_post.register(r'school', SchoolViewSet, basename='school')
router_post.register(r'subsidiary', SubsidiaryViewSet, basename='subsidiary')

urlpatterns = router_post.urls
