from django.urls import path
from . import views



urlpatterns = [
    path('',views.homePage,name='home'),
    path("contact/",views.contact,name='contact'),
    path('project/<str:pk>/',views.projectPage,name="project"),
    path('add-project/',views.addProject,name="add-project"),
    path('edit-project/<str:pk>/',views.editProject,name="edit-project"),
    path("chart/",views.chartPage,name='chart'),
    path('add-skill/',views.addSkill,name="add-skill"),


]