from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name="home"),
    path('Home/', views.home, name="home"),
    path('About/', views.About, name="About"),
    path('Departments/', views.Department, name="Department"),
    path('Project/', views.my_project, name="my_project")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)