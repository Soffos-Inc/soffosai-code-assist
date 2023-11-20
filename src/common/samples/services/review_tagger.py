import json
from soffosai import *


service = ReviewTaggerService()
output = service(
    user = "client_id",
    text = "This oven has been a complete disaster from the start. After about 2 weeks of use, the oven and broiler burners would turn off suddenly after being on for only 5 seconds. This has been an ongoing issue for months, and it still does not work."
)
print(json.dumps(output, indent=4))
