from unicodedata import name
from django.urls import path,include
from blog.views import index_blog,single_blog
app_name = "blog"
urlpatterns = [
    path('', index_blog, name="index"),
    path('single/<int:id>', single_blog, name="single"),
    path('category/<str:cat_name>',index_blog,name='category'),
    path('authors/<str:author_username>',index_blog,name='author'),

]