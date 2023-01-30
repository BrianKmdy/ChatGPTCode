from . import chat_interface

from termcolor import colored
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import TerminalFormatter
import traceback

class Formatter:
    def __init__(self):
        self.formatter = TerminalFormatter()

    def render_markdown(self, text):
        return(highlight(text, get_lexer_by_name("markdown"), self.formatter))


class CLI:
    def __init__(self, chat_interface, formatter, debug=False):
        self.debug = debug
        self.chat_interface = chat_interface
        self.formatter = formatter
        self.counter = 1
        self.connected = False

    def print_intro(self):
        print(f'\nWelcome to {colored("ChatGPT", "blue")} Code!')
        print(f'Press {colored("<Ctrl-C>", "dark_grey")} to exit\n')

    def get_question(self):
        return input(colored(f'[{self.counter}] ', 'blue'))

    def get_response(self, question):
        return self.chat_interface.ask(question)

    def print_response(self, response):
        print(
            f'{colored("-> ", "blue")}'
            f'{self.formatter.render_markdown(response.strip())}'
        )

    def print_divider(self):
        print('')

    def print_exit(self):
        if self.connected:
            print(f'\n{colored("[Session terminated]", "dark_grey")}')

    def run(self):
        self.print_intro()
        try:
            self.chat_interface.connect()
            self.connected = True

            print('')
            while True:
                question = self.get_question()
                print(f'{colored("[Waiting for response]", "dark_grey")}\n')
                self.print_response(self.get_response(question))
                self.print_divider()
                self.counter += 1
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(f'{colored("[Error encountered]", "red")} {e}')

            if self.debug:
                print(f'\n{colored(traceback.format_exc(), "dark_grey")}')
            else:
                print(colored('Run with --debug to see the full stack trace', 'dark_grey'))

        self.print_exit()