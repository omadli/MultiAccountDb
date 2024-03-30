from __future__ import annotations
from django.db import models

# Create your models here.
class Account(models.Model):
    id = models.AutoField(primary_key=True)
    folder = models.PositiveIntegerField(
        verbose_name="Papka",
        default=1,
        help_text="Papkasi"
    )
    user_id = models.PositiveBigIntegerField(
        blank=False, null=False,
        db_index=True,
        help_text="Telegram user_id"
    )
    first_name = models.CharField(
        max_length=255,
        blank=False, null=False,
        help_text="Akkaunt nomi first_name"
    )
    last_name = models.CharField(
        max_length=255,
        blank=True, null=True,
        help_text="Akkaunt nomi last_name"
    )
    username = models.CharField(
        max_length=255,
        null=True, blank=True,
        help_text="Akkaunt @username"
    )
    phone_number = models.PositiveBigIntegerField(
        blank=False, null=False,
        help_text="Akkaunt telefon raqami"
    )
    is_spam = models.BooleanField(
        blank=False, null=False,
        default=False,
        help_text="Spam bo'lganmi yo'qmi"
    )
    string_session = models.TextField(
        blank=False, null=False,
        help_text="Telethon uchun string session"
    )
    
    def __str__(self) -> str:
        return f"+{self.phone_number}: {self.user_id}: {self.first_name}"
    
    class Meta:
        db_table = "accounts"
        verbose_name = "Akkaunt "
        verbose_name_plural = "Akkauntlar"
        
    groups: models.QuerySet[Group]
    channels: models.QuerySet[Channel]


class Group(models.Model):
    id = models.AutoField(primary_key=True)
    chat_id = models.BigIntegerField(
        null=False, blank=False,
        help_text="Guruhning telegram chat_id raqami"
    )
    name = models.CharField(
        max_length=255,
        null=False, blank=False,
        help_text="Guruh nomi"
    )
    invite_link = models.CharField(
        max_length=255,
        null=False, blank=False,
        help_text="Guruh linki qo'shilish uchun"
    )
    created_at=models.DateTimeField(
        null=False, blank=False,
        db_index=True,
        help_text="Guruh ochilgan vaqt"
    )
    creator = models.ForeignKey(
        to=Account,
        on_delete=models.CASCADE,
        related_name='groups',
        db_index=True,
        null=False, blank=False,
        help_text="Guruhni ochgan akkaunt"
    )

    def __str__(self) -> str:
        return f"{self.chat_id}: {self.name}"
    
    class Meta:
        db_table = "groups"
        verbose_name = "Guruh "
        verbose_name_plural = "Guruhlar"


class Channel(models.Model):
    id = models.AutoField(primary_key=True)
    chat_id = models.BigIntegerField(
        null=False, blank=False,
        help_text="Kanalning telegram chat_id raqami"
    )
    name = models.CharField(
        max_length=255,
        null=False, blank=False,
        help_text="Kanal nomi"
    )
    invite_link = models.CharField(
        max_length=255,
        null=False, blank=False,
        help_text="Kanal linki qo'shilish uchun"
    )
    created_at=models.DateTimeField(
        null=False, blank=False,
        db_index=True,
        help_text="Kanal ochilgan vaqt"
    )
    creator = models.ForeignKey(
        to=Account,
        on_delete=models.CASCADE,
        related_name='channels',
        db_index=True,
        null=False, blank=False,
        help_text="Kanalni ochgan akkaunt"
    )

    def __str__(self) -> str:
        return f"{self.chat_id}: {self.name}"
    
    class Meta:
        db_table = "channels"
        verbose_name = "Kanal "
        verbose_name_plural = "Kanallar"
