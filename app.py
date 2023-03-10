import os
import openai
import gradio as gr

#if you have OpenAI API key as an environment variable, enable the below
openai.api_key = os.getenv("OPENAI_API_KEY")

#if you have OpenAI API key as a string, enable the below
#openai.api_key = "*****"

system_command = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly."

messages = [
    {"role": "system", "content": system_command},
]
chat_history = []

def askbot(input, state):
    if len(messages) > 10:
        messages.pop(1)
    
    messages.append({"role": "user", "content": input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})

    chat_history.append([input, reply])
    return chat_history, state

with gr.Blocks() as block:
    gr.Markdown("""<h1><center>Sid's ChatGPT Clone</center></h1>""")
    gr.Markdown("""<h3><center>OpenAI API backend & Gradio frontend</center></h3>""")

    chatbot = gr.Chatbot()
    state = gr.State([])
    
    txt = gr.Textbox(placeholder="What do you want to discuss? ")
    submit = gr.Button("SEND")
    submit.click(askbot, [txt, state], [chatbot, state])

block.launch()