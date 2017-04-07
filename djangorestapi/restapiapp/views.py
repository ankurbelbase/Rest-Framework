from django.shortcuts import render

from restapiapp.serializer import EventSerializers

from restapiapp.models import Event

from rest_framework import viewsets


class EventApiView(viewsets.ModelViewSet):
	# from our model Event
	queryset = Event.objects.all().order_by('-date')

	# from event serializer
	serializer_class = EventSerializers
