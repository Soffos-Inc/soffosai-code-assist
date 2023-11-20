import json
from soffosai import *


service = TableGeneratorService()
output = service(
    user = "client_id",
    text = "Demographic and socioeconomic factors can contribute to community spread of COVID-19. The aim of this study is to describe the demographics and socioeconomic factors in relation to geolocation of COVID-19 patients who were discharged from the emergency department (ED) back into the community...",
    table_format = 'markdown'
)
print(json.dumps(output, indent=4))
