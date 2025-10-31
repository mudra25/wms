from rest_framework import viewsets, permissions
from .models import Organization, Location
from .serializers import OrganizationSerializer, LocationSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]  # or IsAdminUser, etc.

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'organization'):
            return self.queryset.filter(organization=user.organization)
        return self.queryset.none()
