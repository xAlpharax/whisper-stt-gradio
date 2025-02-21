import { Client } from "@gradio/client";

const response_0 = await fetch("https://github.com/gradio-app/gradio/raw/main/test/test_files/audio_sample.wav");
const exampleAudio = await response_0.blob();

const client = await Client.connect("http://localhost:7860/");
const result = await client.predict("/predict", {
				inputs: exampleAudio,
		task: "transcribe",
});

console.log(result.data);
