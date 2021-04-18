from django.urls import path
from .views import MessagesListView, MessageDetailView, MessageCreateView

app_name = 'app'


urlpatterns = [

    path('messages/list/', MessagesListView.as_view()),
    path('messages/single/<int:pk>', MessageDetailView.as_view()),
    path('message/', MessageCreateView.as_view()),

]

