from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Student
from .serializers import StudentSerializer
from .permissions import IsAdmin


class StudentViewSet(ModelViewSet):
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        # ✅ ADMIN → SEE ALL STUDENTS (NO FILTERING AT ALL)
        if user.is_staff or user.is_superuser:
            return Student.objects.select_related("user", "class_level")

        # ✅ STUDENT → SEE ONLY OWN RECORD
        return Student.objects.filter(user=user).select_related(
            "user", "class_level"
        )

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAdmin()]
        return [IsAuthenticated()]
