from django.urls import path
from .views import school_get_all, create_school

urlpatterns = [
    path('school-get-all/', school_get_all, name='get_schools'),
    path('school-create/', create_school, name='create_school')
]
