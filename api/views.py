from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.parsers import FormParser, MultiPartParser
from .business_logic import *


class GetFileView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        serializer = FileUploadSerializer(data=request.data)
        if serializer.is_valid():
            media = serializer.save()
            if str(media.file).split('.')[-1] != 'csv':
                return Response("The file format is not allowed", status=status.HTTP_400_BAD_REQUEST)
            errors = reading_and_writing(media)
            if len(errors):
                return Response(errors, status=status.HTTP_400_BAD_REQUEST)
            return Response("Success!", status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        customers = list(Customer.objects.all().order_by('-spent_money')[:5])
        top_gems = []
        for cust in customers:
            gems = set(cust.deals.all().values_list('gem_name', flat=True))
            top_gems.append(gems)
        counter = len(top_gems)
        while counter > 0:
            cur = top_gems.pop(0)
            ex_cur = set()
            for i in range(len(top_gems)):
                ex_cur = ex_cur | top_gems[i]
            cur = cur & ex_cur
            top_gems.append(cur)
            counter -= 1
        response = {'response': []}
        for i in range(len(customers)):
            user = {
                        'username': customers[i].username,
                        'spent_money': customers[i].spent_money,
                        'gems': top_gems[i]
                    }
            response['response'].append(user)

        return Response(response, status=status.HTTP_200_OK)