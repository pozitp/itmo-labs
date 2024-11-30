import xmltodict, json

o = xmltodict.parse(open("./input.xml", "r").read())
print(json.dumps(o)) # '{"e": {"a": ["text", "text"]}}'