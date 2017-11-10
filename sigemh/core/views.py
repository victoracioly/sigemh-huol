from django.shortcuts import render
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class BaseView(View):

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(BaseView, self).dispatch(request, *args, **kwargs)


class HomeView(BaseView):

    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)


home = HomeView.as_view()
