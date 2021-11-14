import requests
from apikeys import key_elena
from pathlib import Path
from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.views import View
from django.views.decorators.cache import cache_page
from django.views.generic.base import TemplateView
from django.views.generic import ListView,DetailView
from django.http import HttpResponseServerError
from Players.models import Country
from .models import Standings,Teams,Competition
from bs4 import BeautifulSoup
import os

class Snippet(object):

	def __init__(self,headline,path):
		self.headline=headline
		self.path=path


# Create your views here. 

class Subview(ListView):

	model=Country
	template_name='Leagues.html'

	def get_context_data(self,*args,**kwargs):

		context=super().get_context_data(*args,**kwargs)

		secret_key=key_elena.restrictedFunction()
			
		url = "https://football.elenasport.io/v2/upcoming/?expand=league.current_season.inplay&page=1"

		payload={}

		headers = {
		 		  		'Authorization': secret_key
		 			}
		response = requests.request("GET", url, headers=headers, data=payload)

		context['fixtures']=response.json()
		return context

	def get_queryset(self):
		
		return Country.objects.all()

	


	
#@cache_page(60*2)

class League(View):

	def get(self,request,league):

		if league=="PL":

			params_ = (	
		   			("season_id","352"),
		   			("date_from","2020-09-11"),
				);

			params__ = (	
		   			("season_id","352"),
				);

			response_a = requests.get('https://app.sportdataapi.com/api/v1/soccer/matches', headers={ "apikey" : os.environ['sdapikeyI'] }, 
							params=params_);

			response_b = requests.get('https://app.sportdataapi.com/api/v1/soccer/standings', headers={ "apikey" : os.environ['sdapikeyI'] }, 
							params=params__);

		if league=="Laliga":
			
			params_ = (	
		   			("season_id","1511"),
		   			("date_from","2020-09-19"),
				);

			params__ = (	
		   			("season_id","1511"),
				);

			response_a = requests.get('https://app.sportdataapi.com/api/v1/soccer/matches', headers={ "apikey" : os.environ['sdapikeyI'] }, 
							params=params_);

			response_b = requests.get('https://app.sportdataapi.com/api/v1/soccer/standings', headers={ "apikey" : os.environ['sdapikeyI'] }, 
							params=params__ );



		elif league=="UEL":
			
			params_ = (	
		   			("season_id","434"),
   					("date_from","2020-08-20"),
				);

			params__ = (	
		   			("season_id","434"),
   					
				);

			response_a = requests.get('https://app.sportdataapi.com/api/v1/soccer/matches', headers={ "apikey" : os.environ['sdapikeyII'] } ,
							params=params_);


			response_b = requests.get('https://app.sportdataapi.com/api/v1/soccer/standings', headers={ "apikey" : os.environ['sdapikeyII'] },
							params=params__ );

			

			
		elif league=="UCL":

			params_ = (	
		   			("season_id","1243"),
   					("date_from","2020-08-08"),
				);

			params__ = (	
		   			("season_id","1243"),
   					
				);

			response_a = requests.get('https://app.sportdataapi.com/api/v1/soccer/matches', headers={ "apikey" : os.environ['sdapikeyII'] }, 
							params=params_);

			response_b = requests.get('https://app.sportdataapi.com/api/v1/soccer/standings', headers={ "apikey" : os.environ['sdapikeyII'] },
							params=params__ );


		context={

				'matches':response_a.json(),
				'table':response_b.json(),
			}		

		return render(request,'clf.html',context)



#@cache_page(60*15)
def PointsTable(request,id):

	try:
		secret_key=key_elena.restrictedFunction()
		url = "https://football.elenasport.io/v2/stages/"+id+"/standing"
		payload={}
		headers = {
	  					'Authorization': secret_key
					}
		response = requests.request("GET", url, headers=headers, data=payload)
		context=response.json()
		
		return render(request,'PointsTable.html',context)

	except(requests.exceptions.ConnectionError):

		raise HttpResponseServerError()


class TableView(TemplateView):

	template_name='PointsTable.html'
	snippets=[]

	def get_context_data(self,**kwargs):
		self.snippets.clear()
		context=super().get_context_data(**kwargs)

		""" source = requests.get('https://www.skysports.com/football').text
		soup = BeautifulSoup(source,'lxml')
		block = soup.find('div',class_='news-list-secondary block news-list-secondary--2cols is-hidden--bp20 is-hidden--bp30')

		for item in block.find_all('li',class_='news-list-secondary__item'):
			snippet = item.text
			link_src= item.find('a',class_='news-list-secondary__link')['href']
			path=link_src.replace('/','#')
			self.snippets.append(Snippet(snippet,path)) """
						
		context['table']=Standings.objects.filter(competition_id=2).order_by('-points','-lost')
		context['snippets']=self.snippets
		return context

	

def fetchTeams(request,id):

	headers = { 
  		"apikey": os.environ[sdapikeyI]}

	params = (
   			("country_id",id),
		);

	response = requests.get('https://app.sportdataapi.com/api/v1/soccer/teams', headers=headers, params=params);
	
	context=response.json()

	return render(request,'teams.html',context)



