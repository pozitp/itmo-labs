def format_json(json_str):
    result = []
    indent_level = 0
    in_string = False
    current_line = ""
    skip_next = False
    array_level = 0

    for i, char in enumerate(json_str):
        # Handle escape sequences
        if skip_next:
            skip_next = False
            continue
        
        if char == '\\' and i + 1 < len(json_str):
            current_line += char + json_str[i + 1]
            skip_next = True
            continue
            
        # Track string state
        if char == '"' and (i == 0 or json_str[i-1] != '\\'):
            in_string = not in_string
            current_line += char
            continue
            
        if in_string:
            current_line += char
            continue
            
        # Handle array brackets
        if char == '[':
            array_level += 1
            current_line += char
            continue
            
        if char == ']':
            array_level -= 1
            current_line += char
            continue
            
        # Skip whitespace outside strings
        if char.isspace() and array_level == 0:
            if not current_line.strip():
                continue
                
        # Handle object braces
        if char == '{':
            if current_line.strip():
                if ':' in current_line:
                    current_line += '' + char
                else:
                    current_line += char
            else:
                current_line = '    ' * indent_level + char
            indent_level += 1
            result.append(current_line)
            current_line = '    ' * indent_level
            continue
            
        if char == '}':
            if current_line.strip():
                result.append(current_line)
            indent_level -= 1
            current_line = '    ' * indent_level + char
            continue
            
        # Handle colons and commas
        if char == ':' and array_level == 0:
            current_line += ':'
            continue
            
        if char == ',' and array_level == 0:
            current_line += char
            result.append(current_line)
            current_line = '    ' * indent_level
            continue
            
        current_line += char
        
    if current_line.strip():
        result.append(current_line)
        
    for i in range(len(result)):
        result[i] = result[i] + '\n'
        
    return result



# Read and write files
with open("./schedule.json", "r") as infile:
    formatted = format_json(infile.read())
print(formatted)
with open("asd.json", 'w') as outfile:
    outfile.write("".join(formatted))