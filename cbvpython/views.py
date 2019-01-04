from django.http import HttpResponse
from django.views.generic import TemplateView


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')

class IndexView(TemplateView):
	template_name = 'index.html'
	# def get(self, request):
	# 	return HttpResponse("Successed !!")

	def post(self, request):
		return HttpResponse("You are on the POST method !!")