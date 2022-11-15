from transcribe_streaming_mic import MicrophoneStream, RATE, CHUNK
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
import sys
import time

with open('C:\\majorproject\\Mirror\\backend\\backend\\fillers.txt') as file:
    fillers = file.read().splitlines()


class Audio(object):

    def __init__(self):
        self.summary = {
            'transcript': '',
            'crutch_count_by_line': [],
            'wpm_by_line': [],
            'counts': {}
        }
        for filler in fillers:
            self.summary['counts'][filler] = 0
    def run(self):
        # See http://g.co/cloud/speech/docs/languages
        # for a list of supported languages.
        language_code = 'en-US'  # a BCP-47 language tag

        client = speech.SpeechClient()
        config = types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=RATE,
            language_code=language_code)
        streaming_config = types.StreamingRecognitionConfig(
            config=config,
            interim_results=True)

        self.last_time = time.time()
        with MicrophoneStream(RATE, CHUNK) as stream:
            audio_generator = stream.generator()
            requests = (types.StreamingRecognizeRequest(audio_content=content)
                        for content in audio_generator)

            responses = client.streaming_recognize(streaming_config, requests)

            # Now, put the transcription responses to use.
            self.listen_print_loop(responses)

    def listen_print_loop(self, responses):
   from transcribe_streaming_mic import MicrophoneStream, RATE, CHUNK
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
import sys
import time

with open('C:\\majorproject\\Mirror\\backend\\backend\\fillers.txt') as file:
    fillers = file.read().splitlines()

