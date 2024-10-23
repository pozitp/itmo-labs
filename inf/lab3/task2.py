import re
import json

def remove_repeated_words(text):
    pattern = re.compile(r'([А-Яа-яA-Za-z0-9]+(?:[.,!?;]*[А-Яа-яA-Za-z0-9]*)*)(\s+\1)+', re.IGNORECASE)
    result = pattern.sub(r'\1', text)

    return result

if __name__ == "__main__":
    input_text = input("Enter a text: ")
    result = remove_repeated_words(input_text)

    my_json = {}
    answers = [result]
    my_json["answers"] = answers
    with open('result.json', 'w', encoding="utf-8") as file:
        dumped_json = json.dumps(my_json, ensure_ascii=False)
        file.write(dumped_json)