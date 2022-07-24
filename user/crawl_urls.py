from django.urls import path
from django.conf.urls import url
from . import views,crawl

urlpatterns = [
	path('clt',crawl.collectStuxh),
	path('ctrl',crawl.ctrl),
	path('sgl',crawl.sgl),
	path('lic',crawl.lic),
	path('gameon',crawl.gameon),
]