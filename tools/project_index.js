(() => {
  const data=JSON.parse($('project-data').textContent),projects=data.projects;
  const categoryNames=new Map(data.categories.map(c=>[c.id,c.name]));
  const methodNames=new Map(data.methods.map(m=>[m.id,m.name]));
  const byCode=new Map(records.map(r=>[r.code,r]));
  const byId=new Map(projects.map(p=>[p.id,p]));
  const paperProjects=new Map();
  for(const p of projects)for(const code of new Set(p.papers.flatMap(ref=>ref.paper_codes))){if(!paperProjects.has(code))paperProjects.set(code,[]);paperProjects.get(code).push(p);}
  const projectDefaults={search:'',category:'',method:'',environment:'',year:'',project:'',sort:'category',size:'12'};
  let ps={...projectDefaults},projectPage=1,projectFiltered=[],comparison=[];
  const yearsFor=p=>[...new Set(p.papers.flatMap(ref=>{const rows=ref.paper_codes.map(c=>byCode.get(c)?.bibliographic_year).filter(Boolean);return rows.length?rows:ref.year?[ref.year]:[];}))];
  const textByProject=new Map(projects.map(p=>[p.id,[p.name,p.summary,p.description,p.adaptation,p.inputs,p.outputs,p.algorithm_summary,...p.algorithms,...p.environments,...p.methods.map(m=>methodNames.get(m)),...p.papers.map(ref=>ref.title+' '+ref.publication+' '+ref.paper_codes.join(' '))].join(' ').toLocaleLowerCase()]));
  function projectMatches(p,s,omit=''){
    const tokens=s.search.trim().toLocaleLowerCase().split(/\s+/).filter(Boolean);
    return tokens.every(t=>textByProject.get(p.id).includes(t))&&
      (omit==='category'||!s.category||p.category===s.category)&&
      (omit==='method'||!s.method||p.methods.includes(s.method))&&
      (omit==='environment'||!s.environment||p.environments.includes(s.environment))&&
      (omit==='year'||!s.year||yearsFor(p).includes(s.year))&&(!s.project||s.project===p.id);
  }
  function projectSelection(s,omit=''){return projects.filter(p=>projectMatches(p,s,omit));}
  function projectFacets(key){
    const counts=new Map();
    for(const p of projectSelection(ps,key)){
      const values=key==='category'?[p.category]:key==='method'?p.methods:key==='environment'?p.environments:yearsFor(p);
      for(const v of new Set(values))counts.set(v,(counts.get(v)||0)+1);
    }
    return counts;
  }
  const valueLabel=(key,value)=>key==='category'?categoryNames.get(value)||value:key==='method'?methodNames.get(value)||value:key==='project'?byId.get(value)?.name||value:value;
  function projectOptions(key){
    const counts=projectFacets(key),el=$('project-'+key),values=[...counts.keys()].sort((a,b)=>key==='year'?+b-+a:counts.get(b)-counts.get(a)||a.localeCompare(b));
    const first=node('option',{category:'全部方向',method:'全部方法',environment:'全部环境',year:'不限年份'}[key]);first.value='';el.replaceChildren(first);
    for(const value of values){const o=node('option',valueLabel(key,value)+' · '+counts.get(value));o.value=value;el.append(o);}
    if(ps[key]&&!counts.get(ps[key])){const current=node('option',valueLabel(key,ps[key]));current.value=ps[key];current.hidden=true;el.append(current);}
    el.value=ps[key];el.disabled=!values.length&&!ps[key];
  }
  function projectSave(){
    if(activeView!=='projects')return;
    const params=new URLSearchParams({view:'projects'});
    for(const[k,v]of Object.entries(ps))if(v!==projectDefaults[k])params.set(k,v);
    if(projectPage>1)params.set('page',projectPage);
    if(comparison.length)params.set('compare',comparison.join(','));
    try{history.replaceState(null,'',location.pathname+location.search+'#'+params.toString());}catch(e){/* Offline hosts may restrict history. */}
  }
  function projectRestore(){
    const params=new URLSearchParams(location.hash.slice(1));ps={...projectDefaults};
    for(const key of Object.keys(projectDefaults))if(params.has(key))ps[key]=params.get(key);
    for(const[key,values]of [['category',categoryNames],['method',methodNames],['project',byId]])if(ps[key]&&!values.has(ps[key]))ps[key]='';
    if(ps.environment&&!data.environments.includes(ps.environment))ps.environment='';
    if(ps.year&&!/^\d{4}$/.test(ps.year))ps.year='';
    if(!['category','name','year'].includes(ps.sort))ps.sort='category';
    if(!['12','24','all'].includes(ps.size))ps.size='12';
    projectPage=Math.max(1,Number.parseInt(params.get('page'),10)||1);
    comparison=[...new Set((params.get('compare')||'').split(',').filter(id=>byId.has(id)))].slice(0,4);
  }
  function projectOrder(rows){
    const categories=data.categories.map(c=>c.id);
    return [...rows].sort((a,b)=>{
      const fallback=()=>a.name.localeCompare(b.name,undefined,{numeric:true});
      if(ps.sort==='name')return fallback();
      if(ps.sort==='year')return Math.max(0,...yearsFor(b).map(Number))-Math.max(0,...yearsFor(a).map(Number))||fallback();
      return categories.indexOf(a.category)-categories.indexOf(b.category)||projects.indexOf(a)-projects.indexOf(b);
    });
  }
  function references(parent,p){
    for(const ref of p.papers){
      const holder=node('div','','project-reference');
      const title=node('div','','project-reference-title');appendLink(title,ref.url,ref.title);holder.append(title);
      if(ref.publication)holder.append(node('div',ref.publication,'project-reference-meta'));
      const links=node('div','','project-reference-links');
      for(const code of ref.paper_codes){const r=byCode.get(code);if(!r)continue;appendLink(links,r.pdf,'PDF','',code);appendLink(links,r.markdown,'全文','',code);appendLink(links,r.bibtex,'引用','',code);const a=node('a','查看论文条目');a.href='#search='+encodeURIComponent(code);links.append(a);}
      if(links.childNodes.length)holder.append(links);parent.append(holder);
    }
  }
  function projectRow(p){
    const article=node('article','','project-item');article.dataset.project=p.id;article.id='project-'+p.id;
    const grid=node('div','','project-grid'),identity=node('div'),name=node('h3','','project-name');
    appendLink(name,p.repository,p.name);identity.append(name,node('p',categoryNames.get(p.category),'project-category'),node('p',p.summary,'project-summary'));
    const algorithm=node('div');algorithm.append(node('p',p.algorithm_summary,'project-algorithms'));
    const io=node('dl','','project-io');io.append(node('dt','输入'),node('dd',p.inputs),node('dt','输出'),node('dd',p.outputs));algorithm.append(io);
    const implementation=node('div','','project-implementation');implementation.append(node('p',p.environments.join(' · '),'project-runtime'));
    if(p.github.license)implementation.append(node('span',p.github.license,'project-license'));
    const actions=node('div','','project-actions');appendLink(actions,p.repository,'代码 ↗');appendLink(actions,p.github.readme_url,'README ↗');implementation.append(actions);
    const label=node('label','','compare-toggle'),input=node('input');input.type='checkbox';input.dataset.compare=p.id;input.checked=comparison.includes(p.id);input.setAttribute('aria-label','对比 '+p.name);
    input.addEventListener('change',()=>{if(input.checked&&comparison.length<4)comparison.push(p.id);else comparison=comparison.filter(id=>id!==p.id);renderComparison();projectSave();});
    label.append(input,node('span','加入对比'));implementation.append(label);
    grid.append(identity,algorithm,implementation);article.append(grid,node('p',p.adaptation,'project-adaptation'));
    const details=node('details','','project-details');details.open=ps.project===p.id;
    details.append(node('summary',p.papers.length?'实现说明与论文 · '+p.papers.length+' 篇':'实现说明'));
    const body=node('div','','project-detail-body'),description=node('div');description.append(node('h4','方法与实现'),node('p',p.description));
    if(p.resources.length){const resources=node('div','','project-extra-links');for(const r of p.resources)appendLink(resources,r.url,r.label+' ↗');description.append(resources);}
    const chapter=node('div','','project-extra-links');appendLink(chapter,data.source.url+'#'+p.chapter_anchor,'教材说明 ↗');description.append(chapter);body.append(description);
    if(p.papers.length){const papers=node('div');papers.append(node('h4','相关论文'));references(papers,p);body.append(papers);}
    details.append(body);article.append(details);return article;
  }
  function projectChips(){
    const holder=$('project-chips');holder.replaceChildren();
    for(const key of ['search','category','method','environment','year','project'])if(ps[key]){
      const text={search:'搜索',category:'方向',method:'方法',environment:'环境',year:'论文年份',project:'项目'}[key]+': '+valueLabel(key,ps[key]);
      const button=node('button',text,'chip');button.type='button';button.setAttribute('aria-label','移除筛选：'+text);button.append(node('span','×'));button.addEventListener('click',()=>{ps[key]='';renderProjects(true);});holder.append(button);
    }
    holder.hidden=!holder.childNodes.length;
  }
  function renderProjects(resetPage=false){
    if(resetPage)projectPage=1;
    for(const key of ['category','method','environment','year'])projectOptions(key);
    for(const key of ['search','sort','size'])if($('project-'+key).value!==ps[key])$('project-'+key).value=ps[key];
    projectFiltered=projectOrder(projectSelection(ps));
    const size=ps.size==='all'?Math.max(1,projectFiltered.length):+ps.size,pages=Math.max(1,Math.ceil(projectFiltered.length/size));projectPage=Math.min(projectPage,pages);
    const start=(projectPage-1)*size,end=Math.min(start+size,projectFiltered.length);
    $('project-rows').replaceChildren(...projectFiltered.slice(start,end).map(projectRow));
    $('project-count').textContent=projectFiltered.length+' 个';
    const applied=['search','category','method','environment','year','project'].some(k=>ps[k]);
    $('project-result-summary').textContent=(applied?'从全部 '+projects.length+' 个项目中筛选':'全部项目')+(projectFiltered.length?' · 当前显示 '+(start+1)+'—'+end+' 个':'');
    $('project-empty').hidden=!!projectFiltered.length;$('project-reset').disabled=!applied;$('project-export').disabled=!projectFiltered.length;
    $('project-prev').disabled=projectPage<=1;$('project-next').disabled=projectPage>=pages;$('project-page-label').textContent='第 '+projectPage+' / '+pages+' 页';
    for(const button of document.querySelectorAll('[data-project-category]'))button.setAttribute('aria-pressed',String(ps.category===button.dataset.projectCategory));
    for(const button of document.querySelectorAll('[data-project-method]'))button.setAttribute('aria-pressed',String(ps.method===button.dataset.projectMethod));
    projectChips();renderComparison();projectSave();
  }
  function renderComparison(){
    const selected=comparison.map(id=>byId.get(id));
    $('comparison').hidden=!selected.length;$('compare-tray').hidden=!selected.length;
    $('compare-count').textContent=selected.length+' / 4';
    $('compare-tray-text').textContent=selected.length===4?'已选 4 个项目，已达对比上限':'已选 '+selected.length+' 个项目，可对比 2—4 个';
    $('compare-open').disabled=selected.length<2;
    for(const input of document.querySelectorAll('input[data-compare]')){input.checked=comparison.includes(input.dataset.compare);input.disabled=comparison.length>=4&&!input.checked;}
    const table=$('compare-table');table.replaceChildren();table.style.minWidth=Math.max(620,110+selected.length*255)+'px';
    const head=node('thead'),headrow=node('tr'),label=node('th','对比项目');label.scope='col';headrow.append(label);
    for(const p of selected){const th=node('th');th.scope='col';appendLink(th,p.repository,p.name);const remove=node('button','移除','compare-remove');remove.type='button';remove.setAttribute('aria-label','移除对比 '+p.name);remove.addEventListener('click',()=>{comparison=comparison.filter(id=>id!==p.id);renderComparison();projectSave();$('compare-clear').focus();});th.append(remove);headrow.append(th);}
    head.append(headrow);table.append(head);
    const body=node('tbody');
    for(const [label,getter]of [['应用方向',p=>categoryNames.get(p.category)],['算法',p=>p.algorithm_summary],['输入',p=>p.inputs],['输出',p=>p.outputs],['运行环境',p=>p.environments.join(' · ')],['R680 适配',p=>p.adaptation],['相关论文',null]]){
      const tr=node('tr'),th=node('th',label);th.scope='row';tr.append(th);
      for(const p of selected){const td=node('td');if(getter)td.textContent=getter(p);else references(td,p);tr.append(td);}body.append(tr);
    }
    table.append(body);
  }
  function sidebar(items,key,id){
    const holder=$(id);holder.replaceChildren();
    for(const item of items){const count=projects.filter(p=>key==='category'?p.category===item.id:p.methods.includes(item.id)).length;if(!count)continue;
      const button=node('button','','theme-card');button.type='button';button.dataset[key==='category'?'projectCategory':'projectMethod']=item.id;button.setAttribute('aria-pressed','false');button.setAttribute('aria-label',item.name+'，'+count+' 个项目');button.append(node('span',item.name,'theme-name'),node('span',String(count),'theme-number'));
      button.addEventListener('click',()=>{const previous=ps[key];ps={...projectDefaults,[key]:previous===item.id?'':item.id};renderProjects(true);$('projects').scrollIntoView({behavior:'instant'});});holder.append(button);
    }
  }
  function activate(view,write=true){
    activeView=view==='projects'&&projects.length?'projects':'papers';
    const isProject=activeView==='projects';
    $('paper-view').hidden=isProject;$('project-view').hidden=!isProject;
    for(const key of ['papers','projects']){const tab=$(key+'-tab'),selected=(key==='projects')===isProject;tab.setAttribute('aria-selected',String(selected));tab.tabIndex=selected?0:-1;}
    $('skip-content').href=isProject?'#projects':'#papers';
    $('page-description').textContent=isProject?'按任务、算法和运行环境查阅实现，对照论文与车辆适配条件。':'按研究方向、发表年份和期刊 / 会议检索已收录论文。';
    $('footer-count').textContent=' · '+records.length+' 篇论文 · '+projects.length+' 个项目';
    $('footer-note').textContent=isProject?'项目目录可离线浏览，代码与教材链接需联网':'PDF 与全文可离线阅读';
    document.title=(isProject?'开源机器人项目':'移动机器人论文库')+' · WHEELTEC';
    if(write){if(isProject)renderProjects();else render();}
  }
  function navigate(){
    if(location.hash==='#projects'){activate('projects');return;}
    if(['#papers','#overview'].includes(location.hash)){activate('papers');return;}
    const params=new URLSearchParams(location.hash.slice(1));
    if(params.get('view')==='projects'){projectRestore();activate('projects');}
    else{activate('papers',false);restore();render();}
  }
  window.ProjectDirectory={forPaper:code=>paperProjects.get(code)||[],matches:projectMatches,selected:projectSelection,yearsFor};
  $('paper-tab-count').textContent=String(records.length);$('project-tab-count').textContent=String(projects.length);$('projects-tab').hidden=!projects.length;
  $('project-total').textContent=String(projects.length);
  const drl=projects.filter(p=>p.methods.includes('drl')).length,linked=paperProjects.size;
  for(const[count,label]of [[drl,'个深度强化学习项目'],[linked,'篇关联论文提供全文']])if(count){const stat=node('div','','type-stat');stat.append(node('strong',String(count)),node('span',label));$('project-stats').append(stat);}
  if(data.categories.length)$('project-summary-note').append(node('span',data.categories.length+' 个应用方向'));
  if(data.verified_on)$('project-summary-note').append(node('span','仓库核查 '+data.verified_on));
  if(projects.length)$('project-data-note').textContent='运行环境标签包含独立部署仓库，具体 ROS 版本见适配要点。论文年份取已收录论文的出版年份；未收录论文按引用年份显示。仓库信息核查于 '+data.verified_on+'，许可证仅显示明确记录。';
  sidebar(data.categories,'category','project-categories');sidebar(data.methods,'method','project-methods');
  for(const key of ['search','category','method','environment','year','sort','size'])$('project-'+key).addEventListener(key==='search'?'input':'change',()=>{ps[key]=$('project-'+key).value;renderProjects(true);});
  const projectReset=()=>{ps={...projectDefaults};renderProjects(true);};
  $('project-reset').addEventListener('click',projectReset);$('project-empty-reset').addEventListener('click',projectReset);
  for(const[id,delta]of [['project-prev',-1],['project-next',1]])$(id).addEventListener('click',()=>{projectPage+=delta;renderProjects();$('projects').scrollIntoView({behavior:'instant'});$('projects').focus({preventScroll:true});});
  for(const id of ['compare-clear','compare-tray-clear'])$(id).addEventListener('click',()=>{comparison=[];renderComparison();projectSave();$('project-count').parentElement.scrollIntoView({behavior:'instant'});$('project-search').focus({preventScroll:true});});
  $('compare-open').addEventListener('click',()=>{$('comparison').scrollIntoView({behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'instant':'smooth'});$('comparison').tabIndex=-1;$('comparison').focus({preventScroll:true});});
  for(const view of ['papers','projects'])$(view+'-tab').addEventListener('click',()=>activate(view));
  document.querySelector('.collection-tabs').addEventListener('keydown',e=>{if(!['ArrowLeft','ArrowRight','Home','End'].includes(e.key))return;e.preventDefault();const view=e.key==='Home'?'papers':e.key==='End'?'projects':activeView==='projects'?'papers':'projects';activate(view);$(activeView+'-tab').focus();});
  $('project-export').addEventListener('click',()=>{
    const headings=['项目','应用方向','算法','输入','输出','运行环境','R680 适配','代码仓库','相关论文','PDF','全文'];
    const rows=projectFiltered.map(p=>{const holdings=[...new Set(p.papers.flatMap(ref=>ref.paper_codes))].map(code=>byCode.get(code)).filter(Boolean);return [p.name,categoryNames.get(p.category),p.algorithms.join('; '),p.inputs,p.outputs,p.environments.join('; '),p.adaptation,p.repository,p.papers.map(ref=>ref.url).join('; '),holdings.map(r=>r.pdf).filter(Boolean).join('; '),holdings.map(r=>r.markdown).filter(Boolean).join('; ')];});
    const cell=value=>'"'+String(value??'').replace(/"/g,'""')+'"',csv='\ufeff'+[headings,...rows].map(row=>row.map(cell).join(',')).join('\r\n');
    const url=URL.createObjectURL(new Blob([csv],{type:'text/csv;charset=utf-8'})),a=node('a');a.href=url;a.download='wheeltec-open-source-projects.csv';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);
  });
  window.addEventListener('hashchange',navigate);
  if(activeView==='projects')projectRestore();activate(activeView);
})();
