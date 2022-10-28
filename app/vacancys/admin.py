from django.contrib import admin
from app.vacancys.models import Vakancys, Busyness


#админка вакансии
class VakancysAdmin(admin.ModelAdmin):

    list_display = (
        'id', 'profile', 'vakancy_name', 'salary', 'description', 'tasks', 'experience', 'busyness', 'count', 'date_add', 'is_deleted'
    )
    list_display_links = ('id', 'vakancy_name')
    search_fields = ('vakancy_name',)
    list_editable = ('is_deleted',)
    list_filter = ('vakancy_name', 'is_deleted')
    fieldsets = (
        (None, {
            'fields': ('profile', 'vakancy_name', 'salary', 'description', 'tasks', 'experience', 'busyness', 'skills')
        }),
    )


#админка занятость
class BusynessAdmin(admin.ModelAdmin):

    list_display = (
        'id', 'busyness_name', 'date_add', 'is_deleted'
    )
    list_display_links = ('id', 'busyness_name')
    search_fields = ('busyness_name',)
    list_editable = ('is_deleted',)
    list_filter = ('busyness_name', 'is_deleted')
    fieldsets = (
        (None, {
            'fields': ('busyness_name',)
        }),
    )


admin.site.register(Vakancys, VakancysAdmin)
admin.site.register(Busyness, BusynessAdmin)