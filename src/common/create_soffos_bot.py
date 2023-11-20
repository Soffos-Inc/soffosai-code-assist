import json
import soffosai
from soffosai import SoffosAIServices

soffosai.api_key = "Token 0d1d8cc5-ccd5-47dc-be99-a8153def24f3"

# output = SoffosAIServices.ChatBotCreateService.call("franco", "programmer", "Soffos Coding Assistant")
# print(output)
# 'chatbot_id': 'bce90871dfa04c5a9f2e52024754ceb7'

context = ""
# with open("bot_context.py", "r", encoding="utf-8") as source:
#     context = source.read()

# output = SoffosAIServices.DocumentsIngestService.call("franco", document_name="Soffos SDK", text=context)
# print(output)
# 'document_id': '91bfd3ec207b44a4863e632618b2f632'

# with open("README.MD", "r", encoding="utf-8") as source:
#     context = source.read()

# output = SoffosAIServices.DocumentsIngestService.call("franco", document_name="Soffos SDK", text=context)
# print(output)
# 'document_id': '76bc03de9ba74825a463add2ab3a91a8'

chatbotId = 'bce90871dfa04c5a9f2e52024754ceb7'
contextDocIds = ['91bfd3ec207b44a4863e632618b2f632', '76bc03de9ba74825a463add2ab3a91a8']
user = "Soffos Coding Assistant"
chatbot = SoffosAIServices.ChatBotService

message = "Create a python script that analyzes a text for emotions. Use the soffosai package."
output = chatbot.call(
    user=user,
    message=message,
    chatbot_id=chatbotId,
    user_id= "end_user",
    session_id="1234546354243465435",
    context_document_ids=contextDocIds,
    mode='hybrid'
)
print(json.dumps(output, indent=4))