
from django.contrib import admin
from django.urls import path
from api.views import *
from rest_framework.authtoken import views as authviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/short-link",CreateLink.as_view(),name="shortLink"),
    path("api/v1/login",authviews.obtain_auth_token,name="signin"),
    path("api/v1/register",SignUp.as_view(),name="signup"),
    path("r/<str:random_string>",RedirectToLink.as_view(),name="redirectToLink"),
]
