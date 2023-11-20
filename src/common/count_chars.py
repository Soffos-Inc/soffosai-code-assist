def count_characters(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        return len(content)

file_path = "bot_context.py"  # Replace with your file path
print(f"The total number of characters is: {count_characters(file_path)}")