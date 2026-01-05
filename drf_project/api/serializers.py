from rest_framework import serializers
from students.models import Students


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Students           #creating serializers 
        fields = "__all__"