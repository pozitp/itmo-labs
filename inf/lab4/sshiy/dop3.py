from dataclasses import dataclass
from typing import List, Optional, Union, Dict
import string

# AST Node classes
@dataclass
class XMLNode:
    tag: str
    attributes: Dict[str, str]
    children: List['XMLNode']
    text: Optional[str] = None

class XMLGrammarParser:
    def __init__(self):
        self.pos = 0
        self.text = ""
        
    def parse_file(self, filename: str) -> XMLNode:
        with open(filename, 'r', encoding='utf-8') as f:
            self.text = f.read()
            self.pos = 0
            return self.parse_document()
            
    def consume_whitespace(self):
        while self.pos < len(self.text) and self.text[self.pos].isspace():
            self.pos += 1
            
    def expect(self, char: str):
        if self.pos >= len(self.text) or self.text[self.pos] != char:
            raise SyntaxError(f"Expected '{char}' at position {self.pos}")
        self.pos += 1
        
    def parse_name(self) -> str:
        name = ""
        name_chars = string.ascii_letters + string.digits + "_-"
        
        while self.pos < len(self.text) and self.text[self.pos] in name_chars:
            name += self.text[self.pos]
            self.pos += 1
            
        if not name:
            raise SyntaxError(f"Expected name at position {self.pos}")
        return name
        
    def parse_attributes(self) -> Dict[str, str]:
        attributes = {}
        
        while True:
            self.consume_whitespace()
            if self.pos >= len(self.text) or self.text[self.pos] in ('>', '/', '?'):
                break
                
            name = self.parse_name()
            self.consume_whitespace()
            self.expect('=')
            self.consume_whitespace()
            self.expect('"')
            
            value = ""
            while self.pos < len(self.text) and self.text[self.pos] != '"':
                value += self.text[self.pos]
                self.pos += 1
            self.expect('"')
            
            attributes[name] = value
            
        return attributes
        
    def parse_element(self) -> XMLNode:
        self.consume_whitespace()
        self.expect('<')
        
        # Handle comments and processing instructions
        if self.text[self.pos] in ('!', '?'):
            self.pos += 1
            while self.pos < len(self.text) and self.text[self.pos-1:self.pos+1] != '?>':
                self.pos += 1
            self.pos += 1
            return self.parse_element()
            
        tag = self.parse_name()
        attributes = self.parse_attributes()
        
        self.consume_whitespace()
        
        # Self-closing tag
        if self.text[self.pos:self.pos+2] == '/>':
            self.pos += 2
            return XMLNode(tag, attributes, [], None)
            
        self.expect('>')
        
        children = []
        text_content = []
        
        while True:
            self.consume_whitespace()
            if self.pos >= len(self.text):
                raise SyntaxError("Unexpected end of document")
                
            if self.text[self.pos:self.pos+2] == '</':
                self.pos += 2
                close_tag = self.parse_name()
                if close_tag != tag:
                    raise SyntaxError(f"Mismatched tags: {tag} != {close_tag}")
                self.consume_whitespace()
                self.expect('>')
                break
                
            if self.text[self.pos] == '<':
                children.append(self.parse_element())
            else:
                text = ""
                while self.pos < len(self.text) and self.text[self.pos] != '<':
                    text += self.text[self.pos]
                    self.pos += 1
                if text.strip():
                    text_content.append(text.strip())
                    
        return XMLNode(
            tag=tag,
            attributes=attributes,
            children=children,
            text=" ".join(text_content) if text_content else None
        )
        
    def parse_document(self) -> XMLNode:
        self.consume_whitespace()
        return self.parse_element()

class GrammarBasedConverter:
    def node_to_dict(self, node: XMLNode) -> dict:
        result = {}
        
        if node.text and not node.children:
            result[node.tag] = node.text
        else:
            result[node.tag] = {}
            
            if node.attributes:
                result[node.tag]["@attributes"] = node.attributes
                
            if node.text:
                result[node.tag]["#text"] = node.text
                
            for child in node.children:
                child_dict = self.node_to_dict(child)
                for k, v in child_dict.items():
                    if k in result[node.tag]:
                        if not isinstance(result[node.tag][k], list):
                            result[node.tag][k] = [result[node.tag][k]]
                        result[node.tag][k].append(v)
                    else:
                        result[node.tag][k] = v
                        
        return result
        
    def format_json(self, obj: Union[dict, list, str], level: int = 0) -> str:
        indent = "    " * level
        
        if isinstance(obj, dict):
            items = []
            for k, v in obj.items():
                formatted_key = f'"{k}"'
                formatted_value = self.format_json(v, level + 1)
                items.append(f'{indent}    {formatted_key}: {formatted_value}')
            return "{\n" + ",\n".join(items) + f"\n{indent}}}"
            
        elif isinstance(obj, list):
            # Fix: Use obj instead of items
            formatted_items = [self.format_json(item, level + 1) for item in obj]
            return "[\n" + ",\n".join(f"{indent}    {item}" for item in formatted_items) + f"\n{indent}]"
            
        elif isinstance(obj, str):
            escaped = obj.replace('"', '\\"')
            return f'"{escaped}"'
            
        return str(obj)
        
    def convert(self, input_file: str, output_file: str):
        parser = XMLGrammarParser()
        ast = parser.parse_file(input_file)
        result = self.node_to_dict(ast)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(self.format_json(result))

# Usage
converter = GrammarBasedConverter()
converter.convert("input.xml", "output_grammar.json")