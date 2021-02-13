from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from postcodes.uk import PostCodeUK


class PostCodeUKAPI(APIView):
    def get(self, request):
        raw_postcode = request.GET.get('postcode', '')
        postcode = PostCodeUK(raw_postcode)
        http_status = status.HTTP_200_OK if postcode.is_valid else status.HTTP_400_BAD_REQUEST
        http_payload = postcode.to_dict()
        return Response(http_payload, status=http_status)
