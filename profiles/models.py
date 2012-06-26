from django.db import models
from signup.models import Publisher
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    publisher = models.ForeignKey(Publisher)
    def __unicode__)self):
        return "%s: %s" % (self.user.get_full_name(), self.publisher.name)
"""
class PublisherAdmin(admin.ModelAdmin):
    #stuff here??

    def queryset(self, request):
        if request.user.is_superuser:
            return Model.objects.all()
        return Model.objects.filter(edition=request.user.get_profile().fieldnameicreate

"""
