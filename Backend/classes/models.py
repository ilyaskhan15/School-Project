from django.db import models

class ClassLevel(models.Model):
    name = models.CharField(max_length=100)  # e.g. BSCS, Grade 10
    description = models.TextField(blank=True)

    class Meta:
        db_table = "app_class_levels"

    def __str__(self):
        return self.name


class Section(models.Model):
    class_level = models.ForeignKey(
        ClassLevel,
        on_delete=models.CASCADE,
        related_name="sections"
    )
    name = models.CharField(max_length=10)  # A, B, C

    class Meta:
        db_table = "app_sections"
        unique_together = ('class_level', 'name')

    def __str__(self):
        return f"{self.class_level.name} - {self.name}"
