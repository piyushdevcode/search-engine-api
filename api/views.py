from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.scraper import scrape_duck_results


@api_view()
def search_view(request):
    if not request.query_params:
        return Response({}, status=status.HTTP_400_BAD_REQUEST)
    query = request.query_params.get("query")
    pages = request.query_params.get("pages", 1)
    print("My query: ", query)
    query = query.strip()
    data = scrape_duck_results(query, pages)
    return Response(data, status=status.HTTP_200_OK)
