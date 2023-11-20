import json
from soffosai import *


service = SimplifyService()
output = service(
    user = "client_id", 
    text = "During mitosis, a cell duplicates all of its contents, including its chromosomes, and splits to form two identical daughter cells. Because this process is so critical, the steps of mitosis are carefully controlled by certain genes. When mitosis is not regulated correctly, health problems such as cancer can result."
)
print(json.dumps(output, indent=4))
