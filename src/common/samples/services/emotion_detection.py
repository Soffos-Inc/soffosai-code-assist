import json
from soffosai import *


service = EmotionDetectionService()
output = service(
    user = "client_id", 
    text = "On my birthday I got up in the morning with a sad face. I went down to have my breakfast after a long time and as I went down the stairs, I saw all my friends, cousins and my grandparents there. They all wished me \"Happy Birthday\" and I was shocked, surprised, and very happy. Trust me on this, nothing makes you gladder than seeing all your favourite people together. It was one of the best birthdays that I ever had.",
    emotion_choices= ["joy", "surprise", "sadness"]
)
print(json.dumps(output, indent=4))
