from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def search_view(request):
    query = request.query_params.get("query")
    print("My query: ", query)
    my_data = {"name": "John 'Doe'"}
    return Response(my_data, status=status.HTTP_200_OK)
