import requests

from pyfibot import botcore


class BotMock(botcore.CoreCommands):
    config = {}

    def get_url(self, url, nocache=False):
        print("Getting url %s" % url)
        return requests.get(url)

    def say(self, channel, message, length=None):
        #return("%s|%s" % (channel, message))
        return (channel, message)

