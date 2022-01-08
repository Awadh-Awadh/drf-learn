from django.db import models
from helpers.models import TrackingModel
from django.contrib.auth import get_user_model

class Todo(TrackingModel):
  title = models.CharField(max_length=255)
  desc = models.TextField()
  is_complete = models.BooleanField(default=False)
  owner = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)

  def __str__(self) -> str:
      return self.title