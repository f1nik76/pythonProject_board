from django.contrib import admin
from .models import Feedback, Advert, AdvertFeedback, NotificationMail

# Register your models here.
admin.site.register(Feedback)
admin.site.register(Advert)
admin.site.register(AdvertFeedback)
admin.site.register(NotificationMail)