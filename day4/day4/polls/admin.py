from django.contrib import admin
from . import models

# Register your models here.

class ChoiceInline(admin.TabularInline):
	model = models.Choice
	extra = 0

class QuestionAdmin(admin.ModelAdmin):
	# 보여줄 화면
	list_display = ('question_text', 'publish_date', 'was_published_recently')
	#필터 선택
	list_filter = ['publish_date']
	fieldsets = [
	(None, {'fields': ['question_text']}),
	('Date information', {'fields': ['publish_date']}),
	]
	# question에 choice항목 보이기
	inlines = [ChoiceInline]



class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'votes', 'question')
    list_filter = ['votes', 'question']
    
admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.Choice, ChoiceAdmin)