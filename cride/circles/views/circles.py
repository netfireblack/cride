"""Circle views."""

# Django REST Framework
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Serializers
from cride.circles.serializers import CircleModelSerializer

# Models
from cride.circles.models import Circle

class CircleViewSet(viewsets.ModelViewSet):
    """Circle view set."""

    queryset = Circle.objects.all()
    serializer_class = CircleModelSerializer
    permission_classes = (IsAuthenticated,)