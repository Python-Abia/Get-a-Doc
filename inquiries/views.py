from django.shortcuts import render
from .models import InquiryCategory, Syptoms, Inquiry
from .serializers import SyptomsSerializer, InquirySerializer, InquiryCategorySerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

# Create your views here.

# inquiries API endpoints.

@api_view(['GET', 'POST'])
def inquiries_list(request):
    if request.method == 'GET':
        inquiry = Inquiry.objects.all()
        if inquiry is None:
            return Response({"error":"inquiries does not exist"}, status=status.HTTP_404_NOT_FOUND)
        serializer = InquirySerializer( inquiry, many = True)
        return Response(serializer.data)
    
    else:
        #create item
        if request.method == 'POST':
            serializer = InquirySerializer(data = request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)     


@api_view(['GET', 'PUT', 'DELETE'])
def inquiry_list(request, pk):
    
    try:
        inquiry =  Inquiry.objects.get(pk=pk)        
    except  Inquiry.DoesNotExist:
        return Response({"error":"Inquiry not found"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = InquirySerializer(inquiry)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    elif request.method == "PUT": 
            serializer = InquirySerializer(inquiry, data = request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response({"message":"inquiry edited successfully"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == "DELETE":
        InquiryCategorySerializer.delete()
        return Response(status = status.HTTP_204_NO_CONTENT) 


# Category API endpoints
@api_view(['GET', 'POST'])
def categories_list(request):
        if request.method == 'GET':
            category = InquiryCategory.objects.all()
            serializer = InquiryCategorySerializer( category, many = True)
            return Response(serializer.data)
    
        else:
            if request.method == 'POST':
                serializer = InquiryCategorySerializer(data = request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, safe = status.HTTP_400_BAD_REQUEST)    
         
         
@api_view(['GET', 'PUT', 'DELETE'])
def category_list(request, pk):
        try:
            category = InquiryCategory.objects.get(pk=pk)
        
        except InquiryCategory.DoesNotExist:
            return Response({"error":"category not found"}, status=status.HTTP_404_NOT_FOUND)
    
        if request.method == "GET":
            serializer =  InquiryCategorySerializer(category)
            return Response(serializer.data)
        
        elif request.method == "PUT": 
            serializer =  InquiryCategorySerializer(category, data = request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == "DELETE ":
            category.delete()
            return Response(status = status.HTTP_204_NO_CONTENT) 
    
# symptoms API endpoints
@api_view(['GET', 'POST'])
def syptoms_list(request):
        if request.method == 'GET':
            syptoms= Syptoms.objects.all()
            serializer = SyptomsSerializer( syptoms, many = True)
            return Response(serializer.data)
    
        else:
            if request.method == 'POST':
                serializer = SyptomsSerializer(data = request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, safe = status.HTTP_400_BAD_REQUEST)    
         
         
@api_view(['GET', 'PUT', 'DELETE'])
def syptom_list(request, pk):
        try:
            syptom = Syptoms.objects.get(pk=pk)
        
        except Syptoms.DoesNotExist:
            return Response({"error":"syptom not found"}, status=status.HTTP_404_NOT_FOUND)
    
        if request.method == "GET":
            serializer =  SyptomsSerializer(syptom)
            return Response(serializer.data)
        
        elif request.method == "PUT": 
            serializer =  SyptomsSerializer(syptom, data = request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == "DELETE ":
            syptom.delete()
            return Response(status = status.HTTP_204_NO_CONTENT) 
    
