import gradio as gr
from model import Translator
model=Translator()
interface = gr.Interface(fn=model.translate , inputs="text" , outputs = "text")
interface.launch()