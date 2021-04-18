from rest_framework import serializers
from .models import Message


class MessagesListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('email', 'text', 'create_date', 'update_date')


class MessageDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = "__all__"  #('author', 'email', 'text', 'create_date', 'update_date')


import re
def validateEmail(email):
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    if (re.search(regex, email)):
        return email
    else:
        raise serializers.ValidationError('Email is not real.')

def validateMSG(msg):
    regex = '^(?!\s*$).+'
    if len(msg)<100:
        if (re.search(regex, msg)):
            return msg
        else:
            raise serializers.ValidationError('Message is empty.')
    else:
        raise serializers.ValidationError('Message is long than 100 symbols.')


class MessageCreateSerializer(serializers.ModelSerializer):

    email = serializers.CharField(validators={validateEmail})
    text = serializers.CharField(validators={validateMSG})
    class Meta:
        model = Message
        fields = "__all__"    #('email', 'text')