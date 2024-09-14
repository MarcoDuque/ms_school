from django.urls import include, path
# from ..views.school_view import school_get_all, create_school, school_find_byId, school_update, school_delete
from rest_framework.routers import DefaultRouter

from api.views.school_view import SchoolViewSet

router_post = DefaultRouter()
router_post.register(r'school', SchoolViewSet, basename='school')

urlpatterns = router_post.urls
