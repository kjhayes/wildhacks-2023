import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_personality(class_level=None):
  if class_level != None:
    class_level=" for a " + class_level
    class_level+=" level class"
  return f"""You are a class assistant {class_level}.
    Given a transcript from 
    the professor speech, come up with a relevant question about 
    the content being taught. If there is no relevant question 
    can be asked, say '0' and nothing else."""

def get_questions(prof_tscpt,class_lvl=None, temperature="0.5"):
  temperature=float(temperature)
  print(temperature)
  print(class_lvl)
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages = [
      {"role": "system", "content": generate_personality(class_lvl)},
      {"role": "user", "content": prof_tscpt}
      ],
    temperature=temperature,
    top_p=1
    )
  question = response.choices[0].message.content
  print(question)
  if question[0] == "0":
    return ""
  else:
    return question
