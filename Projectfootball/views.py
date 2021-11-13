from django.views.decorators.cache import cache_page
from django.views.generic.base import View,TemplateView
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .forms import SearchForm
from Players.models import PlayerData,ManagerData,Country
from assortedApps.models import Teams,Competition,Season
from News.models import News
#from News.views import Crawler
from django.contrib.postgres.search import SearchVector,SearchQuery,SearchRank
from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests
from bs4 import BeautifulSoup

def Search(request):

	if request.method=="POST":
		form=SearchForm(request.POST)

		if form.is_valid():
			q=form.cleaned_data['search_string']			
			query=SearchQuery(q)

			# For players
			#player_results=PlayerData.objects.filter(player_position__search=q)
			player_results=PlayerData.objects.annotate(search=SearchVector('player_name','player_position','player_nationality_id',),).filter(search=SearchQuery(q))				
			player_country=Country.objects.filter(playerdata__player_name__contains=q)
			
			#For News or Articles
			vector=SearchVector('headline',weight='B') + \
				SearchVector('content', weight='A')	

			news_results=News.objects.annotate(rank=SearchRank(vector,query,cover_density=True)).filter(rank__gte=0.1).order_by('-rank')
			#results=News.objects.annotate(search=SearchVector('headline','content',),).filter(search=SearchQuery(q))

			
			#For Managers 
			manager_results=ManagerData.objects.annotate(search=SearchVector('manager_name','manager_nationality',),).filter(search=query)
			manager_country=Country.objects.filter(managerdata__manager_name__contains=q)

			#For Teams	
			team_results=Teams.objects.annotate(search=SearchVector('team_name','stadium'),).filter(search=query)
			team_country=Country.objects.filter(teams__team_name__contains=q)

			first_team_results=PlayerData.objects.filter(teams__team_name__contains=q)
			team_managers=ManagerData.objects.filter(teams__team_name__contains=q)


			country_results=Country.objects.annotate(search=SearchVector('country_name','capital_city','continent',),).filter(search=query)		
			 
			competition_results=Competition.objects.annotate(search=SearchVector('competition_name','teams_in'),).filter(search=query)

			
			return render(request,'results.html',context={
															
															'form':form,
															'query':q,
															'player_results':player_results,
															'player_country':player_country,
															'news_results':news_results,
															'team_results':team_results,
															'country_results':country_results,
															'manager_results':manager_results,
															'manager_country':manager_country,
															'team_country':team_country,
															'first_team_results':first_team_results,
															'team_managers':team_managers,
															
											

															})

	else:
		form=SearchForm()

	return render(request,'results.html',{'form':form,
										})

"""class HomeView(TemplateView):

	template_name='homepage.html'
	news_objects=[]
	

	def get(self,request,*args,**kwargs):
		prettified_list=[]
		source=requests.get('https://www.espn.in/football/').text
		soup=BeautifulSoup(source,'lxml')


		for news in soup.find_all('section',class_='contentItem__content contentItem__content--fullWidth contentItem__content--enhanced contentItem__content--hero has-image contentItem__content--story'):

			try:
				headline = news.find('h1').text
				content = news.find('p').text
				link_src= news.find('a',class_='contentItem__padding watch-link')['href']
				path = link_src.split('/')[1]+'#'+link_src.split('/')[2]+'#'+link_src.split('/')[3]+'#'+link_src.split('/')[4]+'#'+link_src.split('/')[5]
				self.news_objects.append(Crawler(headline=headline,content=content,path=path))
				
			except(AttributeError):
				content = ' '
				continue

		for storycard in soup.find_all('section',class_='contentItem__content has-image contentItem__content--story StoryCardBody'):

			 	headline = storycard.find('h1',class_='contentItem__title contentItem__title--story').text
			 	timestamp = storycard.find('span',class_='contentMeta__timestamp').text
			 	author = storycard.find('span',class_='contentMeta__author').text
			 	content = storycard.find('p',class_='contentItem__subhead contentItem__subhead--story').text
			 	self.news_objects.append(Crawler(headline=headline,content=content,timestamp=timestamp,author=author))


		for news in soup.find_all('section',class_='contentItem__content contentItem__content--story has-image has-video contentItem__content--collection'):

			try:
				headline = news.find('h1').text
				content = news.find('p').text
				link_src = news.find('a',class_='contentItem__padding contentItem__padding--border')['href']
				path = link_src.split('/')[1]+'#'+link_src.split('/')[2]+'#'+link_src.split('/')[3]+'#'+link_src.split('/')[4]+'#'+link_src.split('/')[5]
				self.news_objects.append(Crawler(headline,content=content,path=path))
			except(AttributeError):
				content = ' '
				continue


		for news in soup.find_all('section',class_='contentItem__content contentItem__content--video contentItem__padding contentItem__padding--border has-video contentItem__content--enhanced contentItem__content--fullWidth has-image'):

			try:
				headline=news.find('h1').text
				self.news_objects.append(Crawler(headline))
			except(AttributeError):
				content = ' '
				continue


		for news in soup.find_all('section',class_='contentItem__content contentItem__content--story has-image has-video contentItem__content--collection contentItem__content--enhanced contentItem contentItem__content--fullWidth'):

			try:
			    headline = news.find('h1').text
			    content = news.find('p').text
			    link_src = news.find('a',class_='contentItem__padding contentItem__padding--border')['href']
			    path = link_src.split('/')[1]+'#'+link_src.split('/')[2]+'#'+link_src.split('/')[3]+'#'+link_src.split('/')[4]+'#'+link_src.split('/')[5]
			    self.news_objects.append(Crawler(headline,content=content,path=path))
			except(AttributeError):
				content = ' '
				continue

		snippets = soup.find('section',class_='headlineStack__listContainer')
		list_items = snippets.find_all('li')

		for item in list_items:
			link_src=item.find('a')['href']
			list_=link_src.split('/')

			if(len(list_)>3):
				path = link_src.split('/')[1]+'#'+link_src.split('/')[2]+'#'+link_src.split('/')[3]+'#'+link_src.split('/')[4]+'#'+link_src.split('/')[5]
			else:
				path = link_src.split('/')[1]+'#'+link_src.split('/')[2]

			prettified_list.append(Crawler(headline=item.text,path=path))

		return render(request , self.template_name , context={  'scraped_news':self.news_objects,
                                                                'prettified_list':prettified_list,
   
                                                            }) """




