
from django.urls import path,re_path
from .views import PlayerView,PlayersListView,ThanksView,PlayerPollView,PlayerDetailView,PlayerNationalityView
from django.views.decorators.cache import cache_page
from . import views


urlpatterns=[

    path('',PlayersListView.as_view(),name='players-main-page'),   	
    path('polls/',PlayerPollView.as_view(),name='players-by-vote'),
    path('thanks/',ThanksView.as_view()),
    path('country/<str:name>',views.PlayerNationalityView.as_view(),name='player-by-nationality'),
    path('countries/<str:page_num>/',views.Countries.as_view(),name='Countries'),
   	path('<slug:pk>/',views.PlayerDetailView.as_view(),name='players-by-name'),
   	path('<str:id>/',PlayerView.as_view(),name='players-by-id'),

]






