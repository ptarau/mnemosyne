import streamlit as st
import os
import warnings
import pandas as pd

from deepllm.api import *
from deepllm.interactors import Agent

# Suppress FutureWarning messages
warnings.simplefilter(action='ignore', category=FutureWarning)

st.set_page_config(layout="wide")

st.title('[Mnemosyne](https://github.com/ptarau/mnemosyne)')
st.write('Just keep talking: [we remember it for you wholesale](https://a.co/d/hsqkMYY)! :smile:')


def to_df(d):
    data = dict((i, [False, k, v]) for (i, (k, v)) in enumerate(d.items()))
    df = pd.DataFrame.from_dict(data, orient='index',
                                columns=['Forget', 'Question', 'Answer'])
    return df


st.sidebar.image(os.path.dirname(__file__) + '/mnemosyne.jpg')

local = st.sidebar.checkbox('Local LLM?', value=False)

if local:
    IS_LOCAL_LLM[0] = True
    LOCAL_PARAMS['API_BASE'] = st.sidebar.text_input('Local LLM server:', value=LOCAL_PARAMS['API_BASE'])
else:
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        key = st.text_input("Enter your OPENAI_API_KEY:", "", type="password")
        if not key:
            # st.write('Please enter your OPENAI_API_KEY!')
            exit(0)
        else:
            set_openai_api_key(key)

    choice = st.sidebar.radio('OpenAI LLM', ['GPT-4', 'GPT-3.5'])
    if choice == 'GPT-4':
        smarter_model()
    else:
        cheaper_model()

agent = Agent('mnemosyne')
agent.set_pattern(None)

spill_it = st.sidebar.button('Spill memory')

initiator = st.sidebar.text_area('question:', value='Who is Mnemosyne?')

query_it = st.sidebar.button('Answer')


def edit_mem(mem, key):
    st.write(key)
    df = to_df(mem)
    df = st.data_editor(df, key=key)
    d = dict()
    for index, row in df.iterrows():
        if not row['Forget']:
            d[row['Question']] = row['Answer']
    return d


def refresh_state():
    agent.resume()
    agent.short_mem = edit_mem(agent.short_mem, 'Short term memory')
    agent.long_mem = edit_mem(agent.long_mem, 'Long term memory')
    agent.persist()


def do_query():
    agent.ask(initiator)
    answer = agent.ask(initiator)
    st.sidebar.write(answer)
    agent.persist()


refresh_state()

if query_it:
    do_query()

if spill_it:
    agent.spill()
    agent.persist()
