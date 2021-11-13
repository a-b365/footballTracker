from django.db import models
from Players.models import PlayerData,ManagerData,Country

#Create your models here.
		
class Teams(models.Model):

	team_name=models.CharField(max_length=50,blank=False,verbose_name='TEAM REPRESENTATION')
	first_team=models.ManyToManyField(PlayerData,verbose_name='FIRST TEAM')
	team_manager=models.ManyToManyField(ManagerData,verbose_name='MANAGER/COACH')
	country=models.ForeignKey(Country,on_delete=models.CASCADE,verbose_name='COUNTRY',default=0)
	stadium=models.CharField(max_length=20,verbose_name='HOME VENUE',blank=True)
	founded_on=models.DateField(verbose_name='FOUNDING DATE',blank=True,null=True)
	official_website=models.URLField(verbose_name='OFFICIAL WEBSITE',blank=True)

	def __str__(self):
		return self.team_name

	class Meta:
		db_table='teams'
		verbose_name='Team'


class TrophyRoom(models.Model):

	trophy_name=models.CharField(max_length=40,verbose_name='TROPHY',blank=False,null=True)
	trophy_won=models.IntegerField(verbose_name='TROPHIES COUNT',default=0)
	teams_in=models.ManyToManyField(Teams,verbose_name='WINNERS')

	def __str__(self):
		return self.trophy_name

	class Meta:
		db_table='trophies_room'
		verbose_name='Trophies and Cup'


class Competition(models.Model):

	COMPETITION_CHOICES=(
			 ('Laliga','LALIGA'),
			 ('PL','ENGLISH PREMIER LEAGUE'),
			 ('Serie A','SERIE A'),
			 ('Bundesliga','BUNDESLIGA'),
			 ('Ligue1','LIGUE 1'),
			 ('UCL','UEFA CHAMPIONS LEAGUE'),
			 ('Copa del Rey','COPA DEL REY'),
			 ('Uefa Europa League','UEFA EUROPA LEAGUE'),
			 ('World Cup','FIFA WORLD CUP'),
			 ('Euro Cup','EURO'),
			 ('Club World Cup','FIFA CLUB WORLD CUP'),
			 ('Segunda División B','Segunda División B')
			 )

	competition_name=models.CharField(choices=COMPETITION_CHOICES,max_length=20,verbose_name='LEAGUE')
	teams_in=models.ManyToManyField(Teams,verbose_name='TEAMS INVOLVED',through='Standings')
	
	
	def __str__(self):
		return self.competition_name

	class Meta:
		db_table='competition'
		verbose_name='Competition'



class Standings(models.Model):

	team=models.ForeignKey(Teams,on_delete=models.CASCADE,verbose_name='TEAM REPRESENTATION')
	competition=models.ForeignKey(Competition,on_delete=models.CASCADE,verbose_name='LEAGUE')
	match_played=models.IntegerField(verbose_name='MATCHES PLAYED',default=0)
	wins=models.IntegerField(verbose_name='WINS',default=0)
	draw=models.IntegerField(verbose_name='DRAW',default=0)
	lost=models.IntegerField(verbose_name='LOST',default=0)
	goals_against=models.IntegerField(verbose_name='GOALS_AGAINST',default=0)
	goals_for=models.IntegerField(verbose_name='GOALS FOR',default=0)
	goal_difference=models.IntegerField(verbose_name='GOAL DIFFERENCE',default=0)
	points=models.IntegerField(verbose_name='POINTS',default=0)

	class Meta:
		db_table='standings'
		verbose_name="Standing"






class Season(models.Model):
	
	competition=models.ManyToManyField(Competition,verbose_name="COMPETITION")
	season_start=models.DateField(verbose_name="START DATE")
	season_end=models.DateField(verbose_name="END DATE")
	season_status=models.BooleanField(choices=(
												(True,'RUNNING'),
												(False,'FINISHED'),
												),verbose_name="Current Status",default=False)
	
	
	class Meta:
		db_table='season'
		verbose_name='Season'






