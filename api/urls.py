from django.urls import path
from .views import school_get_all, create_school, school_find_byId, school_update, school_delete

urlpatterns = [
    path('school-create/', create_school, name='create_school'),
    path('school-get-all/', school_get_all, name='get_schools'),
    path('school-get-by/<int:id>', school_find_byId , name='get_schools_byId'),
    path('school-update-by/<int:id>', school_update , name='update_school'),
    path('school-delete-by/<int:id>', school_delete , name='delete_schools')
]
