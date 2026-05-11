from rest_framework import serializers
from .models import Job

class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = [
            'id',
            'company_name',
            'role',
            'status',
            'applied_date',
            'notes',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at']