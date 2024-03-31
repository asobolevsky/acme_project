from django.contrib import admin
from .models import Birthday


admin.site.empty_value_display = 'Не задано'


@admin.register(Birthday)
class BirthdayAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'birthday',
    )
    list_display_links = ('first_name',)
    search_fields = ('first_name', 'last_name')
