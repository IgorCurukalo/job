from django.contrib import admin
from app.projects.models import Project

class ProjectsAdmin(admin.ModelAdmin):

    list_display = (
        'id', 'user', 'title', 'image', 'description', 'demo_link', 'date_add', 'is_deleted'
    )
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_editable = ('is_deleted',)
    list_filter = ('title', 'is_deleted')
    fieldsets = (
        (None, {
            'fields': ('user', 'title', 'description', 'demo_link', 'image')
        }),
    )


admin.site.register(Project, ProjectsAdmin)