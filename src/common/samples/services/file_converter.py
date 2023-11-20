import json
from soffosai import *

service = FileConverterService()
output = service(user="client_user_id", file="location/of/file.pdf", normalize=1)
print(json.dumps(output, indent=4))
