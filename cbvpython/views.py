from django.http import HttpResponse
from django.views.generic import TemplateView

class IndexView(TemplateView):
	template_name = 'index.html'
	# def get(self, request):
	# 	return HttpResponse("Successed !!")

	def post(self, request):
		return HttpResponse("You are on the POST method !!")