from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate
from django.views import View
from django.http import HttpResponseRedirect,HttpResponse,HttpResponseNotFound,Http404,HttpResponseServerError
from django.views.generic.base import TemplateView
from django.views.generic import ListView,DetailView
from django.views.generic.edit import FormView
from .forms import NameForm
from .models import PlayerData,Country
from apikeys import key_elena
import requests
# Create your views here.

#Class Based View

class PlayersListView(ListView):
	paginate_by=50
	template_name='PlayersList.html'
	context_object_name='playerslist'
	model=PlayerData


class PlayerDetailView(DetailView):

	model=PlayerData
	template_name="Player.html"
	context_object_name="playerdetails"

	def get_context_data(self,*args,**kwargs):

		context=super().get_context_data(*args,**kwargs)
		context['data']=PlayerData.objects.all()
		return context 

class PlayerView(View):
	
	def get(self,request,id):

		try:
			secret_key=key_elena.restrictedFunction()
			url = "https://football.elenasport.io/v2/players/"+id
			payload={}
			headers = {
	  					'Authorization': secret_key
						}
			response = requests.request("GET", url, headers=headers, data=payload)
			playerdata=response.json()
			context={
					'name':playerdata['data'][0]['name'],
					'nationalities':playerdata['data'][0]['nationalities'][0],
					'fullName':playerdata['data'][0]['fullName'],
					'pob':playerdata['data'][0]['pob'],
					'dob':playerdata['data'][0]['dob'],
					'height':playerdata['data'][0]['height'],
					'weight':playerdata['data'][0]['weight'],
					'foot':playerdata['data'][0]['foot'],
					'photoURL':playerdata['data'][0]['photoURL'],
					}
			return render(request,'Player.html',context)

		except ConnectionError:
			raise HttpResponse("Sorry!")


class PlayerPollView(FormView):

	form_class=NameForm
	template_name="Polls.html"
	success_url="/Players/thanks/"

	def form_valid(self,form):
		print(form.cleaned_data)
		return super().form_valid(form)


class ThanksView(TemplateView):

	template_name="thanks.html"


class PlayerNationalityView(TemplateView):
 	template_name='PlayersList.html'
 	paginate_by=3

 	def get_context_data(self,name,*args,**kwargs):
 		context=super().get_context_data(*args,**kwargs)
 		c=Country.objects.filter(country_name=name)
 		context['playerslist']=PlayerData.objects.filter(player_nationality_id=c[0].id)
 		return context

#@cache_page(60*1)

class Countries(View):


	def get(self,request,page_num):
		

		#try:
			secret_key=key_elena.restrictedFunction()
			url="https://football.elenasport.io/v2/countries?page="+page_num
			payload={}
			headers = {
					  	'Authorization': secret_key
					}
			response = requests.request("GET", url, headers=headers, data=payload)
			context=response.json()

			return render(request,'Countries.html',context)

		#except requests.exceptions.ConnectionError:

		#	raise HttpResponseServerError()








#@method_decorator(login_required,name='dispatch')
#class ProtectedView(TemplateView):
#	paginate_by=10
#	template_name='secret.html'






	