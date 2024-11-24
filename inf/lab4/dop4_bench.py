import time
from typing import Callable
import xml.etree.ElementTree as ET
import json
import re
from main2 import XMLtoJSONConverter
from dop2 import XMLtoJSONConverterRegex
from dop3 import GrammarBasedConverter

def benchmark_converter(name: str, converter: Callable, iterations: int = 100) -> float:
    start_time = time.time()
    
    for _ in range(iterations):
        converter.convert("input.xml", f"output_{name}.json")
        
    end_time = time.time()
    return end_time - start_time

def run_benchmarks():
    # Initialize converters
    original = XMLtoJSONConverter()
    regex = XMLtoJSONConverterRegex()
    grammar = GrammarBasedConverter()
    
    # Simple ElementTree implementation for comparison
    class ETConverter:
        def convert(self, input_file: str, output_file: str):
            tree = ET.parse(input_file)
            root = tree.getroot()
            
            def element_to_dict(elem):
                result = {}
                if elem.attrib:
                    result["@attributes"] = elem.attrib
                if elem.text and elem.text.strip():
                    if list(elem):
                        result["#text"] = elem.text.strip()
                    else:
                        return elem.text.strip()
                for child in elem:
                    child_data = element_to_dict(child)
                    if child.tag in result:
                        if not isinstance(result[child.tag], list):
                            result[child.tag] = [result[child.tag]]
                        result[child.tag].append(child_data)
                    else:
                        result[child.tag] = child_data
                return result
            
            data = {root.tag: element_to_dict(root)}
            with open(output_file, 'w') as f:
                json.dump(data, f, indent=4)
    
    library = ETConverter()
    
    # Run benchmarks
    results = {
        "Original": benchmark_converter("original", original),
        "Library (ElementTree)": benchmark_converter("library", library),
        "Regex": benchmark_converter("regex", regex),
        "Grammar": benchmark_converter("grammar", grammar)
    }
    
    # Print results
    print("\nBenchmark Results (100 iterations):")
    print("-" * 50)
    print(f"{'Implementation':<20} {'Time (seconds)':<15} {'Relative Speed':<15}")
    print("-" * 50)
    
    min_time = min(results.values())
    for impl, time_taken in results.items():
        relative = time_taken / min_time
        print(f"{impl:<20} {time_taken:>14.3f}s {relative:>14.2f}x")

if __name__ == "__main__":
    run_benchmarks()