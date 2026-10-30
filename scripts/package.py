from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
root=Path(__file__).resolve().parents[1];dist=root/'dist';out=dist/'downloads'
with ZipFile(out/'creative-assets.zip','w',ZIP_DEFLATED) as z:
 for p in sorted((dist/'creatives').glob('*')):z.write(p,'creatives/'+p.name)
 z.write(root/'content'/'artwork.json','artwork-captions.json')
 z.write(root/'content'/'image-prompts.md','image-prompts.md')
with ZipFile(out/'campaign-pack.zip','w',ZIP_DEFLATED) as z:
 for p in sorted(dist.rglob('*')):
  if p.is_file() and p.suffix!='.zip':z.write(p,str(p.relative_to(dist)))
 z.writestr('README.md', '# KOVA marketing campaign pack\n\nThis archive contains the ready-to-view website, finished artwork and planning files.\n\nServe this folder with `python3 -m http.server 5174 --bind 127.0.0.1`, then open `http://127.0.0.1:5174/`. The case study is index.html, the landing page is drop.html, email drafts are in emails/ and planning CSVs are in downloads/. Use a server so the demo event log is shared across pages.\n\nAll brand products and campaign results are fictional. No leads are collected. AI assistance is disclosed in the campaign brief.\n\nThe separate GitHub source repository includes regeneration scripts and verification notes.\n')
 z.write(root/'content'/'image-prompts.md','image-prompts.md')
print('Campaign and artwork download packs refreshed.')
