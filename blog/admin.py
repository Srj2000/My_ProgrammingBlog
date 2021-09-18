from django.contrib import admin
from .models import Post,Comment,Contact

admin.site.register(Comment)
admin.site.register(Contact)
@admin.register(Post)
class cntactadmin(admin.ModelAdmin):
    list_display=["p_title", "p_author", "p_date"]
    search_fields=["p_title"]
    list_filter=["p_title", "p_author", "p_date"]


# Register your models here.
