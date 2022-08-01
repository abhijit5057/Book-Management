from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from app_demo.models import Author,Book
def register(request):
  if request.method=="POST":
    name=request.POST.get('name')
    email = request.POST.get('email')
    password =request.POST.get('password')
    user = Author.objects.create_user(
            email=email,
            username=name,  
            password=password,
        )      
    user.set_password(password)
   
    # register=Author(username=name,email=email,password=password)
    if user:
      user.save()
      
      return redirect('login')
  return render(request,'register.html')

def login(request):
  if request.method=="POST":
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(email=email, password=password)
    request.session['user']=user.id
    print( )
    if user is not None:
      return redirect('dashboard')
    else:
      return HttpResponse("User Not Valid")
  return render(request,'Login.html')

def dashboard(request):
  user=Author.objects.get(id=request.session['user'])
  book=Book.objects.filter(author=user.id)
  print("----------------",book)
  # for i in book:
  #   print("#######",i.name)
  return render(request,'Dashboard.html',{'book':book,'user':user})
    























# from rest_framework.views import APIView
# from app_demo.serializer import AuthorRegisterSerializer,AuthorLoginSerializer
# from rest_framework.response import Response
# from  rest_framework import status
# from django.core import serializers

# # Create your views here.
# from rest_framework_simplejwt.tokens import RefreshToken
# def get_tokens_for_user(user):
#   refresh = RefreshToken.for_user(user)
#   return {
#       'refresh': str(refresh),
#       'access': str(refresh.access_token),
#   }
# class AuthorRegistraion(APIView):
#     def post(self,request):
#         serializer=AuthorRegisterSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             response = {
#             'success': True,
#             'status_code': status.HTTP_403_FORBIDDEN,
#             'Data': serializer.data
#         }
#             return Response(response,status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# class AuthorLoginView(APIView):
#   def post(self, request, format=None):
#     serializer = AuthorLoginSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     email = serializer.data.get('email')
#     password = serializer.data.get('password')
#     user = authenticate(email=email, password=password)
#     if user is not None:
#       token = get_tokens_for_user(user)
#       print(user)
#       return Response({'token':token, 'msg':'Login Success'}, status=status.HTTP_200_OK)
#     else:
#       return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)


# class Dashboard(APIView):
#     def get(self,request):
#         user=request.user
#         print(user)
#         # serialized_qs = serializers.serialize('json', user)
#         # print(serialized_qs)
#         return Response("Done",status=status.HTTP_200_OK)