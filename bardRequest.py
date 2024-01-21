import textwrap
import os
from IPython.display import Markdown
import google.generativeai as genai

my_secret = os.environ['BardSneakret']
genai.configure(api_key=my_secret)
#my_secret = os.environ['BardSneakret']
#palm.configure(api_key=my_secret)

def query(query):
#discord can only return 2000 characters or less because of the message size limit on discord.
  model = genai.GenerativeModel('gemini-pro')
  query+= "The response absolutely must be 1900 characters in length or less"
  responses = model.generate_content(query)
  
  
  text_responses = []
  for response in responses:
      print(response.text)
      text_responses.append(response.text)
  #return all of the list appended together to make one string, to the function that called it in the main function.
  if(len(text_responses) >= 1 ):
    return "".join(text_responses)
  else:
    return "Sorry, I could not find an answer to your question."
  
#def to_markdown(text):
#  text = text.replace('•', '  *')
#  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
 
