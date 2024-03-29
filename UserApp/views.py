from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import *
from .models import *
from django.core.mail import send_mail, BadHeaderError
from django.core.exceptions import ValidationError
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from django.utils.crypto import get_random_string
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.sessions.models import Session
from django.contrib.auth.hashers import check_password

# Create your views here.



class LoginUserView(APIView):
    def get(self,request):
        if request.session.get('user_email'):
            return redirect('user-home')
        
        return render(request, 'pages/Login.html')
    
    def post(self, request):
        email = request.data.get('email') 
        password = request.data.get('password')  

        try:
            user = AppUsers.objects.get(email=email)
            if check_password(password, user.password):
             
                request.session['user_email'] = user.email
                return redirect('user-home')
            else:
             
                return render(request, 'pages/Login.html', {'error_message': 'Invalid email or password'})
        except AppUsers.DoesNotExist:
       
            return render(request, 'pages/Login.html', {'error_message': 'Invalid email or password'})
        


    

class RegisterUserView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return render(request, 'pages/Register.html')
    
    def post(self, request):
        try:
            email = request.data['email']

            # Check if the user already exists
            if AppUsers.objects.filter(email=email).exists():
                
                return render(request, 'pages/Register.html', {'messages': 'User with this email already exists.'})
            serializer = AppUsersSerializer(data=request.data)
            if serializer.is_valid():
                # Generate and send OTP
                otp = get_random_string(length=4, allowed_chars='1234567890')
                

                send_mail(
                    'OTP for Registration',
                    f'Your OTP for registration is: {otp}',
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False,
                )

                # Save OTP to the database
                user = serializer.save()
                request.session['user_email'] = user.email
                UserOTP.objects.create(user=user, otp=otp)

                # Redirect to OTP verification page (if needed)
                return redirect('user-otp')

        except BadHeaderError:
            return render(request, 'pages/Register.html',{'messages': 'Invalid email header.'})

        except ValidationError as e:
            return render(request, 'pages/Register.html', {'messages': f'Validation error: {str(e)}'})


        return Response(request, 'pages/Register.html',{'messages': 'Invalid data.'})

    



class OtpUserView(APIView):
    def get(self, request):
        user_email = request.session.get('user_email')
        if "user_email" :
            print(user_email,"email")
        return render(request, 'pages/Otp.html')
    
    def post(self, request):
        user_email = request.session.get('user_email')
        get_otp = request.POST.get('otp')
       
        if get_otp:
           
            
            usr = AppUsers.objects.get(email=user_email)
          

            if int(get_otp) == UserOTP.objects.filter(user=usr).last().otp:
              
                usr.is_active = True
                usr.save()

                messages.success(request, f'Account is created for {usr.email}')
                # Redirect to another view with user information
                
                return redirect('/')

            else:
                messages.warning(request, 'You entered a wrong OTP')
                return render(request, 'pages/Otp.html')
        else:
           return render(request, 'pages/Otp.html', {'messages': 'Invalid data.'}, status=status.HTTP_400_BAD_REQUEST)
            

def UserHome(request):
    return render(request, 'pages/Home.html')

def logout(request):

    if 'user_email' in request.session:
            request.session.flush()
    return redirect('user-login')
