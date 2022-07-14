from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item
from .serializer import ItemSerializer
from rest_framework import status


@api_view(["GET"])
def getItems(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def createItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def getOneItem(request, pk):
    item = Item.objects.get(pk=pk)
    serializer = ItemSerializer(item)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["PUT"])
def updateOneItem(request, pk):
    item = Item.objects.get(pk=pk)
    serializer = ItemSerializer(item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def deleteOneItem(request, pk):
    item = Item.objects.get(pk=pk)
    item.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
