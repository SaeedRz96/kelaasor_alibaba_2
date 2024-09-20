from user_app.models import RequestLog
from django.contrib.auth.models import AnonymousUser

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.log_request(request)
        
        response = self.get_response(request)

        return response

    def log_request(self, request):
        ip_address = self.get_client_ip(request)

        user = request.user if isinstance(request.user, AnonymousUser) else request.user

        RequestLog.objects.create(
            method=request.method,
            path=request.path,
            ip_address=ip_address,
            user=user if user.is_authenticated else None
        )

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip