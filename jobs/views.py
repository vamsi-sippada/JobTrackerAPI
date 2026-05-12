from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count, Q
from .models import Job
from .serializers import JobSerializer

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
    
class JobStatsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = Job.objects.filter(user=request.user)

        stats = queryset.aggregate(
            total=Count('id'),
            applied=Count('id', filter=Q(status='applied')),
            interview=Count('id', filter=Q(status='interview')),
            rejected=Count('id', filter=Q(status='rejected')),
            offer=Count('id', filter=Q(status='offer')),
        )

        return Response(stats)