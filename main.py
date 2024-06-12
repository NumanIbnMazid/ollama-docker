from ollama import Client
import time

client = Client(host='ollama-demo')

prompt = """
Audio Transcription Input Data:
---
{{
   "segments":[
      {{
         "start":"2024-05-25 20:15:56.16",
         "end":"2024-05-25 20:15:57.16",
         "text":" Lauren, hello to you once again."
      }},
      {{
         "start":"2024-05-25 20:15:57.24",
         "end":"2024-05-25 20:16:07.44",
         "text":"Manchester United have won the English FA Cup, beating rivals Manchester City 2-1 at Wembley in a match that many had billed as Eric Ten Haag's last in charge of United."
      }},
      {{
         "start":"2024-05-25 20:16:07.52",
         "end":"2024-05-25 20:16:21.04",
         "text":"As rumours swirled that the manager might be sacked, regardless of the result, his team produced a shock against the Premier League champions, Alejandro Garnaccio taking advantage of a mistake to score the first, which another teenager, Kobi Meinu, added "
      }},
      {{
         "start":"2024-05-25 20:16:21.04",
         "end":"2024-05-25 20:16:25.60",
         "text":"Manchester City were attempting to win a historic second league and cup double in a row, but even"
      }},
      {{
         "start":"2024-05-25 20:16:25.64",
         "end":"2024-05-25 20:16:27.20",
         "text":" though Jeremy Docku scored late on."
      }},
      {{
         "start":"2024-05-25 20:16:27.8",
         "end":"2024-05-25 20:16:36.92",
         "text":"United held on for a victory that is a 13th FA Cup, a place in Europe, and also it means a trophy in each of Ten Hag's two seasons as boss."
      }},
      {{
         "start":"2024-05-25 20:16:38.84",
         "end":"2024-05-25 20:16:41.08",
         "text":" The team is progressing and we're winning trophies."
      }},
      {{
         "start":"2024-05-25 20:16:41.84",
         "end":"2024-05-25 20:16:44.60",
         "text":"Two trophies in two years is not bad."
      }},
      {{
         "start":"2024-05-25 20:16:44.84",
         "end":"2024-05-25 20:16:46.36",
         "text":"Three finals is not bad."
      }},
      {{
         "start":"2024-05-25 20:16:47.24",
         "end":"2024-05-25 20:16:49.24",
         "text":"But we have to keep going."
      }},
      {{
         "start":"2024-05-25 20:16:49.92",
         "end":"2024-05-25 20:16:50.84",
         "text":"I'm not satisfied with it."
      }},
      {{
         "start":"2024-05-25 20:16:51.28",
         "end":"2024-05-25 20:16:51.92",
         "text":"We have to do better."
      }},
      {{
         "start":"2024-05-25 20:16:52.08",
         "end":"2024-05-25 20:16:55.32",
         "text":"And if they don't want me anymore, then I go anywhere else to win trophies."
      }},
      {{
         "start":"2024-05-25 20:16:56",
         "end":"2024-05-25 20:16:57.24",
         "text":" but I did my whole career."
      }},
      {{
         "start":"2024-05-25 20:16:58.48",
         "end":"2024-05-25 20:17:03.48",
         "text":"So while Manchester City couldn't claim a double, Celtic did by winning the Scottish Cup final."
      }},
      {{
         "start":"2024-05-25 20:17:03.52",
         "end":"2024-05-25 20:17:07.76",
         "text":"They too beating their rivals Rangers in an old firm derby at Hampden Park."
      }},
      {{
         "start":"2024-05-25 20:17:07.8",
         "end":"2024-05-25 20:17:12.12",
         "text":"It took until the 90th minute for the only goal of the game to arrive."
      }},
      {{
         "start":"2024-05-25 20:17:12.24",
         "end":"2024-05-25 20:17:20.64",
         "text":"Adam Ida pouncing on an error by Rangers goalkeeper Jack Button to give Celtic yet another trophy, claiming the Scottish Cup for a record-extending 42nd time."
      }},
      {{
         "start":"2024-05-25 20:17:23.12",
         "end":"2024-05-25 20:17:23.68",
         "text":" elsewhere in Europe."
      },
      {{
         "start":"2024-05-25 20:17:23.76",
         "end":"2024-05-25 20:17:26.32",
         "text":"Bayer Leverkusen have completed their domestic double."
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

YOUR TASK: Identify unique topics from the provided JSON segments array and provide the output in the following JSON structure, ensuring that no topic is missed from the first one.
REQUIRED JSON FORMAT:
---
[
    {{
		"topic_id": <incremental id>,
		"topic_name": <unique identifier that describes the topic>,
		"concatenated_text": <concatenated text of each topic segment>
		"start_text": <entire first text of the topic>,
		"end_text": <entire last text of the topic>
		"start_text_start_time": <start time of the first text of the topic>
		"end_text_start_time": <start time of the last text of the topic>
    }}
]
---
"""

print("Generating output for the prompt: \n", prompt)

start_time = time.perf_counter()

response = client.generate(model='llama2', prompt=prompt)

end_time = time.perf_counter()

actual_response = response["response"]

print("\n Actual Response: \n", actual_response)
print("\n Response Length: \n", len(actual_response))
print("\n Total Duration: \n", end_time - start_time, "seconds")

# ollama-app  |  Response Length: 
# ollama-app  |  1987
# ollama-app  | 
# ollama-app  |  Total Duration: 
# ollama-app  |  59.86781556999995 seconds
