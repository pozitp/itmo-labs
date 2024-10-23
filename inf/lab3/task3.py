import json
import re

def remove_students_with_same_initials(text, group):
    # Regular expression pattern to match students from the given group with Cyrillic support
    pattern = re.compile(r'(?<!\S)([a-zA-Zа-яА-ЯёЁ-]+)\s+([А-ЯЁ])\.\2\.\s+{}\b'.format(re.escape(group)))

    # Replace the matched students with an empty string to remove them
    filtered_text = re.sub(pattern, '', text)

    # Return the cleaned-up list without students with identical initials in the specified group
    return filtered_text.strip()

# Example usage
if __name__ == "__main__":
    input_text = input("Enter a text: ")

    input_parts = input_text.split(',')
    group_to_filter = input_parts[0].split(" ")[-1]  # Extract group from the first element

    my_json = {}
    results = []
    for part in input_parts:
        result = remove_students_with_same_initials(part.strip(), group_to_filter)
        if result:
            results.append(result)

    my_json["answers"] = results
    with open('result.json', 'w', encoding="utf-8") as file:
        dumped_json = json.dumps(my_json, ensure_ascii=False)
        file.write(dumped_json)
