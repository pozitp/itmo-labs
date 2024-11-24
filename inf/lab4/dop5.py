class XMLtoCSVConverter:
    def __init__(self):
        self.pos = 0
        self.xml = ""
        self.headers = set()
        self.rows = []
        
    def read_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            self.xml = file.read()
            
    def skip_whitespace(self):
        while self.pos < len(self.xml) and self.xml[self.pos].isspace():
            self.pos += 1
            
    def parse_tag(self):
        self.pos += 1
        tag = ""
        while self.pos < len(self.xml) and self.xml[self.pos] not in ('>', '/', ' ', '?'):
            tag += self.xml[self.pos]
            self.pos += 1
        return tag
    
    def parse_attributes(self):
        attributes = {}
        while self.pos < len(self.xml) and self.xml[self.pos] != '>':
            self.skip_whitespace()
            if self.xml[self.pos] in ('/', '?'):
                self.pos += 1
                continue
                
            attr_name = ""
            while self.pos < len(self.xml) and self.xml[self.pos] != '=':
                attr_name += self.xml[self.pos]
                self.pos += 1
                
            self.pos += 2
            attr_value = ""
            while self.pos < len(self.xml) and self.xml[self.pos] != '"':
                attr_value += self.xml[self.pos]
                self.pos += 1
            self.pos += 1
            
            attributes[attr_name.strip()] = attr_value
            
        return attributes
    
    def parse_element(self, current_data=None):
        if current_data is None:
            current_data = {}
            
        if self.pos >= len(self.xml):
            return None
            
        self.skip_whitespace()
        
        if self.pos >= len(self.xml):
            return None
            
        if self.xml[self.pos] != '<':
            text = ""
            while self.pos < len(self.xml) and self.xml[self.pos] != '<':
                text += self.xml[self.pos]
                self.pos += 1
            return text.strip()
        
        if self.xml[self.pos:self.pos+2] == '<!':
            while self.pos < len(self.xml) and self.xml[self.pos] != '>':
                self.pos += 1
            self.pos += 1
            return self.parse_element(current_data)
        
        if self.xml[self.pos:self.pos+2] == '</':
            self.pos += 2
            while self.pos < len(self.xml) and self.xml[self.pos] != '>':
                self.pos += 1
            self.pos += 1
            return None
            
        tag = self.parse_tag()
        attributes = self.parse_attributes()
        
        self.skip_whitespace()
        if self.xml[self.pos:self.pos+2] == '/>':
            self.pos += 2
            return
            
        self.pos += 1  # Skip '>'
        
        text_content = ""
        while True:
            content = self.parse_element(current_data)
            if content is None:
                break
            if isinstance(content, str):
                text_content = content.strip()
                if tag in ["name", "date"]:
                    current_data[tag] = text_content
                elif tag in ["subject", "type", "time_start", "time_end", "teacher", "room", "building"]:
                    current_data[tag] = text_content
                    self.headers.add(tag)
        
        if tag == "lesson":
            row_data = current_data.copy()
            self.rows.append(row_data)
            
        return current_data
    
    def escape_csv(self, text):
        if not text:
            return ""
        if ',' in text or '"' in text or '\n' in text:
            return f'"{text.replace("`", "``").replace('"', '""')}"'
        return text
        
    def convert(self, input_file, output_file):
        self.read_file(input_file)
        self.pos = 0
        self.headers = set()
        self.rows = []
        
        self.parse_element()
        
        # Add required headers if not present
        required_headers = {'name', 'date', 'subject', 'type', 'time_start', 'time_end', 
                          'teacher', 'room', 'building'}
        self.headers.update(required_headers)
        
        # Ensure specific column order
        column_order = ['name', 'date', 'subject', 'type', 'time_start', 'time_end', 
                       'teacher', 'room', 'building']
        
        with open(output_file, 'w', encoding='utf-8') as f:
            # Write headers
            f.write(','.join(column_order) + '\n')
            
            # Write rows
            for row in self.rows:
                csv_row = [self.escape_csv(row.get(header, "")) for header in column_order]
                f.write(','.join(csv_row) + '\n')

# Usage
converter = XMLtoCSVConverter()
converter.convert("input.xml", "output.csv")