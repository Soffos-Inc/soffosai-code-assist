import json
from soffosai import SoffosAIServices

service = SoffosAIServices.TranslationService()
output = service("client identity - any string", "Bakit ang guwapo ko?", False, 'fil', 'en')
print(json.dumps(output, indent=4))
