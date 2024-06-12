from ollama import Client
import time

client = Client(host='ollama')

prompt = """
Audio Transcription Input Data:
---
{{
   "segments":[
  	{{
     	"start": "2024-05-25 18:09:06.96",
     	"end": "2024-05-25 18:09:08.68",
     	"text": "Stability now is change."
  	}},
  	{{
     	"start": "2024-05-25 18:09:08.68",
     	"end": "2024-05-25 18:09:14.60",
     	"text": "It's strange to say that in 2024, but a stable economy has to be the first step of an incoming Labour government."
  	}},
  	{{
     	"start": "2024-05-25 18:09:15.32",
     	"end": "2024-05-25 18:09:20.84",
     	"text": " and that is what we'll make an absolute priority if we're privileged enough to come in to serve."
  	}},
  	{{
     	"start": "2024-05-25 18:09:22.96",
     	"end": "2024-05-25 18:09:31.88",
     	"text": " Visiting a supermarket in London, the woman who's pitching to be in charge of the public finances, Rachel Reeves, promised she would never play fast and loose with taxpayers' money."
  	}},
  	{{
     	"start": "2024-05-25 18:09:32.52",
     	"end": "2024-05-25 18:09:39.64",
     	"text": "All parties received a warning from the Independent Institute for Fiscal Studies today to be open with voters about the economic challenges ahead."
  	}}
   ]
}}
---
Here is the definition of the data:

{{
    "segments": [
   	 {{
   		 "start": <Start time of the segment>,
   		 "end": <End time of the segment>,
   		 "text": <Actual text of that segment>
   	 }}
    ]
}}

Your task is to identify unique topics from the segments array and produce results in the given JSON format. Not necessarily each segment would be a unique topic, a topic might contain multiple items from the segments array.
Do not generate any code or don't provide any concept of doing this.

REQUIRED JSON FORMAT:
---
[
    {{
   	 "topic_id": <incremental id>,
   	 "topic_name": <unique identifier that describes the topic>,
   	 "concatenated_text": <concatenated text of each topic segment>
   	 "topic_summary": <short description of the topic>,
   	 "position_in_segments_array": <position of segments in segments array. Example: [0, 1, 2]>
    }}
]
---

REMEMBER ONLY ANSWER IN THE GIVEN JSON FORMAT. NOTHING MORE.
"""

print("Generating output for the prompt: \n", prompt)

start_time = time.perf_counter()

response = client.generate(model='llama2', prompt=prompt)

end_time = time.perf_counter()

actual_response = response["response"]

print("\n Actual Response: \n", actual_response)
print("\n Total Duration: \n", end_time - start_time, "seconds")
