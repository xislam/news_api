from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api_news_user.models import News
from .serializers import UserSerializer, NewsSerializer


class UserAPIView(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'data': serializer.data},
                status=status.HTTP_201_CREATED
            )

        return Response(
            {'data': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )


class NewsAPIView(APIView):
    serializer_class = NewsSerializer
    """
    List all news, or create a new new.
    """

    def get(self, request):
        if request.user.is_authenticated:
            snippets = News.objects.all()
            serializer = NewsSerializer(snippets, many=True)
            return Response(serializer.data)
        else:
            return Response("you are not authored")

    def post(self, request):
        if request.user.is_authenticated:
            serializer = NewsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("you are not authored")
