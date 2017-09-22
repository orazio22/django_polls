from django.contrib import admin

from .models import Choice, Question, IndirizzoIP

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class IpInline(admin.TabularInline):
    model = IndirizzoIP

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
