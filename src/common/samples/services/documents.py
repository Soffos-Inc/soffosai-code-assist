import json
from soffosai import *


# To ingest text/context:
output = DocumentsIngestService.call(
    user = "client_user_id",
    document_name='dogs',
    text="Genetic evidence suggests that dogs descended directly from wolves (Canis) and that the now-extinct wolf lineages that produced dogs branched off from the line that produced modern living wolves sometime between 27,000 and 40,000 years ago. The timing and location of dog domestication is a matter of debate. There is strong genetic evidence, however, that the first domestication events occurred somewhere in northern Eurasia between 14,000 and 29,000 years ago.",
)
print(json.dumps(output, indent=4))

# To get the text/context referenced by a docuement_id.  There are more options here, hover on the method to
# see optional arguments
output = DocumentsSearchService.call(user="client_user_id", document_ids=['the_document_id_of_ingested_context'])
print(json.dumps(output, indent=4))

# To delete an ingested content to free up your Soffos storage
output = DocumentsDeleteService.call(user="client_user_id", document_ids=['the_document_id_of_ingested_context'])
print(json.dumps(output, indent=4))
