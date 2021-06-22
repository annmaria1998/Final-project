from django.contrib import admin

# Register your models here.
#user_login, user_details, user_pic, user_posts, pic_pool, type_master, keywords_master, user_post_keyword_map

from .models import user_login, user_details, user_pic, user_posts, pic_pool, type_master, keywords_master, user_post_keyword_map

admin.site.register(user_login)
admin.site.register(user_details)
admin.site.register(user_pic)
admin.site.register(user_posts)
admin.site.register(pic_pool)
admin.site.register(type_master)
admin.site.register(keywords_master)
admin.site.register(user_post_keyword_map)


