from django.urls import path
from accounts.views import login_view,signup_view,logout_view
app_name = "accounts"
urlpatterns = [
    # login
    path('login/', login_view, name="login"),
    # logout
    path('logout/',logout_view,name='logout'),
    # signup
    path('signup/',signup_view,name='signup'),
]