from django.urls import re_path as url
from codestar import views

urlpatterns = [
	url(r'^home/$',views.greetings),
    url(r'^home/run$',views.runcode),
    url(r'', views.homepage )
]
