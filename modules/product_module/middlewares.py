from django.utils.deprecation import MiddlewareMixin

class RoleMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            request.user.role = getattr(request.user, 'role', 'public')
        else:
            request.user.role = 'public'
