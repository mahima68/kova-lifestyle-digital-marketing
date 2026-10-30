import pathlib,json,base64,html
root=pathlib.Path(__file__).resolve().parents[1];dist=root/'dist'
hero='data:image/png;base64,'+base64.b64encode((dist/'assets/campaign-hero.png').read_bytes()).decode()
flat='data:image/png;base64,'+base64.b64encode((dist/'assets/folded-tees.png').read_bytes()).decode()
assets=[]
def text(x,y,lines,size=100,fill='#262d28',spacing=0):
 return f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{size}" font-weight="500" fill="{fill}" letter-spacing="{spacing}">'+''.join(f'<tspan x="{x}" dy="{0 if i==0 else size*1.12}">{html.escape(line)}</tspan>' for i,line in enumerate(lines))+'</text>'
def shirt(x,y,c,scale=1):return f'<g transform="translate({x},{y}) scale({scale})"><path d="M100 20 35 50 0 140 60 170 90 120 90 360 310 360 310 120 340 170 400 140 365 50 300 20Q200 110 100 20Z" fill="{c}" stroke="#262d2820" stroke-width="2"/><path d="M140 28Q200 90 260 28" fill="none" stroke="#ffffff50" stroke-width="5"/></g>'
def save(id,title,kind,lines,sub,bg,photo=None,cta='Explore the first-drop preview',caption='',format='Feed 4:5'):
 w,h=(1080,1920) if kind=='story' else (1080,1350)
 body=f'<rect width="{w}" height="{h}" fill="{bg}"/>'
 body+=text(70,110,['KOVA'],47,spacing=12)+text(73,145,['L I F E S T Y L E'],13)
 if photo:
  body+=f'<image href="{photo}" x="60" y="420" width="960" height="{h-600}" preserveAspectRatio="xMidYMid slice"/>'
  body+=text(70,250,lines,86)
 else:
  body+=text(70,300,lines,105 if kind!='carousel' else 88)
  if id=='post-03':
   body+=shirt(110,650,'#292d2b',.6)+shirt(430,650,'#e5e0d4',.6)+shirt(750,650,'#899783',.6)
  elif kind=='carousel':
   body+=f'<line x1="70" x2="1010" y1="680" y2="680" stroke="#262d2840"/>'
   body+=text(70,770,sub,37)
   body+=text(70,1110,['A FIT IDEA, NOT A TESTED GARMENT.'],18,fill='#5d685e',spacing=1)
  else:
   body+=shirt(190,650,'#899783',1.7 if kind=='story' else 1.2)
 if photo: body+=text(75,h-140,sub,23)
 body+=f'<rect x="0" y="{h-90}" width="1080" height="90" fill="#272e28"/>'
 body+=text(70,h-49,[cta+'  →'],24,fill='#f6f2e8')+text(70,h-20,['FICTIONAL PORTFOLIO · AI-ASSISTED CONCEPT'],11,fill='#b4bdaf',spacing=1)
 out=f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title"><title id="title">{html.escape(title)} — KOVA fictional campaign</title>{body}</svg>'
 (dist/'creatives'/f'{id}.svg').write_text(out)
 assets.append({'id':id,'title':title,'kind':kind,'format':format,'file':f'creatives/{id}.svg','caption':caption or 'Two fits. Three colours. Find your everyday starting point with KOVA. Explore the fictional collection preview.','cta':cta})
save('post-01','Wear your everyday','post',['Wear your','everyday.'],['Two fits. Three colours. One starting point.'],'#f5f0e6',hero,caption='Everyday is a style. Meet KOVA, a fictional label built around simple fits and three easy colours. Explore the first-drop preview.')
save('post-02','A quieter starting point','post',['Less outfit','overthinking.'],['Ink. Chalk. Sage.'],'#e7e9df',flat,caption='A neutral tee can be a useful starting point. Try yours with denim, relaxed trousers or an open shirt. Save this outfit idea.')
save('post-03','Three colours, your call','post',['Ink. Chalk.','Sage.'],[],'#dddccf',caption='A quiet palette, a few familiar combinations. Start with the shade you would actually reach for. Which one is yours?')
slides=[('Start with fit.',['Start with fit.','Then colour.'],['A small guide to the KOVA concept.','Swipe to compare the two silhouettes.']),('The Everyday idea',['The Everyday','starting point.'],['A proposed straight silhouette.','Use verified garment measurements','before making a real fit claim.']),('A little more room',['A little','more room.'],['The Oversized concept adds room','through the body and sleeves.','It is a silhouette, not a size shortcut.']),('Compare, don’t guess',['Compare.','Do not guess.'],['Lay a tee you own flat.','Compare shoulder, chest and length','with a verified garment size chart.']),('Find your starting point',['Your fit.','Your everyday.'],['Explore two fit ideas and three colours.','The KOVA preview is fictional.','No products are sold through it.'])]
for i,(title,lines,sub) in enumerate(slides):save(f'carousel-{i+1:02}',title,'carousel',lines,sub,['#ebe8dd','#d6dfce','#deddd2','#e9d8c9','#d4dccd'][i],cta=f'{i+1}/5 · Save the fit guide',caption='Two different moods, one everyday wardrobe. Swipe through the proposed Everyday and Oversized fits, then check the fit article. Save the guide.',format='Carousel 4:5')
save('story-01','Which shade feels like you?','story',['Ink. Chalk.','Sage.'],['Which shade feels like you?'],'#e8e7dc',flat,cta='Proposed poll: choose your shade',format='Story 9:16')
save('story-02','Your fit, your everyday','story',['Your fit.','Your everyday.'],['Everyday or Oversized?'],'#e9e3d8',hero,cta='Explore the fictional preview',format='Story 9:16')
save('story-03','What helps you choose?','story',['Before you','choose.'],[],'#d6decc',cta='Question idea: fit, fabric or delivery?',caption='What stops you buying a tee online? Proposed question sticker: fit, fabric details, delivery cost or return terms. No responses have been collected.',format='Story 9:16')
(dist/'artwork.js').write_text('window.KOVA_ARTWORK = '+json.dumps(assets)+';')
(root/'content'/'artwork.json').write_text(json.dumps(assets,indent=2))
