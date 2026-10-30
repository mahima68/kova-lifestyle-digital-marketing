import json,pathlib,csv,re,urllib.parse,xml.etree.ElementTree as ET
from html.parser import HTMLParser
root=pathlib.Path(__file__).resolve().parents[1];dist=root/'dist'
d=json.loads((root/'content'/'campaign.json').read_text());a=json.loads((root/'content'/'artwork.json').read_text())
assert len(d['calendar'])==30 and [p['day'] for p in d['calendar']]==list(range(1,31))
assert len(d['keywords'])==30 and len({k['keyword'] for k in d['keywords']})==30
assert len(d['rsas'])==57
for group in {r['ad_group'] for r in d['rsas']}:
 r=[x for x in d['rsas'] if x['ad_group']==group]
 assert sum(x['asset_type']=='Headline' for x in r)==15
 assert sum(x['asset_type']=='Description' for x in r)==4
for r in d['rsas']:assert len(r['text'])==r['characters'] and len(r['text'])<=r['limit']
assert len(a)==11 and sum(x['kind']=='post' for x in a)==3 and sum(x['kind']=='carousel' for x in a)==5 and sum(x['kind']=='story' for x in a)==3
for art in a:
 ET.parse(dist/art['file']);assert (dist/art['file'].replace('.svg','.png')).exists()
assert sum(x['spend_inr'] for x in d['scenario'])==12000
assert sum(x['demo_leads'] for x in d['scenario'])==54
for x in d['scenario']:assert 0<=x['demo_leads']<=x['landing_sessions']<=x['clicks']<=x['impressions'] and 'Synthetic' in x['data_type']
class Page(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.ids=set();self.h1=0;self.title=0;self.desc=0
 def handle_starttag(self,tag,attrs):
  attr=dict(attrs)
  if 'id' in attr:self.ids.add(attr['id'])
  if tag=='h1':self.h1+=1
  if tag=='title':self.title+=1
  if tag=='meta' and attr.get('name')=='description':self.desc+=1
  if tag=='img':assert attr.get('alt'), 'Missing image alt'
  if tag in ['a','img','script','link']:
   url=attr.get('href',attr.get('src',''))
   if url and not urllib.parse.urlsplit(url).scheme and not url.startswith('//'):self.links.append(url)
pages={}
for f in dist.rglob('*.html'):
 p=Page();p.feed(f.read_text());pages[f.resolve()]=p
 assert p.h1==1 and p.title==1,(f,p.h1,p.title)
 if f.parent==dist:assert p.desc==1,f
errors=[]
for f,p in pages.items():
 for link in p.links:
  url=urllib.parse.urlsplit(link);target=(f.parent/urllib.parse.unquote(url.path)).resolve() if url.path else f
  if not target.exists():errors.append((f.name,link,'missing file'))
  if url.fragment and target.suffix=='.html' and target in pages and url.fragment not in pages[target].ids:errors.append((f.name,link,'missing anchor'))
assert not errors,errors
print(f'Passed content checks: 30 days, 30 keyword ideas, 57 valid ad assets, 11 paired SVG/PNG artworks, synthetic funnel consistency, {len(pages)} pages and their internal links.')
