from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note

@api_view(['DELETE'])
def delete_note(request, pk):
    try:
        note = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        return Response({'error': 'Note not found'}, status=404)
    note.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
