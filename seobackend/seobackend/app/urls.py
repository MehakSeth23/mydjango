from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path("create_profile/",views.createUserProfile),
    path("update_profile/",views.updatedProfileLink),
    path("get_keyword_list/",views.getKeywordList),
    path("save_search_keyword_log/",views.SaveSearchKeywordLog),
    path('processkeyword_date/',views.processKeywordbyDate)
]