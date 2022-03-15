from rest_framework.serializers import ModelSerializer
from .models import Notes


class NoteSerializer (ModelSerializer):
    class Meta:
        model = Notes
        fields = "__all__"
        # fields = ["body", "updated_at", "created_at"]
