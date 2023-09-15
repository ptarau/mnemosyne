## Mnemosyne is the custodian and the live editor of your LLM's memory

#### This comes with a few consequences:

- the LLM's next answer in your chat window will depend on what you make the LLM *believe* that it answered before
- thus, you can *time travel* through the history of the chat, change what you have asked about and what was answered to
  you
- if you are a fan of movies like *Total Recall*,*Memento* or *Inception* you can see how the LLM's view of *reality* is
  distorted by letting *Mnemosyne* play with its memory

#### Other features that simply manage your chat context:

- if you asked the same question again, the answer will be retrieved from the short term or long term memory at no API
  cost to you
- when you get close to the token limit, the oldest item in the short term memory is moved to the long-term memory
- when changing the subject of your chat you can spill all the content of the short-term memory into the long-term
  memory
- if you run an LLM using the same API as OpenAI (e.g., **Vicuna**) listening on a local port, Mnemosyne can also manage
  your interaction with it

### Installation

#### First, you will need to acquire your OpenAI key from [here](https://openai.com/).

If you have cloned this repo, you can install the package ```memesis``` from its folder with:

```
pip3 install -e .
```

and then run it with:

```
./run.sh
```

You can also install it from [pypi](https://pypi.org/search/?q=memesis) with:

```
pip3 install memesis
```

and then run it with:

```
python -m memesis.run
```

#### Soon, you can also try out at: https://mnemosyne.streamlit.app/

***Enjoy***,

Paul Tarau
