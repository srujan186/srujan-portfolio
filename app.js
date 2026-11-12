document.documentElement.classList.add('js');
const filters=[...document.querySelectorAll('[data-filter]')];
const panels=[...document.querySelectorAll('.role-panel')];
const names={aiml:'AI & machine learning',fullstack:'Full-stack',backend:'Backend'};
function selectRole(role){
  filters.forEach(button=>button.setAttribute('aria-pressed',String(button.dataset.filter===role)));
  panels.forEach(panel=>panel.hidden=panel.dataset.role!==role);
  document.querySelector('.work-count').textContent=`5 projects · ${names[role]}`;
}
filters.forEach(button=>button.addEventListener('click',()=>selectRole(button.dataset.filter)));
selectRole('aiml');
panels.forEach(panel=>{
  const projects=[...panel.querySelectorAll('.project')];
  projects.forEach(project=>project.addEventListener('toggle',()=>{
    if(!project.open)return;
    projects.forEach(other=>{if(other!==project)other.open=false});
    const image=panel.querySelector('.preview-image img');
    image.src=`assets/${project.dataset.image}`;
    image.alt=`${project.dataset.name} ${project.dataset.image.endsWith('.svg')?'concept diagram':'website preview'}`;
    panel.querySelector('.preview-name').textContent=project.dataset.name;
    panel.querySelector('.preview-category').textContent=project.dataset.category;
    panel.querySelector('.preview-kind').textContent=project.dataset.image.endsWith('.svg')?'System concept':'Project preview';
    const link=panel.querySelector('.preview-link');
    link.href=project.querySelector('.project-links a').href;
    link.setAttribute('aria-label',`Open ${project.dataset.name}`);
  }));
});
const copyButton=document.querySelector('#copy-email');
copyButton.addEventListener('click',async()=>{
  const status=document.querySelector('#copy-status');
  try{
    await navigator.clipboard.writeText('srujansrnvs@gmail.com');
    status.textContent='Email copied';
    copyButton.textContent='Copied';
    setTimeout(()=>{copyButton.textContent='Copy email';status.textContent=''},2500);
  }catch{
    status.textContent='Select the email address to copy it.';
  }
});
if('IntersectionObserver' in window){
  const reveals=new IntersectionObserver(entries=>entries.forEach(entry=>{
    if(entry.isIntersecting){entry.target.classList.add('is-visible');reveals.unobserve(entry.target)}
  }),{threshold:.12});
  document.querySelectorAll('.reveal').forEach(element=>reveals.observe(element));
  const navLinks=[...document.querySelectorAll('.site-header nav a')];
  const sections=new IntersectionObserver(entries=>entries.forEach(entry=>{
    if(entry.isIntersecting)navLinks.forEach(a=>a.classList.toggle('active',a.hash===`#${entry.target.id}`));
  }),{rootMargin:'-20% 0px -55% 0px'});
  ['home','work','about','experience','contact'].forEach(id=>sections.observe(document.getElementById(id)));
}
