import os
import sys
import json
import soffosai
from soffosai import SoffosAIServices


soffosai.api_key = "Token 0d1d8cc5-ccd5-47dc-be99-a8153def24f3"

service = SoffosAIServices.DocumentsIngestService()
_dir = "samples/services/"
file = "answer_scoring.py"

answer_scoring_doc = "da1b90b617d043f68fa71f394eaf9be3"



DOCUMENT_IDS = [answer_scoring_doc]

def create_meta(filename:str):
    doc_title = filename.replace("_", " ").replace(".py", "").title()
    return {"content": doc_title}

def push_to_soffos(file):
    with open(f"{_dir}{file}", "r", encoding="utf-8") as source:
        content = source.read()
    meta = create_meta(file)
    output = service('franco', meta=meta, document_name=meta['content'], text=content)
    print(json.dumps(output, indent=4))

    

def main():
    # Check if script is run with an argument
    if len(sys.argv) > 1:
        print(f"processing {sys.argv[1]}")
        push_to_soffos(sys.argv[1])
    else:
        print("file required")


if __name__ == "__main__":
    main()