import re
from pykwalify.core import Core
import yaml

def extract_yaml_snippets(markdown_string):
    pattern = r'```yaml\n(.*?)\n```'
    snippets = re.findall(pattern, markdown_string, re.DOTALL)
    return snippets

def generate_record_schema(properties, types):
    schema = {
        'type': 'map',
        'mapping': {
            'RECORD': {
                'type': 'map',
                'mapping': {properties[i]: {'type': types[i], 'required': False} for i in range(len(properties))}
            }
        }
    }
    return schema

def validate_yaml(yaml_data, schema):
    c = Core(source_data=yaml_data, schema_data=schema)
    c.validate(raise_exception=True)
    
def find_matching_snippet(snippets, schema):
    for snippet in snippets:
        try:
            yaml_data = yaml.safe_load(snippet)
            c = Core(source_data=yaml_data, schema_data=schema)
            c.validate(raise_exception=True)
            return yaml_data["RECORD"]
        except Exception:
            continue
    return None