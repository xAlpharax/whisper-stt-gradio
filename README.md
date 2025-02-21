# whisper-stt-gradio

Gradio Interface for Transcription and Translation using the Whisper Large V3 model for Speech-To-Text (STT) tasks. It has support for many languages, including Romanian, and offers pretty great accuracy.

## Setup

Python `3.10.14` is used for this project. You can use `pyenv` to manage the python versions (I really recommend `pyenv`, in fact I will make a guide for it). I have used CUDA version `12.4` for both my host system and container image (they must match). Below are instructions to set up the project.

```bash
pyenv install 3.10.14

pyenv virtualenv whisper-stt-gradio
pyenv activate whisper-stt-gradio

pip install -r requirements.txt

python app.py
```

Now you can open the browser and go to `http://0.0.0.0:7860/` to see the Gradio Interface with Whisper STT available to use, you can also look at the API specification for it. `Ctrl + C` to stop the server. A simple API example is found under `./test_api` in JavaScript and in Python, you will need `npm` and `node`.

```bash
cd test_api

npm install

node test_whisper_stt.js
```

or for the Python example:

```bash
cd test_api

pip install -r requirements.txt

python test_whisper_stt.py
```

## Docker

You can also run the server in a docker container. Beware that you will need to have `nvidia-container-toolkit` installed on your host system (refer to [this link](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html) to see installation instructions). Mine, on Void Linux, was installed with the following commands:

```bash
sudo xbps-install -Su nvidia-container-toolkit
```

You can build the image and then run it with the following commands:

```bash
docker build -t whisper-stt-gradio .

docker run -d --gpus all -p 7860:7860 --name whisper-stt-gradio whisper-stt-gradio

#when stopping the container
#docker stop whisper-stt-gradio

#when removing the container
#docker rm whisper-stt-gradio

#when removing the image
#docker rmi whisper-stt-gradio

#to remove everything related to docker (sometimes needed, quick reference)
#docker system prune -a --volumes --force
```

Or use docker-compose:

```bash
#to start a container
docker-compose up

#start as a daemon
#docker-compose up -d

#when stopping the container
#docker-compose down
```

Remember you can always remove the `-d` flag for debugging purposes.

**You can modify the port the application is running on by setting the PORT environment variable in `.env`.**

## Contributing

I'm actively supporting FOSS collaboration, so, if you feel like you can help in any way, file an issue in the *Issues* tab or submit a Pull Request and I will go through it.

## License

Copyright (C) xAlpharax

This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along with this program. If not, see https://www.gnu.org/licenses/.
