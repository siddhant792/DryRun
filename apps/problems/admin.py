from django.contrib import admin
from apps.problems import models as problem_models


@admin.register(problem_models.Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ("name", "id", "slug")
    search_fields = ("name", "slug")


@admin.register(problem_models.TestCase)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ("id", "input")
    raw_id_fields = ("problem", )
    

@admin.register(problem_models.Constraint)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ("id", "given_constraint")
    raw_id_fields = ("problem", )


@admin.register(problem_models.Tag)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    raw_id_fields = ("problem", )


@admin.register(problem_models.Solution)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ("id", "problem")
    raw_id_fields = ("problem", )


@admin.register(problem_models.Submission)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "problem", "status")
    raw_id_fields = ("problem", "user")