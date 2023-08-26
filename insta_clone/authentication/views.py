from django.shortcuts import render
from django.views.generic import View
from authentication.forms import UserForm
# Create your views here.

class SignUpView(View):
    
    template_name = 'authentication/signup.html'
    form_class = UserForm
    def get(self,request , *args, **kwargs):
        # Run this code
        return render(request, self.template_name)

    def post(self,request,*args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signup_view')
        return render(request, self.template_name)



