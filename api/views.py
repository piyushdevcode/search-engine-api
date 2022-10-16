from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.scraper import scrape_duck_results


@api_view()
def search_view(request):
    query = request.query_params.get("query")
    if not query:
        return Response({}, status=status.HTTP_400_BAD_REQUEST)

    # if pages are not specified in query params then default is 1
    pages = request.query_params.get("pages", 1)

    print("Search requested for ", query)
    query = query.strip()
    data = scrape_duck_results(query, pages)
    return Response({"results": data}, status=status.HTTP_200_OK)
