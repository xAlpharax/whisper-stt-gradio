from gradio_client import Client, handle_file

client = Client("http://localhost:7860/")

result = client.predict(
    inputs=handle_file('https://github.com/gradio-app/gradio/raw/main/test/test_files/audio_sample.wav'),
    task="transcribe",
    api_name="/predict"
)

print(result)
