from django.views import View
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class UserRegisterView(View):
    template_name = 'pages/register.html'
    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=True)
            print("user =", user)
            user.set_password(form.cleaned_data.get('password'))
            print("username = ", user.username)
            login(request, user)
            return redirect("/")

     
class UserLoginView(View):
    template_name = 'pages/login.html'
    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(request, data=request.POST or None)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
        return redirect("/")
    
class UserLogoutView(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('/')