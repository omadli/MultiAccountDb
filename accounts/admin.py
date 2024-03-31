from django.contrib import admin
from django.utils.html import format_html
from rangefilter.filters import DateRangeFilterBuilder
from import_export.admin import ImportExportActionModelAdmin

from .models import Account, Group, Channel


@admin.register(Account)
class AccountAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'folder', 'phone', 'user_id', 'first_name', 'last_name', 'username', 'is_spam')
    list_display_links = ('id', 'user_id', 'first_name', 'last_name')
    
    search_fields = ('user_id', 'phone', 'first_name', 'last_name', 'username')
    list_filter = ('is_spam', 'folder')
    show_facets = admin.ShowFacets.ALLOW
    
    @admin.display(description="Telefon raqami", ordering='phone_number')
    def phone(self, obj: Account):
        return f"+{obj.phone_number}"
    
@admin.register(Group)
class GroupAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'chat_id', 'name', 'link', 'created_at', 'creator')
    list_display_links = ('id', 'chat_id', 'name')
    search_fields = ('chat_id', 'name')
    list_filter = (
        ('created_at', DateRangeFilterBuilder()),
        ('creator__is_spam', admin.BooleanFieldListFilter),
        ('creator', admin.RelatedOnlyFieldListFilter)
    )
    show_facets = admin.ShowFacets.ALLOW
    
    @admin.display(description="Invite link", ordering='invite_link')
    def link(self, obj: Group):
        return format_html("<a href='%s'> %s </a>" % (obj.invite_link, obj.invite_link.removeprefix("https://t.me/")))


@admin.register(Channel)
class ChannelAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'chat_id', 'name', 'link', 'created_at', 'creator')
    list_display_links = ('id', 'chat_id', 'name')
    search_fields = ('chat_id', 'name')
    list_filter = (
        ('created_at', DateRangeFilterBuilder()),
        ('creator__is_spam', admin.BooleanFieldListFilter),
        ('creator', admin.RelatedOnlyFieldListFilter)
    )
    show_facets = admin.ShowFacets.ALLOW
    
    @admin.display(description="Invite link", ordering='invite_link')
    def link(self, obj: Channel):
        return format_html("<a href='%s'> %s </a>" % (obj.invite_link, obj.invite_link.removeprefix("https://t.me/")))

