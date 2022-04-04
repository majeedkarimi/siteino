from django.urls import path
from accounts.views import login_view,signup_view
app_name = "account"
urlpatterns = [
    # login
    path('login/', login_view, name="login"),
    # logout
    # path('logout/',logout,name='logout'),
    # signup
    path('signup/',signup_view,name='signup'),
]