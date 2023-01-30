# Chat GPT Code
This extension is for terminal based AI assisted programming. It takes advantage of the ChatGPT python package and has additional formatting to make it easier to use for developers.

## Installation
I'll publish a pip package soon, but for now you can install it by cloning the repo and running the following from the project's root directory.
```bash
> git clone https://github.com/BrianKmdy/ChatGPTCode.git
> cd ChatGPTCode
> pip install poetry
> poetry install
```

## Setup
Create a file called `config.json` in folder `.gptcode` in your home directory. The file should be formatted as follows, where `session_token` referers to the `__Secure-next-auth.session-token` to the browser cookie found on the chat GPT website ([see terry3041's guide for additional info](https://github.com/terry3041/pyChatGPT)):

```json
{
  "session_token": "eyJhbGciOiJkaXIiL...",
}
```

## Usage
To run the app with poetry use the following command. In order for this to work you'll need to have chrome or chromium installed. A browser instance will pop up, connect to chat GPT, and then will automatically be hidden from view.
```bash
> poetry run python -m gptcode
```

You can then ask chat GPT questions and get a response in your terminal! With nicely formatted code and easy to read output.

Thanks so much to user [acheong08](https://github.com/acheong08) for the amazing [ChatGPT Python package](https://github.com/acheong08/ChatGPT) which this is based on!