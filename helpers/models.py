from django.db import models

'''
A model to be reused by all other models

'''

class TrackingModel(models.Model):
  created_at=models.DateTimeField(auto_now_add=True)
  updated_at=models.DateTimeField(auto_now=True)

  class Meta:
    '''
    Abstract=True means this is just a reference class and not to be used to create object
    '''
    abstract=True
    ordering = '-created_at'