import json
from soffosai import *

service = LanguageDetectionService()
output = service("client_user_id", "φιλόσοφος, που θεωρείται ο ιδρυτής της Δυτικής φιλοσοφίας και")
print(json.dumps(output, indent=4))
