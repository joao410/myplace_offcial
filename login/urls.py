from django.urls import path
from .views import RegistrationView, UsernameValidationView, EmailValidationView , VerificationView, LoginView, LogoutView
from django.views.decorators.csrf import csrf_exempt 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    path('', LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    #path('validate-username', csrf_exempt(UsernameValidationView.as_view()),name="validate-username"),
    #path('validate-email', csrf_exempt(EmailValidationView.as_view()), name="validate-email"),
    #path('activate/<uidb64>/<token>', VerificationView.as_view(), name="activate"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)