from django.db import models

#Create your models here.

class Country(models.Model):

	country_name=models.CharField(max_length=20,blank=False,verbose_name='COUNTRY')
	capital_city=models.CharField(max_length=20,blank=False,verbose_name='CAPITAL')
	continent=models.CharField(choices=(
										('EUROPE','EUROPE'),
			 							('SOUTH AMERICA','SOUTH AMERICA'),
										('NORTH AMERICA','NORTH AMERICA'),
										('AUSTRALIA','AUSTRALIA & OCENIA'),
										('ASIA','ASIA'),
										('AFRICA','AFRICA'), 
									   ),max_length=20,blank=False,verbose_name='CONTINENT')
	
	def __str__(self):
		return self.country_name

	class Meta:
		db_table='country_info'
		verbose_name='Country Information'

class PlayerData(models.Model):
	position_choices=(
			('GK','Goalkeeper'),
			(
				'Defender',
						(
						('CD','Central Defender'),
						('RCD','Right Central Defender'),	
						('LCD','Left Central Defender'),
						('RF','Right Full Back'),
						('LF','Left Full Back')
						)
			),

			(	
				'MidFielder',
						(
						('DM','Defensive MidFielder'),
						('B2B','Box To Box MidFielder'),	
						('CM','Central MidFielder'),
						('RCB','Right Central MidFielder'),
						('LM','Left Offensive MidFielder'),
						('OM','Offensive MidFielder'),
						('RM','Right Offensive MidFielder'),
						('PM','PlayerMaker'),
						)
			),

			(
				'Forward',
						(
						('ST','Striker'),
						('RW','Right Winger'),	
						('LW','Left Winger'),
						('CF','Centre Forward'),
						)
			)

			
			
			)

	player_name=models.CharField(verbose_name="FIRST NAME",max_length=30,blank=False)
	full_name=models.CharField(verbose_name="FULL NAME",max_length=30,blank=True)
	age=models.IntegerField(verbose_name="AGE",default=0,blank=False)
	player_height=models.DecimalField(verbose_name="HEIGHT(m)",default=0,blank=True,decimal_places=2,max_digits=4)
	player_weight=models.DecimalField(verbose_name="WEIGHT(kg)",default=0,blank=True,decimal_places=2,max_digits=4)
	player_nationality=models.ForeignKey(Country,on_delete=models.PROTECT,verbose_name="NATIONALITY")
	player_position=models.CharField(choices=position_choices,verbose_name="FIELD POSITION",max_length=15,blank=False,default="None")
	shirt_num=models.IntegerField(verbose_name="SHIRT NUMBER",blank=True,null=True)


	def __str__(self):
		return self.player_name

	class Meta:
		db_table='playerdata'
		verbose_name='Player'

class ManagerData(models.Model):
	manager_name=models.CharField(verbose_name="FULL NAME",max_length=30,blank=True)
	date_of_birth=models.DateField(verbose_name="DATE OF BIRTH")
	manager_nationality=models.ForeignKey(Country,on_delete=models.CASCADE,verbose_name="NATIONALITY")


	def __str__(self):
		return self.manager_name

	class Meta:
		db_table='managerdata'
		verbose_name='Manager'





