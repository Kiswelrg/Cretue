from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect,HttpResponse
class AdminMiddleWare(MiddlewareMixin):
	def process_request(self,request):
		if request.path != "/" and request.path != "/signin" and request.path != "/login" and request.path != '/favicon.ico' and request.path[0:6] != '/tools' and request.path != '/ems/code':
			if not request.session.has_key("username") or not request.session["username"]:
				return HttpResponseRedirect("/signin")
		if request.path[0:6] == '/crawl' and len(request.path) > 7 and request.session['username'] != '16020031085':
			return HttpResponseRedirect("/")