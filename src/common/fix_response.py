with open("response.py", "r") as source:
    SOURCE = source.read()

corrected_string = SOURCE.replace("\\n", "\n")

with open("corrected_response.py", "w") as target:
    target.write(corrected_string)