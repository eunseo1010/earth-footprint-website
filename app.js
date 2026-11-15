const questionIcons=[{"src": "assets/icons/transport.png", "alt": "대중교통 아이콘"}, {"src": "assets/icons/delivery.png", "alt": "배달음식 아이콘"}, {"src": "assets/icons/drink.png", "alt": "음료 아이콘"}, {"src": "assets/icons/clothes.png", "alt": "옷 아이콘"}, {"src": "assets/icons/devices.png", "alt": "전자기기 아이콘"}, {"src": "assets/icons/aircon.png", "alt": "에어컨 아이콘"}, {"src": "assets/icons/bag.png", "alt": "비닐봉지 아이콘"}];
const questions=window.QUESTIONS;
const KEY='earth-question-pages-v1';
let answers={};let index=0;let timer=null;
try{const saved=JSON.parse(sessionStorage.getItem(KEY)||'{}');for(const q of questions){if(q.options.some(o=>o.value===saved[q.id]))answers[q.id]=saved[q.id];}}catch{}
const byId=id=>document.getElementById(id);
function save(){try{sessionStorage.setItem(KEY,JSON.stringify(answers));}catch{}}
function cancel(){if(timer){clearTimeout(timer);timer=null;}}
function render(){cancel();byId('survey').hidden=false;const q=questions[index];const icon=byId("question-icon");icon.src=questionIcons[index].src;icon.alt=questionIcons[index].alt;document.title=`Question ${index+1} · Earth, After?`;byId('progress').textContent=`${String(index+1).padStart(2,'0')} / 07`;byId('question-number').textContent=`Question ${String(index+1).padStart(2,'0')}`;byId('question-title').textContent=q.text;byId('bar').style.width=`${(index+1)/questions.length*100}%`;byId('choices').replaceChildren();q.options.forEach((o,i)=>{const b=document.createElement('button');b.type='button';b.className='answer';b.classList.toggle('selected',answers[q.id]===o.value);b.setAttribute('aria-pressed',String(answers[q.id]===o.value));const n=document.createElement('span');n.className='number';n.textContent=i+1;const text=document.createElement('span');text.className='label';text.textContent=o.label;const arrow=document.createElement('span');arrow.className='arrow';arrow.textContent='→';arrow.setAttribute('aria-hidden','true');b.append(n,text,arrow);b.addEventListener('click',()=>{cancel();answers[q.id]=o.value;save();render();byId('status').textContent='선택했어요. 다음 단계로 이동합니다.';timer=setTimeout(advance,650);});byId('choices').append(b);});byId('prev').disabled=index===0;byId('next').disabled=!answers[q.id];byId('next').textContent=index===6?'답변 저장':'다음 질문 →';byId('status').textContent=answers[q.id]?'저장된 답변을 변경할 수 있습니다.':'답변 하나를 선택해주세요.';}
function advance(){cancel();if(!answers[questions[index].id])return;if(index<6){index++;render();}else finish();}
function finish(){
 cancel();
 if(questions.some(q=>!answers[q.id]))return;
 try{
  sessionStorage.setItem(KEY,JSON.stringify(answers));
  byId('status').textContent='답변이 저장되었습니다.';
 }catch{
  byId('status').textContent='브라우저 저장이 차단되었습니다. 답변은 현재 화면에서만 유지됩니다.';
 }
 // Stay on Question 07. No result page or answer summary is displayed.
 byId('next').textContent='저장 완료';
 byId('next').disabled=true;
}
byId('next').addEventListener('click',advance);byId('prev').addEventListener('click',()=>{cancel();if(index>0){index--;render();}});const first=questions.findIndex(q=>!answers[q.id]);index=first<0?6:first;render();if(first<0)finish();
