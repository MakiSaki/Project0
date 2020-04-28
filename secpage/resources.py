from tastypie.resources import ModelResource
from secpage.models import Note
class NoteResource(ModelResource):
    class Meta:
        queryset = Note.objects.all()
        resource_name = 'note'