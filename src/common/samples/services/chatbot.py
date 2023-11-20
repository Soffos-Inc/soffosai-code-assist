import json
from soffosai import SoffosAIServices
import soffosai

soffosai.api_key = "<your API key>"

# Create the chatbot in 2 ways:
# 2 liner:
service = SoffosAIServices.ChatBotCreateService()
output1 = service(user="franco", role="programmer", chatbot_name="francobot1")

# or 1 liner if you do not need to initialize
output2 = SoffosAIServices.ChatBotCreateService.call(user="franco", role="programmer", chatbot_name="francobot2")

print(json.dumps(output1, indent=4)) # The output will provide the chatbot_id
print(json.dumps(output2, indent=4)) # The output will provide the second chatbot_id 

# after creating the bot, you can call it by its chatbot_id. In this example, the chatbot_id is "046b5ea5691544d3b40aa70e34272b30"
service = SoffosAIServices.ChatBotService()
output = service(
    user="francoadmin",
    message="who are you?", 
    chatbot_id="046b5ea5691544d3b40aa70e34272b30", 
    user_id="franco2452561444abcdef877", 
    mode="open"
)
print(json.dumps(output, indent=4))

# This bot will reply he is francobot2 and how it can help.
# You have now created your own bot!