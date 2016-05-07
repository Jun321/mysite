from django.contrib import admin

from .models import User, Comment
# Register your models here.

class UserAdmin(admin.ModelAdmin):
	fieldsets = [
	(None,       {'fields': ['user_name']}),
	('password', {'fields': ['user_password'], 'classes': ['collapse']}),
	]
	list_display = ('user_name', )

class CommentAdmin(admin.ModelAdmin):
	fieldsets = [
	(None,       {'fields': ['title']}),
	('date',     {'fields': ['pub_time']}),
	('user',     {'fields': ['user']}),
	('text',     {'fields': ['text'], 'classes':['collapse']}),
	]
	list_display = ('title', 'pub_time', 'user')
		
admin.site.register(Comment, CommentAdmin)
admin.site.register(User, UserAdmin)