from django.contrib import admin
from .models import Post, PostAttachment
from django.utils.translation import gettext_lazy as _
# Register your models here.

# admin.site.register(Post)
admin.site.register(PostAttachment)

@admin.register(Post)
class CustomPostAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Автор'), {'fields': ('author',)}),
        (_('Основаная информация поста (ru)'), {'fields': ('title_ru', 'content_ru')}),
        (_('Основаная информация поста (en)'), {'fields': ('title_en', 'content_en')}),
        (_('Дополнительная информация поста'), {'fields': ('time_stamp', 'edited')}),    
    )

    add_fieldsets = (
        (_('Автор'), {'fields': ('author',)}),
        (_('Основаная информация поста (ru)'), {'fields': ('title_ru', 'content_ru')}),
        (_('Основаная информация поста (en)'), {'fields': ('title_en', 'content_en')}),
    )

    list_display = ('title', 'time_stamp', 'edited')
    search_fields = ('title', 'content')
    ordering = ('time_stamp', 'title')
    readonly_fields = ('time_stamp',)

    def get_fieldsets(self, request, obj = None):
        if obj:
            return self.fieldsets
        return self.add_fieldsets
    
