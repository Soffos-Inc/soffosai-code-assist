import json
from soffosai import *


service = MicrolessonService()
output = service(
    user = "client_user_id",
    content=[
        {
            "source": "Telescope.docx",
            "text": "The James Webb Space Telescope is the largest, most powerful space telescope ever built. It will allow scientists to look at what our universe was like about 200 million years after the Big Bang. The telescope will be able to capture images of some of the first galaxies ever formed. It will also be able to observe objects in our solar system from Mars outward, look inside dust clouds to see where new stars and planets are forming and examine the atmospheres of planets orbiting other stars."
        },
        {
            "source": "dogs.docx",
            "text": "Genetic evidence suggests that dogs descended directly from wolves (Canis) and that the now-extinct wolf lineages that produced dogs branched off from the line that produced modern living wolves sometime between 27,000 and 40,000 years ago. The timing and location of dog domestication is a matter of debate. There is strong genetic evidence, however, that the first domestication events occurred somewhere in northern Eurasia between 14,000 and 29,000 years ago.",
        }
    ]
)
print(json.dumps(output, indent=4))

# Content can also be added like this:
service.add_content(
    source = "Telescope.docx",
    text = "The James Webb Space Telescope is the largest, most powerful space telescope ever built. It will allow scientists to look at what our universe was like about 200 million years after the Big Bang. The telescope will be able to capture images of some of the first galaxies ever formed. It will also be able to observe objects in our solar system from Mars outward, look inside dust clouds to see where new stars and planets are forming and examine the atmospheres of planets orbiting other stars."
)
service.add_content(
    source = "dogs.docx",
    text = "Genetic evidence suggests that dogs descended directly from wolves (Canis) and that the now-extinct wolf lineages that produced dogs branched off from the line that produced modern living wolves sometime between 27,000 and 40,000 years ago. The timing and location of dog domestication is a matter of debate. There is strong genetic evidence, however, that the first domestication events occurred somewhere in northern Eurasia between 14,000 and 29,000 years ago.",
)
output = service(user="client_user_id")
print(json.dumps(output, indent=4))

