import json

from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from apiV1.serializers import AccountSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework import status, permissions
from oauth2_provider.settings import oauth2_settings
from oauth2_provider.views.mixins import OAuthLibMixin


# @api_view(['POST'], )
class userRegistration_view(OAuthLibMixin, CreateAPIView):
    server_class = oauth2_settings.OAUTH2_SERVER_CLASS
    validator_class = oauth2_settings.OAUTH2_VALIDATOR_CLASS
    oauthlib_backend_class = oauth2_settings.OAUTH2_BACKEND_CLASS
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        if request.auth is None:
            serializer = AccountSerializer(data=request.data)
            data = {}
            if serializer.is_valid():
                try:
                    account = serializer.save()
                    url, headers, body, token_status = self.create_token_response(request)
                    if token_status != 200:
                        raise Exception(json.loads(body).get("error_description", ""))
                    else:
                        data['response'] = 'successfully registered'
                        data['email'] = account.email
                        data['username'] = account.username
                        token = Token.objects.get(user=account).key
                        data['token'] = token
                        return Response(data, json.loads(body), status=token_status)

                except Exception as e:
                    return Response(data={"error": e.message}, status=token_status)

            else:
                return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                # data = serializer.errors
        # return Response(data)
        return Response(status=status.HTTP_403_FORBIDDEN)
