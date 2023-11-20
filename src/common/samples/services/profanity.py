import json
from soffosai import *


service = ProfanityService()
output = service(
    user = "client_id",
    text = "Your look like shit on your shirt! Fucking go home and change."
)
print(json.dumps(output, indent=4))
