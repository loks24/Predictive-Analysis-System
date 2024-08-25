from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import GetTagCode
from . models import Report
from . Serializer import TagCodeSerializer
from django.contrib.auth.models import User
from django.views import generic
import json



class IndexView(generic.ListView):
    template_name='webapp/index.html'
    context_object_name='tagcodes'
    def get_queryset(self):
        return GetTagCode.objects.using('my_db_2').all()

class TagCodeView(APIView):
    

    def get(self,request):
        #lab=request.GET.get('Labels',False)
       
        TagCode1=list( GetTagCode.objects.using('my_db_2').filter(TagCode=request.GET.get('TagCode',False)))
        
        Final=GetTagCode.objects.using('my_db_2').filter(Labels=TagCode1[0])
        
        
 
        serializer=TagCodeSerializer(Final,many=True)
            
        return Response(serializer.data)
     

    def post(self):
        pass


class ReportView(generic.ListView):

    template_name='webapp/report.html'
    context_object_name='codes'
    def get_queryset(self):
        return Report.objects.using('my_db_1').all()