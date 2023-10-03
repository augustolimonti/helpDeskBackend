from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from tickets.models import Ticket
from .serializers import TicketSerializer

@api_view(['GET'])
def getData(request):
    tickets = Ticket.objects.all()
    serializer = TicketSerializer(tickets, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addTicket(request):
    serializer = TicketSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteTicket(request, ticket_id):
    try:
        ticket = Ticket.objects.get(id=ticket_id)
    except Ticket.DoesNotExist:
        return Response({'error': 'Ticket not found.'}, status=status.HTTP_404_NOT_FOUND)

    ticket.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PATCH'])
def updateStatus(request, ticket_id):
    try:
        ticket = Ticket.objects.get(id=ticket_id)
    except Ticket.DoesNotExist:
        return Response({'error': 'Ticket not found.'}, status=status.HTTP_404_NOT_FOUND)

    if 'status' not in request.data:
        return Response({'error': 'Status field is required.'}, status=status.HTTP_400_BAD_REQUEST)

    new_status = request.data['status']
    if new_status not in dict(Ticket.STATUS_CHOICES):
        return Response({'error': 'Invalid status value.'}, status=status.HTTP_400_BAD_REQUEST)

    ticket.status = new_status
    ticket.save()
    serializer = TicketSerializer(ticket)
    return Response(serializer.data, status=status.HTTP_200_OK)
