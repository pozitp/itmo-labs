def json_to_yaml(json_str):
    def parse_json(s):
        s = s.strip()
        if s == "true":
            return True
        if s == "false":
            return False
        if s == "null":
            return None
        if s.startswith('"') and s.endswith('"'):
            return s[1:-1]
        if s.replace('.','',1).isdigit():
            return float(s) if '.' in s else int(s)
        if s.startswith('{'):
            return parse_object(s)
        if s.startswith('['):
            return parse_array(s)
        return s

    def parse_object(s):
        result = {}
        s = s.strip()[1:-1].strip()  # Remove { }
        if not s:
            return result
            
        parts = []
        current = ''
        depth = 0
        in_string = False
        
        for char in s:
            if char == '"' and (not current or current[-1] != '\\'):
                in_string = not in_string
            elif not in_string:
                if char == '{':
                    depth += 1
                elif char == '}':
                    depth -= 1
                elif char == ',' and depth == 0:
                    parts.append(current)
                    current = ''
                    continue
            current += char
            
        parts.append(current)
        
        for part in parts:
            if ':' not in part:
                continue
            key, value = part.split(':', 1)
            key = parse_json(key.strip())
            value = parse_json(value.strip())
            result[key] = value
            
        return result

    def parse_array(s):
        s = s.strip()[1:-1].strip()  # Remove [ ]
        if not s:
            return []
        
        # Split for arrays while respecting nested structures
        parts = []
        current = ''
        depth = 0
        in_string = False
        
        for char in s:
            if char == '"' and (not current or current[-1] != '\\'):
                in_string = not in_string
            elif not in_string:
                if char in '[{':
                    depth += 1
                elif char in ']}':
                    depth -= 1
                elif char == ',' and depth == 0:
                    parts.append(current.strip())
                    current = ''
                    continue
            current += char
        
        if current:
            parts.append(current.strip())
        
        # Parse each part
        result = []
        for part in parts:
            part = part.strip()
            if part.isdigit():
                result.append(int(part))
            elif part.replace('.', '', 1).isdigit():
                result.append(float(part))
            else:
                result.append(parse_json(part))
        
        return result

    def to_yaml(data, indent=0):
        result = []
        if isinstance(data, dict):
            if not data:
                result.append('{}')
            for key, value in data.items():
                line = ' ' * indent + str(key) + ':'
                if isinstance(value, (dict, list)):
                    result.append(line)
                    result.extend(to_yaml(value, indent + 2))
                else:
                    result.append(f"{line} {format_value(value)}")
        elif isinstance(data, list):
            if not data:
                result.append(' ' * indent + '[]')
            else:
                for item in data:
                    prefix = ' ' * indent + '-'
                    if isinstance(item, (dict, list)):
                        result.append(prefix)
                        result.extend(to_yaml(item, indent + 2))
                    else:
                        result.append(f"{prefix} {format_value(item)}")
        return result

    def format_value(value):
        if isinstance(value, str):
            if any(c in value for c in ':{]}[,\n'):
                return f'"{value}"'
            return value
        if value is None:
            return 'null'
        if isinstance(value, bool):
            return str(value).lower()
        return str(value)

    # Parse JSON and convert to YAML
    data = parse_json(json_str)
    yaml_lines = to_yaml(data)
    return '\n'.join(yaml_lines)

# Example usage:

with open("schedule.json", "r") as infile:
    yaml_output = json_to_yaml(infile.read())
    
with open("output.yaml", "w") as outfile:
    outfile.write(yaml_output)
