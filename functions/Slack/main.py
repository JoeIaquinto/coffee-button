import os
import requests
import pytz
import datetime
import random
from enum import Enum


class ButtonClickType(Enum):
    """An enumeration for the IoT button states."""

    def __str__(self):
        return str(self.value)

    Single = 'SINGLE'
    Double = 'DOUBLE'
    Long = 'LONG'


def handle(event, context):
    """Publishes a message to the configured Slack channel when and
    Amazon IoT button is pressed.

    Arguments:
      event (dict): Data passed to the handler by Amazon Lambda
      context (LambdaContext): Provides runtime information to the handler
    """
    slack_webhook_url = os.environ['COFFEE_BUTTON_SLACK_WEBHOOK_URL']
    slack_channel = os.environ['COFFEE_BUTTON_SLACK_CHANNEL']

    if event['clickType'] == str(ButtonClickType.Single):
        now = datetime.datetime.now(tz=pytz.timezone('US/Eastern'))
        ready_datetime = now + datetime.timedelta(minutes=90)
        ready_time = ready_datetime.strftime('%l:%M%p').lower().strip()
        msg = ['Becky has been walked.', 'The bitch got walked.', 'Becky got a walkie', 'BECKERONI IS WALKERONI', 'Doggo Walko']
        r = random.randint(0,len(msg))
        requests.post(slack_webhook_url, json={
            'text': '{} Next time you should walk her is around {}.'.format(msg,ready_time),  # NOQA
            'channel': slack_channel})

    if event['clickType'] == str(ButtonClickType.Double):
        msg = ['Becky has been fed.', 'The bitch got fed.', 'Becky got her din din.', 'BECKERONI IS EATERONI', 'Dinnah Dog']
        r = random.randint(0,len(msg))
        requests.post(slack_webhook_url, json={
            'text': msg[r],  # NOQA
            'channel': slack_channel})

    if event['clickType'] == str(ButtonClickType.Long):
        requests.post(slack_webhook_url, json={
            'text': 'Someone take care of little Beckeroni',
            'channel': slack_channel})
