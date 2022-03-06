from django.urls import path,include
from blog.views import index_blog,single_blog
app_name = "blog"
urlpatterns = [
    path('', index_blog, name="index"),
    path('single/<int:id>', single_blog, name="single"),

]