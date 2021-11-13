from django.contrib import admin
from .models import PlayerData,ManagerData,Country
#Register your models here.

class PlayersAdmin(admin.ModelAdmin):

	list_display=['player_name','age','player_nationality','player_position']
	search_fields=['player_name','player_nationality']
	filter_fields=['player_nationality']

class ManagersAdmin(admin.ModelAdmin):

	list_display=['manager_name','date_of_birth','manager_nationality']
	search_fields=['manager_name','manager_nationality']
	filter_fields=['manager_nationality']

class CountryAdmin(admin.ModelAdmin):

	list_display=['country_name','capital_city','continent']
	search_fields=['country_name','continent']
	filter_fields=['capital_city']


admin.site.register(PlayerData,PlayersAdmin)
admin.site.register(ManagerData,ManagersAdmin)
admin.site.register(Country,CountryAdmin)

