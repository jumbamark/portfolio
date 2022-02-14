from django.http import JsonResponse
from base.models import Question
from .serializers import QuestionSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response

# we querying all of the answers to the questions from our db and we wanna pull that data out and we make sure it's in json data
# many = True ,we are returning multiple questions


@api_view(["GET"])
def votingData(request):
    # questions = Question.objects.all()
    # serializer = QuestionSerializer(questions, many=True)
    # return Response(serializer.data)

    frontend = Question.objects.filter(answer="Frontend").count()
    backend = Question.objects.filter(answer="Backend").count()
    fullstack = Question.objects.filter(answer="FullStack").count()

    return Response({"frontend": frontend, "backend": backend, "fullstack": fullstack})
