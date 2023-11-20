import json
from soffosai import *


service = TranscriptCorrectionService()
output = service(
    user = "client_id",
    text = " We just want to show people or services can't help them. Create amazing. Applications"
)
print(json.dumps(output, indent=4))
