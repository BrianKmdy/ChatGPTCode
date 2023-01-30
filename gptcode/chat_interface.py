from abc import ABC, abstractmethod

class ChatInterface(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def ask(self, prompt):
        pass