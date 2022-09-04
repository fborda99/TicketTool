from django.urls import path
from AppIT_Team.views import *

urlpatterns = [
    path("homepage/",it_team_homepage,name="homepage_it"),
    path("list/",IT_TeamList.as_view(),name="IT_Team_List"),
    path("create/",IT_TeamCreate,name="IT_Team_Create"),
    path("detail/<pk>/",IT_TeamDetail.as_view(),name="IT_Team_Detail"),
    path("delete/<pk>/",IT_TeamDelete.as_view(),name="IT_Team_Delete"),
    path("update/<id_IT_Member>/",IT_TeamUpdate,name="IT_Team_Update"),

    #User
    path("user/profile/",it_profile_user, name = "it_profile_user"),
    path("user/edit/email/",it_edit_user_email, name = "it_edit_user_email"),
    path("user/edit/password/",it_edit_user_password, name = "it_edit_user_password"),
    path("user/edit/password/success/",it_user_password_confirm, name = "it_user_password_confirm"),
    path("user/edit/avatar/",it_add_avatar, name = "it_add_avatar"),
]