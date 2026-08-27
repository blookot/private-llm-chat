# private-llm-chat
Chat UI (on Streamlit) that replaces expensive public LLMs (ChatGPT/Gemini...) for simple chat



## Requirements

This demo requires a strong Linux/Mac instance with (I would say) 12+ GB RAM. I personnaly run it on a MacBook Pro (48GB RAM)...


## Clone this repo

Open your terminal and clone this repo first:
```sh
git clone https://github.com/blookot/private-llm-chat
cd private-llm-chat
```

## Setup a local LLM

Download & install [ollama](https://github.com/ollama/ollama) for your platform.<br/>
Get the model you want. You can choose any of the models from [ollama library](https://ollama.com/library?sort=popular) that has the 'tools' tag. I personnaly use gwen3 but I also tested mistral which works great as well!

Here is an example:
```sh
ollama pull qwen3
```

Test your new LLM (setting the model to the model you chose of course, qwen3 in my example):
```sh
curl http://localhost:11434/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "qwen3",
        "messages": [
            {
                "role": "system",
                "content": "Tu es un assistant conversationnel qui parle en français uniquement et donne des réponses concises."
            },
            {
                "role": "user",
                "content": "Bonjour !"
            }
        ]
    }'
```

## Install dependencies

Install dependencies for the python program:
```sh
python -m venv .venv
source .venv/bin/activate
pip install streamlit ollama
```

## Configure

You may want to customize the model selection by taking your output of `ollama list` and insert the model names in privateChat.py


## Run

Then run the program:
```sh
streamlit run privateChat.py
```

Your web browser should open the Streamlit UI automatically. Otherwise, the UI URL is provided in the command output.

## Example

Here is an example of what it should look like:

<p align="center">
<img src="https://github.com/blookot/private-llm-chat/blob/main/chatbot.png" width="80%" alt="Chatbot screenshot"/>
</p>


## End

When you're done, simply delete the virtual env:
```sh
deactivate
rm -rf .venv
```

## Authors

* **Vincent Maury** - *Initial commit* - [blookot](https://github.com/blookot)

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE.md](LICENSE.md) file for details
