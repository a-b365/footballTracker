from django.urls import path,re_path
from . import views


urlpatterns=[

	path('',views.LatestNewsView.as_view(template_name='news.html'),name='news-list'),
	# path('skysports/<str:path>/',views.scrawler,name='skysports'),	
	# path('espn/<str:path>/',views.ecrawler,name='espnfc'),
	path('<int:pk>/',views.NewsDetailView.as_view(),name='news-detail'),
	path('<slug:slug>',views.NewsRedirectView.as_view(),name='news-portal'),

]

