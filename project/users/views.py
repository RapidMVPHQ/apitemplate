import requests as http_requests
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView


class ActivateUserEmail(CreateAPIView):
    permission_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        uid = request.data.get("uid")
        token = request.data.get("token")
        response = None

        protocol = "https://" if request.is_secure() else "http://"
        hosts = request.get_host()
        post_url = f"{protocol}{hosts}/auth/users/activation/"
        payload = dict(uid=uid, token=token)
        res = http_requests.post(post_url, data=payload)

        response = dict(detail="success") if res.status_code < 300 else res.json()
        return Response(response)
