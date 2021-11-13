from django.urls import path,re_path
from . import views


urlpatterns=[

	path('',views.Subview.as_view(),name='League'),
	path('matchdetails',views.TemplateView.as_view(template_name='stats.html'),name='matchdetails'),
	path('pointsTable/',views.TableView.as_view(),name='Ptstable'),
	path('apitable/<str:id>/',views.PointsTable,name='Ptstable1'),
	path('teams/<str:id>/',views.fetchTeams,name='teams'),
	re_path(r'^(?P<league>UCL|Laliga|PL|UEL|EuroCup)/',views.League.as_view(),name='moreSpecificLeagueView'),
]