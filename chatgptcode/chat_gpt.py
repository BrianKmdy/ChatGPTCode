from . import chat_interface

from revChatGPT.ChatGPT import Chatbot
import os
import json

class ChatGPT(chat_interface.ChatInterface):
    CONFIG_PATH = os.path.join(os.path.expanduser('~'), '.gptcode', 'config.json')

    def __init__(self, conversation_id=None, parent_id=None):
        super().__init__()

        with open(self.CONFIG_PATH, 'r') as f:
            config = json.load(f)
            self.session_token = config['session_token']

        # To possibly use in the future
        self.conversation_id = None
        self.parent_id = None

    def connect(self):
        self.chatbot = Chatbot({
            "session_token": self.session_token
        }, conversation_id=None, parent_id=None)

    def ask(self, prompt):
        response = self.chatbot.ask(prompt, conversation_id=None, parent_id=None)
        self.conversation_id = response['conversation_id']
        self.parent_id = response['parent_id']
        return response['message']