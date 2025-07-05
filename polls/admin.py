from django.contrib import admin

from .models import Question, Choice

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display  = ('id', 'question_text', 'pub_date')  # columns in the list view
    list_filter   = ('pub_date',)                        # sidebar filters (optional)
    search_fields = ('question_text',)

admin.site.register(Question)
admin.site.register(Choice)