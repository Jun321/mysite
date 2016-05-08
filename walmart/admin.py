from django.contrib import admin

from .models import Comment
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
	fieldsets = [
	(None,       {'fields': ['title']}),
	('date',     {'fields': ['pub_time']}),
	('user',     {'fields': ['user']}),
	('text',     {'fields': ['text'], 'classes':['collapse']}),
	]
	list_display = ('title', 'pub_time', 'user')
		
admin.site.register(Comment, CommentAdmin)