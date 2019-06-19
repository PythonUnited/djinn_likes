from django.contrib import admin
from .models.likes import Like


class LikeAdmin(admin.ModelAdmin):

    list_display = ('content_object', 'user', 'created', )
    list_filter = ['created', ]
    raw_id_fields = ['user']
    search_fields = ['user__username', ]

    readonly_fields = ['created']

admin.site.register(Like, LikeAdmin)
