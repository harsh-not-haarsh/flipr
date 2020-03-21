from django.shortcuts import render
from django.views.generic import CreateView
from .forms import signupForm
from .models import UserProfile

class registerView(CreateView):
    form_class = signupForm
    template_name = 'accounts/signup.html'
    success_url = '/accounts/login/'
    
    def form_valid(self, form):
        data = self.request.POST.copy()
        form = signupForm(data)
        user = form.save()
        user.username = data['email']
        user.save()
        userprofile = UserProfile.objects.create(user=user)
        userprofile.save()
        return super(registerView, self).form_valid(form)

    def form_invalid(self, form, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)
    