import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_prompt(transcript):
  return """TAi is a college student who is watching a class 
  and have some questions about the content being taught.
  Professor: Initially, let us assume that a thermodynamically
  large system is in thermal contact with the environment,
  with a temperature T, and both the volume of the system and
  the number of constituent particles are fixed.
  TAi: What is a thermodynamically large system?
  Professor: {}
  TAi:""".format(transcript)

def get_questions(prof_tscpt: str) -> list[str]:
  try:  
      response = openai.Completion.create(
        model="text-davinci-003",
        prompt=generate_prompt(prof_tscpt),
        temperature=0.5,
        )
      return [choice.text for choice in response.choices]
  except:
      return ["Why didn't the call to OpenAI's API Work?"]
