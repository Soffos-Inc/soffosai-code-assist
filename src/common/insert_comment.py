import os

# Directory where the classes are
dir_path = r'soffosai_classes'

# The comment to insert
triple_quote = "'''"
comment = triple_quote + "\n Before using a SoffosAIService into a SoffosPipeline, you must setup the service's input configuration.\n" + triple_quote

# Iterate over all files in the directory
for filename in os.listdir(dir_path):
    if filename.endswith('.py'):
        file_path = os.path.join(dir_path, filename)

        # Read the file
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Look for the required line and insert the comment
        for i in range(len(lines)):
            line = lines[i]

            if 'super().set_input_configs' in line:
                lines[i] = comment + line

        # Write the file back
        with open(file_path, 'w') as file:
            file.writelines(lines)