from html.parser import HTMLParser
from pathlib import Path
import json
class Node:
    def __init__(self,tag='',attrs=()): self.tag=tag; self.attrs=dict(attrs); self.children=[]
    def text(self): return ''.join(c if isinstance(c,str) else c.text() for c in self.children).strip()
    def find(self,cls): return [n for n in self.walk() if cls in n.attrs.get('class','').split()]
    def walk(self):
        for c in self.children:
            if isinstance(c,Node):
                yield c
                yield from c.walk()
    def tags(self,tag): return [n for n in self.walk() if n.tag==tag]
class Parser(HTMLParser):
    def __init__(self): super().__init__(); self.root=Node(); self.stack=[self.root]
    def handle_starttag(self,t,a):
        n=Node(t,a); self.stack[-1].children.append(n)
        if t not in ('meta','link','br','img','hr','input','source'): self.stack.append(n)
    def handle_endtag(self,t):
        for i in range(len(self.stack)-1,0,-1):
            if self.stack[i].tag==t: self.stack=self.stack[:i]; break
    def handle_data(self,d): self.stack[-1].children.append(d)
p=Parser(); p.feed(Path('/tmp/srujan-original.html').read_text(encoding='utf-8'))
roles={}
for role in p.root.find('role-content'):
    projects=[]
    for n in role.find('project-card'):
        projects.append(dict(title=n.tags('h3')[0].text(),tech=n.find('project-tech')[0].text(),description=n.tags('p')[0].text(),links=[{'text':a.text().replace(' →',''),'href':a.attrs['href']} for a in n.tags('a')]))
    roles[role.attrs['data-content']]=dict(title=role.find('section-title')[0].text(),projects=projects,skills=[{'title':n.tags('h3')[0].text(),'description':n.tags('p')[0].text()} for n in role.find('skill-card')],experience=[{'role':n.find('exp-role')[0].text(),'company':n.find('exp-company')[0].text(),'date':n.find('exp-date')[0].text(),'details':[li.text() for li in n.tags('li')]} for n in role.find('exp-card')])
Path('content.json').write_text(json.dumps(roles,indent=2,ensure_ascii=False), encoding='utf-8', newline='\n')
print({key:len(value['projects']) for key,value in roles.items()})
