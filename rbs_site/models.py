from django.db import models

# Create your models here.
class Event(models.Model):
  event_text = models.CharField(max_length= 200)
  event_info = models.TextField()
  pub_date = models.DateTimeField('date published')

  def __str__(self):
    return self.event_text

class Going(models.Model):
  event = models.ForeignKey(Event, on_delete=models.CASCADE)
  rsvps = models.IntegerField(default = 0)