import xml.dom.minidom
import xml.sax
from datetime import datetime

def dom_parse(xml_file):
# use the DOM to parse XML and count the maximum value of each namespace<is_a>
    start = datetime.now()
    DOMTree = xml.dom.minidom.parse(xml_file)
    terms = DOMTree.getElementsByTagName('term')
    max_data = {
        'molecular_function': {'id': '', 'name': '', 'count': 0},
        'biological_process': {'id': '', 'name': '', 'count': 0},
        'cellular_component': {'id': '', 'name': '', 'count': 0}
    }

    for term in terms:
            term_id = term.getElementsByTagName('id')[0].firstChild.data.strip()
            term_name = term.getElementsByTagName('name')[0].firstChild.data.strip()
            namespace = term.getElementsByTagName('namespace')[0].firstChild.data.strip()
            is_a_count = len(term.getElementsByTagName('is_a'))
      

            if namespace in max_data and is_a_count > max_data[namespace]['count']:
                max_data[namespace]['id'] = term_id
                max_data[namespace]['name'] = term_name
                max_data[namespace]['count'] = is_a_count

    return max_data, datetime.now() - start

class SAXHandler(xml.sax.ContentHandler):
# SAX processor, which counts the maximum value of each namespace<is_a>
    def __init__(self):
        self.max_data = {
            'molecular_function': {'id': '', 'name': '', 'count': 0},
            'biological_process': {'id': '', 'name': '', 'count': 0},
            'cellular_component': {'id': '', 'name': '', 'count': 0}
        }
        self.current = {}
        self.content = ""

    def startElement(self, name, attrs):
        if name == 'term':
            self.current = {'id': '', 'name': '', 'namespace': '', 'is_a': 0}
        elif name == 'is_a':
            self.current['is_a'] += 1
        self.content = name

    def characters(self, data):
        data = data.strip()
        if not data:
            return
        if self.content == 'id':
            self.current['id'] += data
        elif self.content == 'name':
            self.current['name'] += data
        elif self.content == 'namespace':
            self.current['namespace'] += data

    def endElement(self, name):
        if name == 'term':
            namespace = self.current['namespace']
            if namespace in self.max_data:
                count = self.current['is_a']
                if count > self.max_data[namespace]['count']:
                    self.max_data[namespace].update({
                        'id': self.current['id'],
                        'name': self.current['name'],
                        'count': count
                    })
            self.current = {}

def sax_parse(xml_file):
# use SAX to parse XML and collect statistics
    start = datetime.now()
    parser = xml.sax.make_parser()
    handler = SAXHandler()
    parser.setContentHandler(handler)
    parser.parse(xml_file)
    return handler.max_data, datetime.now() - start


xml_file = 'go_obo.xml'

# DOM
dom_results, dom_time = dom_parse(xml_file)
print("DOM Results:")
for ns, data in dom_results.items():
    print(f"{ns}: {data['id']} ({data['name']}) - {data['count']} <is_a>")

# SAX
sax_results, sax_time = sax_parse(xml_file)
print("\nSAX Results:")
for ns, data in sax_results.items():
    print(f"{ns}: {data['id']} ({data['name']}) - {data['count']} <is_a>")

# time comparison
print(f"\nDOM: {dom_time}\nSAX: {sax_time}")
print("# SAX is generally faster because it doesn't require the full file to be loaded into memory for streaming parsing")

