from rest_framework import serializers
from .models import Student
from classes.models import ClassLevel


class StudentSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(
        source="user.get_full_name",
        read_only=True
    )
    email = serializers.EmailField(
        source="user.email",
        read_only=True
    )
    class_level_name = serializers.CharField(
        source="class_level.name",
        read_only=True
    )

    class Meta:
        model = Student
        fields = [
            "id",
            "user",
            "full_name",
            "email",
            "roll_no",
            "degree_name",
            "enroll_date",
            "gpa",
            "credits",
            "class_level",
            "class_level_name",
            "expected_graduation",
        ]
        read_only_fields = ["id"]
