from .models import UserEvent
from django_user_agents.utils import get_user_agent

class UserEventMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Exclude admin URLs from tracking
        if request.path.startswith('/admin404/'):
            return response

        user_agent = get_user_agent(request)
        
        event_data = {
            'user': request.user if request.user.is_authenticated else None,
            'session_key': request.session.session_key,
            'event_type': 'page_view',
            'page_url': request.build_absolute_uri(),
            'page_name': request.resolver_match.view_name if request.resolver_match else '',
            'ip_address': request.META.get('REMOTE_ADDR'),
            'user_agent': str(user_agent),
            'device_type': 'Mobile' if user_agent.is_mobile else 'Desktop' if user_agent.is_pc else 'Tablet' if user_agent.is_tablet else 'Bot' if user_agent.is_bot else 'Other',
            'browser': user_agent.browser.family,
            'operating_system': user_agent.os.family,
            'referrer': request.META.get('HTTP_REFERER'),
        }

        # Track site visit
        if not request.session.get('has_visited'):
            request.session['has_visited'] = True
            request.session.set_expiry(0) # Expire on browser close
            visit_data = event_data.copy()
            visit_data['event_type'] = 'site_visit'
            UserEvent.objects.create(**visit_data)

        UserEvent.objects.create(**event_data)

        return response
