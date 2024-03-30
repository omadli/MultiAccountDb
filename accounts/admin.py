from django.contrib import admin
from .models import Account, Group, Channel

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'folder', 'phone', 'user_id', 'first_name', 'last_name', 'username', 'is_spam')
    list_display_links = ('id', 'user_id', 'first_name', 'last_name')
    
    search_fields = ('user_id', 'phone', 'first_name', 'last_name', 'username')
    list_filter = ('is_spam', 'folder')
    show_facets = admin.ShowFacets.ALWAYS
    
    @admin.display(description="Telefon raqami", ordering='phone_number')
    def phone(self, obj: Account):
        return f"+{obj.phone_number}"
    
admin.site.register(Group)
admin.site.register(Channel)
