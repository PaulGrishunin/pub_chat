from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import Message
from .serializers import  MessagesListSerializer, MessageDetailSerializer, MessageCreateSerializer



class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10
    page_query_param = 'page'



class MessagesListView(generics.ListAPIView):
    """Get list of messages with pagination"""
    queryset = Message.objects.all().order_by('create_date')
    serializer_class = MessagesListSerializer
    pagination_class = StandardResultsSetPagination



class MessageDetailView(APIView):
    """Get message details by id"""
    def get(self, request, pk):
        message = Message.objects.filter(id=pk)
        serializer = MessageDetailSerializer(message, many=True)
        return Response(serializer.data)



class MessageCreateView(APIView):
    """Create(sent) new message"""
    def post(self, request):
        message =  request.data
        serializer = MessageCreateSerializer(data=message)
        if serializer.is_valid(raise_exception=True):
            message = serializer.save()
        return Response({"success": "Message '{}' created successfully".format(message.text)}, status=201)