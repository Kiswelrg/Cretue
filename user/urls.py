from django.urls import path
from django.conf.urls import url
from . import views,crawl

urlpatterns = [
	path('',views.Index),

	#record viewers
	path('count', views.count),


	#cretue
    path('ret', views.ret),
    path('code', views.getVCode),
    path('transc', views.transc),
    path('grades', views.getGrades),
    path('coins', views.coins),
    path('alstd', views.alstd),
    path('frd', views.frd),
    path('ss', views.getSS),
]