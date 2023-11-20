import json
from soffosai import *


service = QuestionAnsweringService()
output = service(
    user = "client_id",
    question = "What is the topic?",
    document_text = "The James Webb Space Telescope is the largest, most powerful space telescope ever built. It will allow scientists to look at what our universe was like about 200 million years after the Big Bang. The telescope will be able to capture images of some of the first galaxies ever formed. It will also be able to observe objects in our solar system from Mars outward, look inside dust clouds to see where new stars and planets are forming and examine the atmospheres of planets orbiting other stars.",
)
print(json.dumps(output, indent=4))
