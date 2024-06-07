from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('people/', views.people, name='people'),
    path('people/<int:person_id>/', views.person_details, name='person_details'),
    path('people/<int:person_id>/job_list', views.job_list, name='job_list'),
]
