from django.conf.urls import url
import views
urlpatterns = [
    url(r'^$', views.book, name="book"),
    url(r'^(?P<book_id>\d+)$', views.intro, name="intro"),
    url(r'^article/(?P<article_id>\d+)$', views.article, name="article"),
]