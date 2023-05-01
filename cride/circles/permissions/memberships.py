"""Circle permission classes."""

# Django REST Framework
from rest_framework.permissions import BasePermission

# Models
from cride.circles.models import Membership

class IsActiveCircleMember(BasePermission):
    """Allow access only to circle members.
    
    Expect that the views implementing this permission
    have a circle attribute assigned.
    """

    def has_permission(self, request, views):
        """Verify user is an active member of the circle."""
        try:
            Membership.objects.get(
                user=request.user,
                circle=views.circle,
                is_active=True
            )
        except Membership.DoesNotExist:
            return False
        return True