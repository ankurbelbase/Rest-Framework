from rest_framework import serializers

from restapiapp.models import Event


class EventSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Event
		#fields from models that gonna shown in api
		fields = ('name', 'location', 'date')