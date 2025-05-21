from django.db import models

class single_day(models.Model):
	day_date = models.DateField(auto_now_add=True)
	start_time = models.TimeField(blank=True,null=True)
	end_time = models.TimeField(blank=True,null=True)
	break_time = models.DecimalField(max_digits=4, decimal_places=2 , default=0.0)
	job_name = models.CharField(max_length = 100)
	user_notes = models.TextField(blank=True)
	day_hours = models.DecimalField(max_digits = 5, decimal_places=2, null=True, blank=True)
	
	def calculate_day_hours(self):
		if self.start_time and self.end_time:
			from datetime import datetime, timedelta

			start = datetime.combine(self.day_date,self.start_time)
			end = datetime.combine(self.day_date, self.end_time)
			raw_hours = (end - start).total_seconds()/3600
			return round(raw_hours-float(self.break_time),2)
		return None
	
	def save(self,*args,**kwargs):
		self.day_hours = self.calculate_day_hours()
		super().save(*args, **kwargs)

