from rest_framework.views import APIView
from rest_framework.response import Response
from profiles.models import Profile
from profiles.serializers import ProfileSerializer


class ProfileList(APIView):
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)
