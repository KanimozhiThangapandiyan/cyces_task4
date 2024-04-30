from django.http import JsonResponse


def success_response(data=None, message="Success"):
    response_data = {
        'success': True,
        'message': message,
        'data': data
    }
    return JsonResponse(response_data)


def failure_response(message="Failure"):
    response_data = {
        'success': False,
        'message': message
    }
    return JsonResponse(response_data, status=400)
