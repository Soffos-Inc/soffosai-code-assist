import json
from soffosai import *


service = SentimentAnalysisService()
output = service(
    user = "client_id",
    text = "Avocado shake tastes great!"
)
print(json.dumps(output, indent=4))
