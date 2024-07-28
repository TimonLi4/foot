from typing import Any
from django.contrib import admin,messages
from django.db.models.query import QuerySet
from .models import Footballers,Category,Wife


# Register your models here.

class MarriedFilter(admin.SimpleListFilter):
    title = "Статус"
    parameter_name='status'

    def lookups(self,request, model_admin):
        return [
            ('married','Женат'),
            ('single','Не женат')

        ]

    def queryset(self, request, queryset):

        if self.value() =='married':
            return queryset.filter(wife__isnull=False)
        
        if self.value() =='single':
            return queryset.filter(wife__isnull=True)
    

@admin.register(Footballers)
class FootballersAdmin(admin.ModelAdmin):
    #fields=['title','content','slug']
    prepopulated_fields={"slug":('title',)}
    list_display=('title','time_create','is_published',"cat",'brief_info')
    list_display_links=('title',)
    ordering=['time_create','title']
    list_editable=('is_published',)
    list_per_page = 5
    actions=['set_published','set_draft']
    search_fields=['title','cat__name']
    list_filter=[MarriedFilter,'cat__name','is_published']
    #readonly_fields=['slug']


    @admin.display(description='Краткое описание',ordering='content')
    def brief_info(self,football:Footballers):
        return f'Описание {len(football.content)} символов'

    @admin.action(description='Опубликовать выбранные записи')
    def set_published(self,request,queryset):
        count=queryset.update(is_published = Footballers.Status.PUBLISHED)
        self.message_user(request,f'Изменено {count} записей')

    @admin.action(description='Снять с публикации выбранные записи')
    def set_draft(self,request,queryset):
        count=queryset.update(is_published = Footballers.Status.DRAFT)
        self.message_user(request,f'Изменено {count} записей',messages.WARNING)

#admin.site.register(Footballers,FootballersAdmin)

@admin.register(Category)
class FootballersAdmin(admin.ModelAdmin):
    list_display=("id",'name',)
    list_display_links=("id",'name',)
    ordering=['id','name'] 
    
"""@admin.register(Wife)
class WifeAdmin(admin.ModelAdmin):
    list_display=("id",'name',)
    list_display_links=("id",'name',)
    ordering=['id','name'] """