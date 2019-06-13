from django.urls import path

from . import views
app_name = "rbs_site"
urlpatterns = [
  path( '', views.HomepageView.as_view(), name = 'home')
]