import logging
from sendgrid import Mail, SendGridClient

from homeassistant.components.notify import (
    ATTR_TITLE, DOMAIN, BaseNotificationService)
from homeassistant.helpers import validate_config

REQUIREMENTS = ['sendgrid>=1.6.0,<1.7.0']
_LOGGER = logging.getLogger(__name__)


def get_service(hass, config):
    if not validate_config({DOMAIN: config},
                           {DOMAIN: ['api_key', 'sender', 'recipient']},
                           _LOGGER):
        return None

    api_key = config['api_key']
    sender = config['sender']
    recipient = config['recipient']
    return SendgridNotificationService(api_key, sender, recipient)


class SendgridNotificationService(BaseNotificationService):
    def __init__(self, api_key, sender, recipient):
        self.api_key = api_key
        self.sender = sender
        self.recipient = recipient

    def send_message(self, message='', **kwargs):
        subject = kwargs.get(ATTR_TITLE)

        sg = SendGridClient(self.api_key)
        mail = Mail(from_email=self.sender, to=self.recipient,
                    html=message, text=message, subject=subject)
        sg.send(mail)
