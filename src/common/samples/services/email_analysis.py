import json
from soffosai import *


service = EmailAnalysisService()
output = service(
    user = "client_user_id",
    text="Dear John,\n\nI hope this email finds you well. I am writing to follow up on a few topics that we discussed in our last meeting on the 31st of March. There are a few updates and urgent matters that I would like to discuss with you.\n\nFirstly, I wanted to touch base on the progress of the project we discussed. As per our conversation, we had agreed on a tentative timeline to complete the project by June 15th. However, due to unforeseen circumstances, we are falling behind schedule. It is imperative that we discuss the current situation and come up with a plan to get back on track as soon as possible.\n\nSecondly, as you are aware, we had discussed the possibility of scheduling a meeting with Mary regarding the financials on the 10th of April. However, we have yet to confirm a date and time for this meeting. Given the importance of this matter, I would like to request that we schedule this meeting within the next two weeks.\n\nLastly, I would like to express my appreciation for your ongoing support and assistance in these matters. Your expertise and guidance have been invaluable, and I am confident that we will be able to overcome any challenges that come our way.\n\nGiven the urgency of these matters, I would greatly appreciate a prompt response to this email. Kind regards,\nPeter"
)
print(json.dumps(output, indent=4))
