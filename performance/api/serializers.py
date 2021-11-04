from django.contrib.auth import models
from rest_framework import serializers
from performance.models  import Announcement,Performance,Profile,Annou_Detail,Metas


class Announcementserializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields= '__all__'

class Performanceserializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    def get_user(self,obj):
        return obj.user.username

    class Meta:
        model = Performance
        fields= ("year",
                "month",
                "user",
                "porcentagem")
                