from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'ask_buevich.views.index_view', name='index'),
    url(r'^tag/john/', 'ask_buevich.views.tag_john_view', name='tag_john'),
    url(r'^question(?P<article_id>\d+)/', 'ask_buevich.views.answer_view', name='answer'),
    url(r'^login', 'ask_buevich.views.login_view', name='login'),
    url(r'^singup', 'ask_buevich.views.singup_view', name='singup'),
    url(r'^hot/', 'ask_buevich.views.index_view', name='hot'),
    url(r'^ask', 'ask_buevich.views.ask_view', name='ask'),
    url(r'^settings', 'ask_buevich.views.settings_view', name='settings'),
    url(r'^admin/', admin.site.urls),
]
