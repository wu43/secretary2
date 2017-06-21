from django.conf.urls import url
from django.contrib import admin
from web import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^diary/add/$', views.diary_add),
    url(r'^diary/(?P<month>\d+)/$', views.diary),
    url(r'^diary/word/(?P<month>\d+)/$', views.diary_word),
    url(r'^home/$', views.home),
    url(r'^money/(?P<month>\d+)$', views.money),
    url(r'^money/add/$', views.money_add),
    url(r'^money/excel/(?P<month>\d+)/$', views.money_excel),
    url(r'^$', views.user_login),
    url(r'^logout/$',auth_views.logout),
]
