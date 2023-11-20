import json
import soffosai
from soffosai import SoffosAIServices

soffosai.api_key = "Token 0d1d8cc5-ccd5-47dc-be99-a8153def24f3"
SoffosAIServices.AnswerScoringService
service = SoffosAIServices.ChatBotService()
chatbot_id = 'bce90871dfa04c5a9f2e52024754ceb7'
document_ids = ["da1b90b617d043f68fa71f394eaf9be3"]

output = service(
    "franco", 
    "How to create a soffos ai service that scores an answer? Use Soffos AI's SDK.",
    chatbot_id=chatbot_id,
    user_id="franco such",
    context_document_ids=document_ids,
    mode="hybrid",
    session_id="1234abcdef"
    )
print(json.dumps(output, indent=4))
