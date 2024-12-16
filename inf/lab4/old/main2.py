class XMLtoJSONConverter:
    def __init__(self):
        self.pos = 0        # Указатель на текущую позицию при чтении XML
        self.xml = ""       # Здесь будет храниться весь XML как текст
    
    def read_file(self, filename):
        # Чтение XML файла в строку
        with open(filename, 'r') as file:
            self.xml = file.read()
    
    def skip_whitespace(self):
        # Пропуск пробелов в XML
        while self.pos < len(self.xml) and self.xml[self.pos].isspace():
            self.pos += 1
    
    def parse_tag(self):
        # Чтение имени тега XML (например "book" из "<book>")
        self.pos += 1  # Пропускаем '<'
        tag = ""
        # Читаем название тега пока не встретим >, /, пробел или ?
        while self.pos < len(self.xml) and self.xml[self.pos] not in ('>', '/', ' ', '?'):
            tag += self.xml[self.pos]
            self.pos += 1
        return tag
    
    def parse_attributes(self):
        # Чтение атрибутов тега (например id="bk101")
        attributes = {}
        # Читаем атрибуты пока не встретим >
        while self.pos < len(self.xml) and self.xml[self.pos] != '>':
            # Пропускаем пробелы
            self.skip_whitespace()
            if self.xml[self.pos] in ('/', '?'):
                self.pos += 1
                continue

            # Читаем имя атрибута до =
            attr_name = ""
            while self.pos < len(self.xml) and self.xml[self.pos] != '=':
                attr_name += self.xml[self.pos]
                self.pos += 1
            
            # Пропускаем =" и читаем значение до следующей "
            self.pos += 2  # Skip '="'
            attr_value = ""
            while self.pos < len(self.xml) and self.xml[self.pos] != '"':
                attr_value += self.xml[self.pos]
                self.pos += 1
            self.pos += 1  # Skip closing quote
            
            attributes[attr_name.strip()] = attr_value
        
        return attributes
    
    def parse_element(self):
        if self.pos >= len(self.xml):
            return None
            
        self.skip_whitespace()
        
        # Проверяем, не достигли ли конца файла после пропуска пробелов
        if self.pos >= len(self.xml):
            return None
            
        if self.xml[self.pos] != '<':
            # Text content
            text = ""
            while self.pos < len(self.xml) and self.xml[self.pos] != '<':
                text += self.xml[self.pos]
                self.pos += 1
            return text.strip()
        
        if self.xml[self.pos:self.pos+2] == '<!':
            # Skip comments and DOCTYPE
            while self.pos < len(self.xml) and self.xml[self.pos] != '>':
                self.pos += 1
            self.pos += 1
            return self.parse_element()
            
        if self.xml[self.pos:self.pos+2] == '</':
            # Closing tag
            self.pos += 2
            while self.pos < len(self.xml) and self.xml[self.pos] != '>':
                self.pos += 1
            self.pos += 1
            return None
            
        # Opening tag
        tag = self.parse_tag()
        attributes = self.parse_attributes()
        
        self.skip_whitespace()
        if self.pos < len(self.xml) and self.xml[self.pos:self.pos+2] == '/>':
            self.pos += 2
            return {tag: attributes} if attributes else {tag: ""}
            
        if self.pos < len(self.xml):
            self.pos += 1  # Skip '>'
        
        # Parse children
        children = []
        while True:
            child = self.parse_element()
            if child is None:
                break
            if child:
                children.append(child)
        
        result = {tag: {}}
        
        if len(children) == 1 and isinstance(children[0], str):
            result[tag] = children[0]
        elif children:
            for child in children:
                if isinstance(child, dict):
                    for k, v in child.items():
                        if k in result[tag]:
                            if not isinstance(result[tag][k], list):
                                result[tag][k] = [result[tag][k]]
                            result[tag][k].append(v)
                        else:
                            result[tag][k] = v
                            
        return result
    
    def format_json_string(self, obj, level=0):
        # Преобразует Python словарь в красиво отформатированную JSON строку:
        # - Правильные отступы
        # - Кавычки вокруг ключей и строк
        # - Экранирование специальных символов
        indent = "    " * level
        
        if isinstance(obj, dict):
            items = []
            for k, v in obj.items():
                formatted_key = f'"{k}"'
                formatted_value = self.format_json_string(v, level + 1)
                items.append(f'{indent}    {formatted_key}: {formatted_value}')
            return "{\n" + ",\n".join(items) + f"\n{indent}}}"
            
        elif isinstance(obj, list):
            items = [self.format_json_string(item, level + 1) for item in obj]
            return "[\n" + ",\n".join(f"{indent}    {item}" for item in items) + f"\n{indent}]"
            
        elif isinstance(obj, str):
            # Clean up newlines and escape quotes
            cleaned = obj.replace('\n', ' ').replace('  ', ' ').strip()
            escaped = cleaned.replace('"', '\\"')
            return f'"{escaped}"'
            
        return str(obj)

    def convert(self, input_file, output_file):
        self.read_file(input_file)
        if not self.xml.strip():
            raise ValueError("Empty XML file")
            
        self.pos = 0
        result = self.parse_element()
        
        with open(output_file, 'w', encoding='utf-8') as file:
            formatted_json = self.format_json_string(result)
            file.write(formatted_json)

# Usage
converter = XMLtoJSONConverter()
converter.convert("input.xml", "output.json")