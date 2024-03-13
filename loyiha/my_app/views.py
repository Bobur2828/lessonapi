from rest_framework.views import APIView
from .models import Women
from .serializers import WomenSerializer
from rest_framework.response import Response
from django.forms import model_to_dict
class WomeApiView(APIView):
    def get(self, request):
        women=Women.objects.all().values()
        return Response({"women":list(women) })
    

    def post(self,request):
        new_post=Women.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id'],

        )
        return Response({"post":model_to_dict(new_post)})






# class WomeApiView(APIView):
#     queryset=Women.objects.all()
#     serializer_class=WomenSerializer