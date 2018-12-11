from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

class CustomUserManager(UserManager):
    pass

class Language(models.Model):
    # Representation of this language in English.
    # For example, "Japanese" or "Spanish".
    english_representation = models.CharField(max_length=100)
    
    # TODO: Add a LanguageLabel model later representing
    # languages in different languages.
    # For example, in the future, we want to be able to represent
    # English in Japanese (英語), Japanese in French (japonais), and so on.

    def __str__(self):
        return self.english_representation

    class Meta:
        ordering = ('english_representation',)

class CustomUser(AbstractUser):
    objects = CustomUserManager()
    learning_languages = models.ManyToManyField(Language, related_name="learning_users")
    fluent_languages = models.ManyToManyField(Language, related_name="fluent_users")