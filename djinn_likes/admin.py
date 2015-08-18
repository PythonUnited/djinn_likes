from django.contrib import admin
from models.likes import Like


class LikeAdmin(admin.ModelAdmin):

    list_display = ('content_object', 'user', 'created', )
    list_filter = ['created', ]
    search_fields = ['user', ]

    readonly_fields = ['created']

admin.site.register(Like, LikeAdmin)
