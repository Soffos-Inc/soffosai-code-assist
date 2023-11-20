'''
Answer Scoring module sample
'''

import json
import soffosai
from soffosai import SoffosAIServices

soffosai.api_key = "<your api key>"
service = SoffosAIServices.AnswerScoringService()
output = service(
    user = "client_user_id",
    context="Genetic evidence suggests that dogs descended directly from wolves (Canis) and that the now-extinct wolf lineages that produced dogs branched off from the line that produced modern living wolves sometime between 27,000 and 40,000 years ago. The timing and location of dog domestication is a matter of debate. There is strong genetic evidence, however, that the first domestication events occurred somewhere in northern Eurasia between 14,000 and 29,000 years ago.",
    question="How long ago did dogs first become domesticated?",
    user_answer="around 20,000 years ago.",
    answer="Between 14,000 and 29,000 years ago."
)
print(json.dumps(output, indent=4))

# Returns:
'''
{
    "score": 0.8,
    "reasoning": "The user's answer is close to the correct answer, but not exact. The correct answer states that dogs were first domesticated between 14,000 and 29,000 years ago, while the user's answer is \"around 20,000 years ago.\" Although the user's answer falls within the correct range, it is not as precise as the correct answer.",     
    "cost": {
        "api_call_cost": 0.005,
        "character_volume_cost": 0.02855,
        "total_cost": 0.03355
    },
    "charged_character_count": 571,
    "unit_price": "0.000050"
}
'''