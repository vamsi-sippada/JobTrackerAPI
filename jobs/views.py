from django.shortcuts import render
from rest_framework import generics
from .models import Job
from .serializers import JobSerializer
from rest_framework.permissions import IsAuthenticated

class JobListCreateView(generics.ListCreateAPIView):

    # queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Job.objects.filter(user=self.request.user)

        status = self.request.query_params.get('status')
        search = self.request.query_params.get('search')

        if status:
            queryset = queryset.filter(status=status)

        if search:
            queryset = queryset.filter(company_name__icontains=search)

        return queryset 
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class JobDetailView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Job.objects.filter(user=self.request.user)