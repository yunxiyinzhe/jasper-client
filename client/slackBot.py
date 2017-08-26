# -*- coding: utf-8-*-

import json
import urllib
import urllib2
import threading
import logging
from slackbot.bot import Bot

class Slackbot:

    def __init__(self, url):
        self._logger = logging.getLogger(__name__)
        self._url = url # https://hooks.slack.com/services/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

    def request(self, text = None):
        try:
            # https://dylangao.slack.com/apps/new/A0F7XDUAZ-incoming-webhooks
            url = self._url
            values = {"text": text}
            data = json.JSONEncoder().encode(values)

            user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
            headers = {'User-Agent' : user_agent, 'Content-type':"application/json"}
            req = urllib2.Request(url, data=data, headers=headers)
            res_data = urllib2.urlopen(req)
            res = res_data.read()

            if res_data.getcode() == 200:
                return res
        except urllib2.HTTPError, err:
            self._logger.error("Error code is :" + str(err.code))
            self._logger.error(err.read())
            raise

    def sendMessage(self, text):
        if(self._url == ""):
            return
        args = {'text': text}
        t = threading.Thread(target=self.request, kwargs=args)
        t.start()

    def startBot(self):
        t = threading.Thread(target=self.run)
        t.start()


    def run(self):
        bot = Bot()
        bot.run()

from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re

@respond_to('send', re.IGNORECASE)
def home(message):
    message.reply("reply")