from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ViewSet

from app.serializers import *

from rest_framework.response import Response

class ProductCrud(ViewSet):
    def list(self,request):
        POD=Product.objects.all()
        JOD=ProductModelSerializer(POD,many=True)
        return Response(JOD.data)
    

    def retrieve(self,request,pk):
        PO=Product.objects.get(pk=pk)
        JOD=ProductModelSerializer(PO)
        return Response(JOD.data)

    def create(self,request):
        JDO=request.data
        PDO=ProductModelSerializer(data=JDO)
        if PDO.is_valid():
            PDO.save()
            return Response({'created':'Data is created...'})
        
    def update(self,request,pk):
        PO=Product.objects.get(pk=pk)
        JD=request.data
        PDO=ProductModelSerializer(PO,data=JD)
        if PDO.is_valid():
            PDO.save()
            return Response({'Update':'Data is Updated'})
        else:
            return Response({'Error':'Update Not Done...'})
        

    def partial_update(self,request,pk):
        PO=Product.objects.get(pk=pk)
        JD=request.data
        PDO=ProductModelSerializer(PO,data=JD,partial=True)
        if PDO.is_valid():
            PDO.save()
            return Response({'Update':'Data is Updated'})
        else:
            return Response({'Error':'Update Not Done'})

    def destroy(self,request,pk):
        Product.objects.get(pk=pk).delete()
        return Response({'delete':'Data is deleted'})


