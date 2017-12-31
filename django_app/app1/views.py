from django.views.generic import TemplateView

# Create your views here.
class AboutView(TemplateView):
    template_name = "about.html"
    def get(self, request):
        # <view logic>
        return HttpResponse('result')