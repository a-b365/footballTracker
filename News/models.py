from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class News(models.Model):

	user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="USER")
	headline=models.CharField(verbose_name="HEADLINE",max_length=100,blank=False,null=True)
	byline=models.CharField(verbose_name="WRITER",max_length=20)
	content=models.TextField(verbose_name="CONTENT",blank=False,max_length=10000,null=True)
	date_published=models.DateField(verbose_name="DATE PUBLISHED",default=timezone.now,null=True)
	source=models.CharField(verbose_name="SOURCE",max_length=500,null=True)
	category=models.CharField(choices=
									(
									('TN','Transfer News'),
									(
									'Leagues And Tournaments',
										(
										('EURO','EURO'),
										('UCL','UEFA CHAMPIONS LEAGUE'),
										('ESP','SPAIN'),
										('ENG','ENGLAND'),
										('FRA','FRANCE'),
										('ITA','ITALY'),	
										('GER','GERMANY'),			
										)
									),

									('MD','Matchday Analysis'),
									),max_length=10,blank=False,verbose_name="CATEGORY")
	


	class Meta:
		db_table='news_info'
		verbose_name='New'









