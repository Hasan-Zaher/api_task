from django.urls import path
from .get_views import get_notes, get_note_detail
from .post_views import create_note
from .put_views import update_note
from .delete_views import delete_note

urlpatterns = [
    path('notes/', get_notes, name='get-notes'),
    path('notes/<int:pk>/', get_note_detail, name='get-note-detail'),
    path('notes/create/', create_note, name='create-note'),
    path('notes/<int:pk>/update/', update_note, name='update-note'),
    path('notes/<int:pk>/delete/', delete_note, name='delete-note'),
]
