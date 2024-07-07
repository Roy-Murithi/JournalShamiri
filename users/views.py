from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework import permissions
from .models import CustomUser
from .serializers import CustomUserSerializer, PasswordResetSerializer


class UserSignUp(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            # # Check if passwords match
            # password = serializer.validated_data.get('password')
            # confirm_password = request.data.get('confirm_password')
            # if password != confirm_password:
            #     return Response({'Error': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)
            
            # Create user without hashing the password
            user = CustomUser.objects.create_user(**serializer.validated_data)
            user.save()
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

class CheckAuthentiction(APIView):
    def get(self, request):
        return Response({'message': 'User is Authenticated'})    

class CurrentUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user 

        user_data = {
            'id': user.id,
            'username': user.first_name + ' ' + user.last_name,
            'email': user.email
        }

        return Response(user_data)
    
class PasswordResetView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            new_password = serializer.validated_data['new_password']

            try:
                user = CustomUser.objects.get(email=email)
                user.set_password(new_password)
                user.save()
                return Response({'message': 'Password reset successful'}, status=status.HTTP_200_OK)
            except CustomUser.DoesNotExist:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
