from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.views.decorators.http import require_http_methods
from django.contrib.postgres.search import SearchVector,SearchQuery,SearchRank
from django.views.decorators.cache import cache_page
from django.views.generic.base import View,RedirectView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from .models import News 
from .forms import DateForm
from datetime import date
import requests,uuid,json
from bs4 import BeautifulSoup

class Crawler:
	'''A News Class'''
	def __init__(self,headline,caption='',path='',content='',inner_headline='',timestamp='',author='',category=''):
		self.headline=headline
		self.path=path
		self.content=content
		self.inner_headline=inner_headline
		self.timestamp=timestamp
		self.author=author
		self.caption=caption
		self.category=category


class NewsRedirectView(RedirectView):
	url='/News'


class NewsDetailView(DetailView):
	model=News


class LatestNewsView(ListView,FormView):

	#snippets=[]
	model=News
	paginate_by=10
	success_url='/News'
	form_class=DateForm

	
	def get_context_data(self,**kwargs):

		context=super().get_context_data(**kwargs)
		""" source = requests.get('https://www.skysports.com/football/news').text
		soup = BeautifulSoup(source,'lxml')

		for snippet in soup.find_all('div',class_='news-list__body'):
			
			headline = snippet.find('h4',class_='news-list__headline').text
			category =snippet.find('a', class_='label__tag').text
			timestamp =snippet.find('span', class_='label__timestamp').text
			content = snippet.find('p',class_='news-list__snippet').text
			link_src= snippet.find('a',class_='news-list__headline-link')['href']
			path=link_src.replace('/','#')

			self.snippets.append(Crawler(headline=headline,content=content,category=category,timestamp=timestamp,path=path))

		context['scraped_news']=self.snippets """
		context['recent_news']=News.objects.all()
		
		return context

	def post(self,request):

		form=DateForm(request.POST)

		if form.is_valid():
			date_input=form.cleaned_data['date_published']
			filtered_news=News.objects.filter(date_published__exact=date_input)
			context={'filtered_news':filtered_news}
			return render(request,'newsevent.html',context)

""" #@cache_page(60*15)
def scrawler(request,path):

	news_object = []
	content = []
	news_object.clear()
	content.clear()

	path = path.replace('#','/')
	source = requests.get(path).text		
	soup = BeautifulSoup(source,'lxml')

	#Scraping Useful Data
	header=soup.find('h1',class_='sdc-site-component-header--h1 sdc-article-header__title').text
	subtitle=soup.find('p',class_='sdc-site-component-header--h2 sdc-article-header__sub-title').text
		
	try:
		byline=soup.find('p',class_='sdc-article-author__byline')
	
	except(AttributeError):
		byline = 'None'

	datetime=soup.find('p',class_='sdc-article-date__date-time').text	
	body_div=soup.find('div',class_='sdc-article-body sdc-article-body--lead')
	for element in body_div.find_all('p'):
		content.append(element.text)

	news_object.append(Crawler(headline=header,content=content,caption=subtitle,timestamp=datetime,author=byline))

	context={
			'scraped_news':news_object
			}

	return render(request , 'News/newspage.html' , context)


#@cache_page(60*2)
def ecrawler(request,path):

	news_object = []
	content = []
	news_object.clear()
	content.clear()

	path = path.replace('#','/')
	url = 'https://www.espn.in/'+path
	source = requests.get(url).text
	soup = BeautifulSoup(source,'lxml')

	#Scraping Useful Data
	article = soup.find('section',class_='col-b')
	headline = article.find('h1').text
	article_meta = soup.find('div',class_='article-meta')
	timestamp = article_meta.find('span',class_='timestamp').text
	author = article_meta.find('div',class_='author').text

	for item in article.find_all('p'):
		content.append(item.text)

	news_object.append(Crawler(headline=headline,content=content,timestamp=timestamp,author=author))

	context={
			'scraped_news':news_object
			}

	return render(request , 'News/newspage.html' , context) """