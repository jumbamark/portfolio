from django.urls import path
from . import views


# Creating a name space called base - if you have multiple apps for your projects
# app_name = 'base'


urlpatterns = [
    path("", views.homePage, name='home'),
    path("project/<str:pk>/", views.projectPage, name='projects'),

    path("add-project/", views.addProject, name='add-project'),
    path("edit-project/<str:pk>/", views.editProject, name='edit-project'),

    path("inbox/", views.inboxPage, name='inbox'),
    path("message/<str:pk>/", views.messagePage, name='messages'),
    path("add-skill/", views.addSkill, name="add-skill"),
    path("add-endorsements/", views.addEndorsement, name='add-endorsements'),
    path("donation/", views.donationPage, name='donation'),

    path("vote/", views.chartPage, name='chart')
]
