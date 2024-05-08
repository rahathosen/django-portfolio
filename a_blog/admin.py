from django.contrib import admin
from .models import Post,Category

admin.site.register(Post)
admin.site.register(Category)

# @admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'created_at', 'image_thumb')  # Add 'image_thumb'
    readonly_fields = ('image_thumb',)  # Add 'image_thumb'

    def image_thumb(self, obj):
        if obj.image:
            return mark_safe('<img src="{}" width="100px" height="80px" />'.format(obj.image.url))
        else:
            return 'No image'

    image_thumb.short_description = 'Image'