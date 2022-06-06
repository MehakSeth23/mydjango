from django.contrib import admin
from .models import *


class SearchKeywordLogAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'keyword_id', 'search_date')
admin.site.register(SearchKeywordLog,SearchKeywordLogAdmin)

admin.site.register(UserProfile)
admin.site.register(SearchURLKeyword)
admin.site.register(UserAssignKeyword)

