from . import chat_interface
from . import chat_gpt
from . import cli

import click

@click.command()
@click.option('--debug', is_flag=True, help='Enable debug mode')
def main(debug):
    chat_gtp = chat_gpt.ChatGPT()
    formatter = cli.Formatter()
    _cli = cli.CLI(chat_gtp, formatter, debug=debug)
    _cli.run()

if __name__ == "__main__":
    main()