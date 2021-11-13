from django.contrib import admin,messages
from django.contrib.auth import authenticate
from .models import News
# Register your models here.

class NewsAdmin(admin.ModelAdmin):

	list_display=['headline','date_published','category','byline']
	#search by the following elements
	search_fields=['category','date_published']
	filter_fields=['date_published']
	editable_lists=['byline']

	#disable delete option
	# def has_delete_permission(self,request,obj=None):
	# 	if self.user is not None:
	# 		return True
	# 	else:
	# 		return False

	#disable add option
	# def has_add_permission(self,request,obj=None):
	# 	if self.user is not None:
	# 		return True
	# 	else:
	# 		return False

	# def has_view_permission(self,request,obj=None):
	# 	if self.user is not None:
	# 		return True
	# 	else:
	# 		return False

admin.site.register(News,NewsAdmin)


