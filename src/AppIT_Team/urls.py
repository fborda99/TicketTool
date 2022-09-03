from django.urls import path
from AppIT_Team.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("homepage/",it_team_homepage,name="homepage_it"),
    path("list/",IT_TeamList.as_view(),name="IT_Team_List"),
    path("create/",IT_TeamCreate,name="IT_Team_Create"),
    path("detail/<pk>",IT_TeamDetail.as_view(),name="IT_Team_Detail"),
    path("delete/<pk>",IT_TeamDelete.as_view(),name="IT_Team_Delete"),
    path("update/<id_IT_Member>",IT_TeamUpdate,name="IT_Team_Update"),
    path("logout/",LogoutView.as_view(template_name="AppIT_Team/logout.html"),name="logout"),
]