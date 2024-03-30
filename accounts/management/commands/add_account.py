from django.conf import settings
from accounts.models import Account
from django.core.management.base import BaseCommand, CommandError

from telethon.sync import TelegramClient
from telethon.sessions.string import StringSession


class Command(BaseCommand):
    help = "Bazaga yangi akkaunt qo'shish uchun buyruq"

    def check_spam(self, app: TelegramClient):
        # spam tekshirish
        if not isinstance(app, TelegramClient):
            raise CommandError()
        if not app.is_connected():
            # why not connected?
            app.connect()
            
        username = app.get_entity("@spambot")
        app.send_message(username, "/start")
        m: list = app.get_messages(username)
        t: str = m[0].text
        keywords = ["Dear", "Hurmatli", "Здравствуйте", "Unfortunately", "Afsuski", "К сожалению"]
        return any(map(lambda x: x in t, keywords))
            
    def handle(self, *args, **options):
        try:
            API_HASH = settings.API_HASH
            API_ID = settings.API_ID
            with TelegramClient(
                StringSession(), api_hash=API_HASH, api_id=API_ID,
                device_model="Samsung S23 ultra",
                system_version="Android 14",
                system_lang_code="uz",
                app_version="10.9.2",
                lang_code="uz"
            ) as app:
                app: TelegramClient
                app.start()
                me = app.get_me()
                is_spam = self.check_spam(app)
                new_account = Account(
                    user_id=me.id,
                    first_name=me.first_name,
                    last_name=me.last_name,
                    username=me.username,
                    phone_number=app._phone,
                    is_spam=is_spam,
                    string_session=app.session.save()
                )
                new_account.save()
                self.stdout.write(
                    self.style.SUCCESS('Success: New account added: +%s' % app._phone)
                )
        except Exception as e: 
            raise CommandError('Error: "%s"' % e.with_traceback())
