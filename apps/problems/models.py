from django.db import models
from django.utils import timezone

from apps.accounts import models as account_models
from apps.problems import constants as problem_constants

class Problem(models.Model):
    """
    Model to store problems
    """

    DIFFICULTY_CHOICE = [
        ('EASY', 'Easy'),
        ('MEDIUM', 'Medium'),
        ('HARD', 'Hard'),
    ]
    name = models.CharField(max_length=100, help_text="Name of Problem")
    slug = models.CharField(max_length=100, help_text="Problem slug")
    statement = models.TextField(max_length=1000, help_text="Problem statement")
    difficulty = models.CharField(choices=DIFFICULTY_CHOICE, max_length=100, help_text="Problem difficulty level")
    follow_up = models.CharField(max_length=500, help_text="Problem follow up", blank=True)
    driver_code = models.TextField(help_text="Driver Code of the problem")
    helper_function = models.TextField(help_text="Function where of the user writes logic")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class TestCase(models.Model):
    """
    Model to store testcases of problems
    """
    input = models.CharField(max_length=2000, help_text="Input")
    output = models.CharField(max_length=2000, help_text="Output")
    explaination = models.TextField(max_length=500, help_text="Explaintion of the testcase", blank=True)
    is_hidden = models.BooleanField(default=True, help_text="If the test case is visible to the user")
    problem = models.ForeignKey(Problem, help_text="The problem to which the testcase belongs", on_delete=models.CASCADE)


class Constraint(models.Model):
    """
    Model to store constrains of problems
    """
    given_constraint = models.TextField(max_length=500, help_text="Constraint for the problem")
    problem = models.ForeignKey(Problem, help_text="The problem to which the constraint belongs", on_delete=models.CASCADE)


class Tag(models.Model):
    """
    Model to store tags of problems
    """
    name = models.CharField(max_length=100, help_text="Name of the tag")
    problem = models.ForeignKey(Problem, help_text="The problem to which the testcase belongs", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Solution(models.Model):
    """
    Model to store solutions of problems
    """
    complexity_analysis = models.TextField(max_length=1000, help_text="Complexity analysis of the solution")
    explaination = models.TextField(max_length=1000, help_text="Explaintion of the solution")
    code = models.TextField(help_text="Code of the problem's solution")
    problem = models.ForeignKey(Problem, help_text="The problem to which the solution belongs", on_delete=models.CASCADE)


class Submission(models.Model):
    """
    Model to store submissions of problems
    """
    user = models.ForeignKey(account_models.User, help_text="The user which has made this submission", on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, help_text="The problem to which the submission belongs", on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        choices=problem_constants.SUBMISSION_STATUS, 
        max_length=100,
        help_text="If the submission is accepted or not"
    )
    code = models.TextField(help_text="Code of the problem's solution by the user", null=True)
    runtime = models.CharField(max_length=300, help_text="Time taken to run all the test cases")
    language_used = models.CharField(
        choices=problem_constants.PROGRAMMING_LANGUAGES_SUPPORTED, 
        max_length=200, 
        help_text="Programming language used to submit the problem"
    )
