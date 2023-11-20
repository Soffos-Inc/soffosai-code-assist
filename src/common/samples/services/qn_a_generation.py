import json
from soffosai import SoffosAIServices


service = SoffosAIServices.QnAGenerationService()
output = service(
    user = "client_id",
    text = "AI and specifically NLP is a very powerful component to any application that makes it powerful, interesting and creative. However, implementing the NLP components can sometimes be hard, or very costly in cases where an NLP engineering team has to be hired to build it. Especially, since NLP keeps evolving at an absurd rate, it might be impossible for a developer to keep up with the advancements in terms of work that needs to be done or money that need to be spent to keep their NLP at a state where it can compete with similar apps out there. Here at Soffos we have packaged several high-level functionalities as modules, some of which require multiple types of NLP and complex logic, for developers to use out-of-the-box, as is, removing the need to develop it themselves. Moreover, Soffos continuously updates their modules to match the state of the art. Developers will never need to maintain any AI/NLP related component of their application. All they need is to be creative, come up with ideas, and combine our modules however they desire to come up with amazing intelligent applications.",
    sentence_overlap = True,
    sentence_split = 5
)
print(json.dumps(output, indent=4))
