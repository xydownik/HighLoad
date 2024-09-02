from django.contrib import admin


from .models import Post, Comment


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')  # Customize the list view
    search_fields = ('title',)


admin.site.register(Comment)