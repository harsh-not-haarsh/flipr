from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save


class UserProfile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # personal_board = models.ForeignKey(PersonalBoard, on_delete=models.CASCADE)
    # team_boards = models.ManyToManyField(TeamBoards, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name

# def pre_save_user_profile(sender, instance, **kwargs):
#     if instance._state.adding is True:
#         instance.personal_board = PersonalBoard.objects.create()



# pre_save.connect(pre_save_user_profile, sender=UserProfile)
