import os
import requests
import google.generativeai as palm
import json
from vertexai.preview import generative_models
palm.configure(api_key=os.environ['BardSneakret'])
#from vertexai.preview import generative_models

#your individual API Key goes where "BardSneakret" is. Do this by creating a secret on replit and putting your Bard API key in it.
my_secret = os.environ['BardSneakret']
palm.configure(api_key=my_secret)

def query(query):
#discord can only return 2000 characters or less because of the message size limit on discord. So whatever the currently listed query is, ask it to do that in 2k characters or less
  query+= "In 2000 characters or less, please"
  
  #list the generative model parameters
  model = palm.GenerativeModel(model_name="gemini-pro",
                                #generation_config=generation_config,
                                 #safety_settings=safety_config
                              )
    
  #uses the model, without typing out the characters one at a time, uses default safety settings, and establishes temperature (the amount of stuff the AI can make up)  
  responses = model.generate_content(
                                     [query],
                                     stream=False,
                                     #safety_settings=safety_config,
                                     generation_config={"max_output_tokens": 2048, "temperature": 1.0} )

  #create a list of all of the strings Bard is sending over. print each to console so the admin can see what the bot is doing. append it to a response 
  text_responses = []
  for response in responses:
      print(response.text)
      text_responses.append(response.text)
  #return all of the list appended together to make one string, to the function that called it in the main function.
  return "".join(text_responses)
 
