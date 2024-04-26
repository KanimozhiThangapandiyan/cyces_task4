from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

class ChangePasswordAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user  # Accessing the user making the request
        
        # Check if the user is a superuser
        if user.is_superuser:
            print("Request Data:", request.data)  # Print request data for debugging
            username = request.data.get('username')
            old_password = request.data.get('old_password')
            new_password = request.data.get('new_password')
            confirm_password = request.data.get('confirm_password')
            
            print("Username:", username)  # Print received username for debugging
            
            if not all([username, old_password, new_password, confirm_password]):
                return Response({"error": "Please provide all required fields"}, status=status.HTTP_400_BAD_REQUEST)
            
            # Check if the username matches the user's username
            if username != user.username:
                return Response({"error": "Username does not match"}, status=status.HTTP_400_BAD_REQUEST)
            
            # Check if the old password matches the user's current password
            if not check_password(old_password, user.password):
                return Response({"error": "Old password is incorrect"}, status=status.HTTP_400_BAD_REQUEST)
            
            # Check if the new password matches the confirm password
            if new_password != confirm_password:
                return Response({"error": "New password and confirm password do not match"}, status=status.HTTP_400_BAD_REQUEST)
            
            # Set the new password and save the user
            user.set_password(new_password)
            user.save()
            return Response({"success": "Password changed successfully"}, status=status.HTTP_200_OK)
        else:
            # Return forbidden error if the user is not a superuser
            return Response({"error": "You do not have permission to change the password"}, status=status.HTTP_403_FORBIDDEN)

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.permissions import IsAuthenticated

# class ChangePasswordAPIView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request, *args, **kwargs):
#         user = request.user  # Accessing the user making the request
        
#         # Check if the user is a superuser
#         if user.is_superuser:
#             new_password = request.data.get('new_password')
#             if new_password:
#                 # Set the new password and save the user
#                 user.set_password(new_password)
#                 user.save()
#                 return Response({"success": "Password changed successfully"}, status=status.HTTP_200_OK)
#             else:
#                 return Response({"error": "New password not provided"}, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             # Return forbidden error if the user is not a superuser
#             return Response({"error": "You do not have permission to change the password"}, status=status.HTTP_403_FORBIDDEN)
