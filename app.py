import torch
import gradio as gr
from transformers import pipeline

MODEL_NAME = "openai/whisper-large-v3"
BATCH_SIZE = 8

device = 0 if torch.cuda.is_available() else "cpu"

pipe = pipeline(
    task="automatic-speech-recognition",
    model=MODEL_NAME,
    device=device,
)

def transcribe_or_translate(inputs, task):
    if inputs is None:
        raise gr.Error("No audio file submitted! Please upload or record an audio file before submitting your request.")

    text = pipe(inputs, batch_size=BATCH_SIZE, generate_kwargs={"task": task})["text"]
    return text

description="Transcribe (any language) or Translate (anything to English) with the click of a button! Demo uses `openai/whisper-large-v3` and 🤗 Transformers to transcribe/translate audio files of arbitrary length."

demo = gr.Interface(
    fn=transcribe_or_translate,
    inputs=[
        gr.Audio(type="filepath", label="Audio file"),
        gr.Radio(["transcribe", "translate"], label="Task", value="transcribe"),
    ],
    outputs=gr.Textbox(label="Output Text"),
    title="Whisper STT Sentence-To-Text and Translation",
    description=description,
    theme=gr.themes.Origin(),
    analytics_enabled=False,
    flagging_mode="never",
    clear_btn=None,
)

demo.launch(server_name="0.0.0.0")
