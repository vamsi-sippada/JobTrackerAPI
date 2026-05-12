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
            'deadline',
            'notes',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']