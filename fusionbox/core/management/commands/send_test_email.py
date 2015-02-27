import socket, datetime

from django.core.management.base import BaseCommand, CommandError
from django.core.mail import send_mail

class Command(BaseCommand):
    help = "Sends an email through the framework to an address specified on the command line."
    args = "<email email...>"

    def handle(self, *args, **kwargs):
        if not args:
            raise CommandError('You must provide at least one destination email')
        send_mail(
                subject='Test email from %s on %s' % (socket.gethostname(), datetime.datetime.now()),
                message='If you\'re reading this, it was successful.',
                from_email=None,
                recipient_list=args,
        )
