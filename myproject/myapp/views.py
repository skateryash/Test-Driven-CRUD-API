from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from myapp.models import Item
from myapp.serializers import ItemSerializer

# Create your views here.
# List all items
@api_view(['GET'])
def get_items(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many = True)
    return Response(serializer.data)

# Create new item
@api_view(['POST'])
def create_item(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# Retrieve a single item
@api_view(['GET'])
def get_item(request, id):
    try:
        item = Item.objects.get(id=id)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT)
    
    serializer = ItemSerializer(item)
    return Response(serializer.data)

# Update an item
@api_view(['PUT'])
def update_item(request, id):
    try:
        item = Item.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ItemSerializer(instance=item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
        
# Delete item
@api_view(['DELETE'])
def delete_item(request, id):
    try:
        item = Item.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    item.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
