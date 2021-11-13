from django.contrib import admin
from .models import Teams,Season,Competition,TrophyRoom,Standings

# Register your models here.

class TeamsAdmin(admin.ModelAdmin):
	list_display=['id','team_name','founded_on','stadium','official_website']
	list_filter=['team_name','founded_on','official_website']
	search_fields=['team_name']

class CompetitionAdmin(admin.ModelAdmin):
	list_display=['competition_name']
	search_fields=['competition_name']

class SeasonAdmin(admin.ModelAdmin):
	list_display=['season_start','season_end']
	search_fields=['season_status']

class TrophyRoomAdmin(admin.ModelAdmin):
	list_display=['trophy_name','trophy_won']
	search_fields=['trophy_name']

class StandingsAdmin(admin.ModelAdmin):
	list_display=['competition_id','team_id','match_played','points']
	

admin.site.register(Teams,TeamsAdmin)
admin.site.register(Competition,CompetitionAdmin)
admin.site.register(Season,SeasonAdmin)
admin.site.register(TrophyRoom,TrophyRoomAdmin)
admin.site.register(Standings,StandingsAdmin)

