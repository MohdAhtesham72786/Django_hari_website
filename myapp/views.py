from django.shortcuts import render
#from rest_framework import generics
from rest_framework.views import APIView
import io, csv, pandas as pd
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.request import Request
from myapp.models import Coupon
from tablib import Dataset
from django.http import HttpResponse, JsonResponse
#from .resources import CouponReource
#from myapp.serializers import SaveCouponSerializer, CouponUploadSerializer
from rest_framework import status


'''class UploadCouponView(generics.CreateAPIView):
    serializer_class = CouponUploadSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        coupons = serializer.validated_data['Coupons']
        reader = pd.read_csv(coupons)
        for _, row in reader.iterrows():
            new_coupon = Coupon(
                       code= row["code"],
                       description= row['description'],
                       amount= row["amount"],
                       amount_type= row["amount_type"]
                       )
            new_coupon.save()
        return Response({"status": "success"},
                        status.HTTP_201_CREATED)'''
                        
class CSVUploadHandler(APIView):
    #parser_classes = (CSVUploadParser, )
    
    def post(self, request, format='csv'): 
        if request.method == 'POST':
            oldCoupons = []
            newCoupons = []
            coupons =  request.data['coupons']
            reader = pd.read_csv(coupons)
            
            for _, row in reader.iterrows():
                if Coupon.objects.filter(code = row['code']).exists():
                    oldCoupons.append(row['code'])
                else :
                    Coupon.objects.create(
                       code= row['code'],
                       description= row['description'],
                       amount= row['amount'],
                       amount_type= row['amount_type']
                       )
                    newCoupons.append(row['code'])
            
            return Response({
                "status": "success",
                "new" : len(newCoupons),
                "duplicate_count" : len(oldCoupons),
                "dulicate_code" : oldCoupons,
                "new_code" : newCoupons,
                },status.HTTP_201_CREATED)
        else : 
            return Response({"status": "success"},status.HTTP_405_METHOD_NOT_ALLOWED)

                              
                      
                        
    
   