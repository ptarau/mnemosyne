import streamlit as st
import os
import warnings

from deepllm.api import *
from deepllm.interactors import Agent

# Suppress FutureWarning messages
warnings.simplefilter(action='ignore', category=FutureWarning)

st.set_page_config(layout="wide")

st.title('[LLM API Chat](https://github.com/ptarau/mnemosyne)')

local = st.sidebar.checkbox('Local LLM?', value=False)

if local:

    LOCAL_PARAMS['API_BASE'] = st.sidebar.text_input('Local LLM server:', value=LOCAL_PARAMS['API_BASE'])
    local_model()
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

chat_name = st.sidebar.text_input('Chat name:', 'chat')
agent = Agent(chat_name)
agent.set_pattern(None)

spill_it = st.sidebar.button('Spill short term memory')
clear_it = st.sidebar.button('Clear all memory')

initiator = st.sidebar.text_area('question:', value='What is nothing?')

query_it = st.sidebar.button('Answer')

out = st.empty()


def show_mem(mem, key):
    if mem:
        st.subheader(key)
        for k, v in mem.items():
            st.write('*' + k + "*")
            st.write('\t' + v)


def show():
    out.empty()
    with out.container():
        show_mem(agent.short_mem, 'Short term memory:')
        show_mem(agent.long_mem, 'Long term memory:')


def pop_it():
    if agent.short_mem:
        agent.short_mem.popitem()
        agent.persist()
        show()


st.sidebar.button('Forget last interaction!', on_click=pop_it)


def do_query():
    agent.ask(initiator)
    answer_ = agent.ask(initiator)
    show()
    agent.persist()


agent.resume()
show()

if query_it:
    do_query()

if spill_it:
    agent.spill()
    agent.persist()
    show()

if clear_it:
    agent.clear()
    out.empty()
    show()
