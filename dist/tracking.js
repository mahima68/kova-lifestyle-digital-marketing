(()=>{'use strict';
const KEY='kova_marketing_demo_events_v1';
const params=new URLSearchParams(location.search),tags={};
for(const k of ['utm_source','utm_medium','utm_campaign','utm_content']){const v=params.get(k);if(v&&/^[a-zA-Z0-9_-]{1,80}$/.test(v))tags[k]=v;}
function record(name,detail={}){try{let events=JSON.parse(localStorage.getItem(KEY)||'[]');if(!Array.isArray(events))events=[];events.push({event:name,time:new Date().toISOString(),...tags,...detail});localStorage.setItem(KEY,JSON.stringify(events.slice(-100)));}catch{}}
record('page_view',{page:'drop'});
const fit=document.querySelector('#fit');fit.addEventListener('change',()=>{document.querySelector('#product-title').textContent=`The ${fit.value} Tee`;document.querySelector('#product-price').textContent=`Proposed price ₹${fit.value==='Everyday'?'699':'899'}`;});
document.querySelector('#product-form').addEventListener('submit',e=>{e.preventDefault();const colour=document.querySelector('input[name=colour]:checked').value;record('view_item',{item_id:`concept_${fit.value.toLowerCase()}_${colour.toLowerCase()}`,fit:fit.value,collection:document.querySelector('#gender').value,colour});document.querySelector('#product-response').textContent=`You explored ${fit.value} in ${colour}. This is a concept, not an item for sale.`;});
document.querySelector('#fit-details').addEventListener('toggle',e=>{if(e.target.open)record('select_content',{content_id:'fit_note'});});
document.querySelector('#signup-form').addEventListener('submit',e=>{e.preventDefault();const form=e.currentTarget;if(!form.reportValidity())return;record('generate_lead',{form_id:'demo_launch_list',demo_only:true});form.reset();document.querySelector('#signup-result').textContent='Demo complete. No email was saved or sent, and no subscription was created.';});
})();
