from django.urls import path,register_converter
from footballers.views import *
from footballers import converters


register_converter(converters.FourDigitYearConverter,"year4")

urlpatterns = [
    path('',index,name='home'),
    path('about/',about,name='about'),
    path('addpage/',addpage,name="add_page"),
    path('contact/',contact,name="contact"),
    path('login/',login,name='login'),
    path('post/<slug:post_slug>/',show_post,name='post'),
    path('category/<slug:cat_slug>/',show_category,name='category'),
    path('tag/<slug:tag_slug>/',show_tag_postlist,name='tag')
    
    
]


