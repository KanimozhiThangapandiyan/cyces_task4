from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class ChangePasswordAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user  # Accessing the user making the request
        
        # Check if the user is a superuser
        if user.is_superuser:
            new_password = request.data.get('new_password')
            if new_password:
                # Set the new password and save the user
                user.set_password(new_password)
                user.save()
                return Response({"success": "Password changed successfully"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "New password not provided"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Return forbidden error if the user is not a superuser
            return Response({"error": "You do not have permission to change the password"}, status=status.HTTP_403_FORBIDDEN)
