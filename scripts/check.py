from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
import json
class Check(HTMLParser):
    def __init__(self): super().__init__(); self.ids=[]; self.local=[]; self.fragments=[]; self.projects=0; self.images=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.append(a['id'])
        if a.get('class')=='project':self.projects+=1
        if tag=='img':
            assert a.get('alt'), 'Missing alt text'
            self.images.append(a['src'])
        for key in ['src','href']:
            value=a.get(key,'')
            if value.startswith('#'):self.fragments.append(value[1:])
            elif value and not urlparse(value).scheme:self.local.append(value)
        if a.get('target')=='_blank':assert 'noopener' in a.get('rel',''), 'External link missing rel'
p=Check();p.feed(Path('index.html').read_text(encoding='utf-8'))
assert len(p.ids)==len(set(p.ids)), 'Duplicate IDs'
assert all(f in p.ids for f in p.fragments), 'Broken anchor'
assert all(Path(f).is_file() for f in p.local), 'Missing local file'
assert p.projects==15
assert len(json.loads(Path('content.json').read_text(encoding='utf-8')))==3
for f in ['security.svg','rag.svg','pipeline.svg','radar.png','dna.png','skintel.png']:
    assert (Path('assets')/f).is_file()
print('PASS: 15 project perspectives, 3 disciplines, unique IDs, anchors, local assets, image alt text, and safe external links.')
