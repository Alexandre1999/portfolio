from django.urls import path

from .views import (
    home_view,
    project_detail_view,
    projects_view,
    create_project_view,
    update_project_view,
    delete_project_view,
    send_email_view,
    update_bio_view,
    logout_view,
)

app_name = 'base'
urlpatterns = [
    path('', home_view, name="home"),
    path('project/<slug:slug>', project_detail_view, name="project_detail"),
    path('projects/', projects_view, name="projects"),
    path('update_bio/', update_bio_view, name="update_bio"),
    path('create_project/', create_project_view, name="create_project"),
    path('update_project/<slug:slug>', update_project_view, name="update_project"),
    path('delete_project/<slug:slug>', delete_project_view, name="delete_project"),
    path("logout", logout_view, name="logout"),
    path('send_mail/', send_email_view, name="send_email"),
]
