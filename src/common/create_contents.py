import os
import sys
from soffosai import SoffosAIServices
import soffosai

soffosai.api_key = "Token 0d1d8cc5-ccd5-47dc-be99-a8153def24f3"

service = SoffosAIServices.DocumentsIngestService()
_dir = "soffosai_classes/"
file = "answer_scoring.py"

answer_scoring_doc = ""



DOCUMENT_IDS = [answer_scoring_doc]



def main():
    # Check if script is run with an argument
    if len(sys.argv) > 1:
        print("Hello", sys.argv[1] + "!")
    else:
        print("Hello, World!")


if __name__ == "__main__":
    main()