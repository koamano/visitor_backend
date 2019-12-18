from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EntriesSerializer
from .models import Entries
import re

class EntriesView(viewsets.ModelViewSet):
    serializer_class = EntriesSerializer

    def get_queryset(self):
        queryset = Entries.objects.all()
        filterParam = self.request.query_params.get('filter', None)
        nameParam = self.request.query_params.get('name', None)
        notesParam = self.request.query_params.get('notes', None)
        signedOutParam = self.request.query_params.get('signed_out', None)
        signedOutDateParam = self.request.query_params.get('signout_date', None)
        
        if filterParam is not None:
            queryset = (queryset.filter(name__icontains=filterParam) or 
            queryset.filter(notes__icontains=filterParam))
        if nameParam is not None:
            queryset = queryset.filter(name__icontains=nameParam) 
        if notesParam is not None:
            queryset = queryset.filter(notes__icontains=notesParam)
        if signedOutParam is not None:
            queryset = queryset.filter(is_signout=signedOutParam) 
        if signedOutDateParam is not None:
            queryset = queryset.filter(signout_date__icontains=signedOutDateParam) 
        return queryset
