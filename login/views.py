from django.shortcuts import redirect, render
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
#from validate_email import validate_email
from django.contrib import messages
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import auth
from helpdesk.models import UsuarioPessoal





# Create your views here.

class EmailValidationView(View):

    def post(self, request):
        data = json.loads(request.body)
        email = data['email']    

        if not validate_email(email):
            return JsonResponse({'email_error':'Esse e-mail nao e valido'}, status=400)
        
        if Usuarios.objects.filter(email=email).exists():
            return JsonResponse({'email_error':'Esse e-mail ja esta cadastrado'}, status=409)
        
        return JsonResponse({'email_valid': True})



class UsernameValidationView(View):

    def post(self, request):
        data = json.loads(request.body)
        username = data['username']    

        if not str(username).isalnum():
            return JsonResponse({'username_error':'username deve conter apenas letras/numeros'}, status=400)
        
        if Usuarios.objects.filter(usarname=username).exists():
            return JsonResponse({'username_error':'Esse username ja esta sendo utilizado'}, status=409)
        
        return JsonResponse({'username_valid': True})


class RegistrationView(View):

    def get(self, request):
        return render(request, 'authentication/register.html')

    def post(self, request):
        #GET USER DATA
        #VALIDATE
        #create user account

        usuario = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        context = {
            'fieldValues': request.POST
        }

        if not Usuarios.objects.filter(usuario=usuario).exists():
            if not Usuarios.objects.filter(email=email).exists():                
                if len(password) < 6:
                    messages.error(request, "Senha muito curta(<6)")
                    return render(request, 'authentication/register.html', context)
                
                if password != repassword:
                    messages.error(request, "As senhas nao batem")
                    return render(request, 'authentication/register.html', context)

                
                user = ser.objects.create_user(username=username, email=email)
                user.set_password(password)
                user.is_active = False
                user.save()
                """
                email_subject = 'Ative sua conta'

                # path_to_View
                # getting domain we are on
                # relative url verification
                # encode uid
                # token                 

                email_body = 'Teste Body'
                email = EmailMessage(
                    email_subject,
                    email_body,
                    'noreply@.com',
                    [email],                   
                )
                email.send(fail_silently=False)
                """
                messages.success(request, "Conta criada com sucesso")
                return render(request, 'authentication/register.html')

        return render(request, 'authentication/register.html')

class VerificationView(View):
    def get(self, request, uidb64, token):
        return redirect


class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')

    def post (self, request):
        username = request.POST['username']
        password = request.POST['password']
        username =  username.upper()
        password = password.upper()

        if username and password:             
            user = auth.authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    if user.is_staff:
                        auth.login(request, user)
                        messages.success(request, 'Bem Vindo '+ username +', você está logado')
                        return redirect('home')
                    else:
                        auth.login(request, user)
                        messages.success(request, 'Bem Vindo '+ username +', você está logado')
                        #return redirect('home')
                        return redirect('home')
                        

                messages.error(request, 'Conta nao esta ativa, por favor checar o e-mail de ativacao')
                return render(request, 'authentication/login.html')
            messages.error(request, 'Credenciais erradas ou nao cadastradas, por favor tente novamente')
            return render(request, 'authentication/login.html')
        messages.error(request, 'Por favor preencha suas credenciais')
        return render(request, 'authentication/login.html')


class LogoutView(View):
    def post(self, request):
        auth.logout(request)
        messages.success(request, 'Logout com sucesso')
        return redirect('login')
