import json, html
from pathlib import Path
h=html.escape
roles=json.loads(Path('content.json').read_text(encoding='utf-8'))
resume='https://drive.google.com/file/d/1qlhcYHaLflYWFon-wAEdI2ojP1_5Eti_/view?usp=sharing'
icons={'arrow':'<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>','out':'<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M6 18 18 6M6 6h12v12"/></svg>'}

def identity(title):
    for key,name,category,image in [('AdCraft','AdCraft AI','Generative video','adcraft.png'),('MORPHEUS','Morpheus','AI supply-chain security','security.svg'),('Skintel','Skintel AI','Computer vision','skintel.png'),('RAG','RAG Chatbot','Retrieval-augmented generation','rag.svg'),('DNA','DNA Cryptography','Applied cryptography','dna.png'),('EW','EW Visualization','Real-time graphics','radar.png'),('SISA','SISA PRISM','Software supply-chain security','pipeline.svg')]:
        if key in title: return name,category,image
    raise ValueError(title)

panels=[]
for role,data in roles.items():
    items=[]
    for i,p in enumerate(data['projects']):
        name,category,img=identity(p['title'])
        links=''.join(f'<a href="{h(l["href"])}" target="_blank" rel="noopener noreferrer">{h(l["text"])} {icons["out"]}</a>' for l in p['links'])
        tech=''.join(f'<span>{h(t.strip())}</span>' for t in p['tech'].split('·'))
        description=p['description']
        if name=='AdCraft AI' and role=='aiml':
            description='An AI video generator that turns a business URL into a finished ad. An LLM writes the script, Kokoro synthesizes the voiceover, and FFmpeg brings the video, music, and narration together.'
        items.append(f'''<details class="project" data-image="{img}" data-name="{h(name)}" data-category="{h(category)}" {'open' if i==0 else ''}>
          <summary><span>{h(name)}</span><span class="expand" aria-hidden="true"></span></summary>
          <div class="project-details"><p>{h(description)}</p><div class="tags">{tech}</div><div class="project-links">{links}</div></div>
        </details>''')
    skills=''.join(f'<div><h4>{h(s["title"])}</h4><p>{h(s["description"])}</p></div>' for s in data['skills'])
    panels.append(f'''<div class="role-panel" id="panel-{role}" data-role="{role}" aria-labelledby="filter-{role}">
      <h3 class="no-js-title">{h(data['title'])}</h3>
      <div class="project-explorer"><div class="project-list">{''.join(items)}</div>
      <figure class="project-preview glass"><div class="preview-top"><span class="window-dots" aria-hidden="true"><i></i><i></i><i></i></span><span class="preview-kind">Project preview</span>{icons['out']}</div><div class="preview-image"><img src="assets/adcraft.png" width="1280" height="720" loading="lazy" alt="AdCraft AI website preview"></div><figcaption><div><strong class="preview-name">AdCraft AI</strong><span class="preview-category">Generative video</span></div><a class="preview-link circle-link" href="https://adcraft-ai-xbog.vercel.app/" target="_blank" rel="noopener noreferrer" aria-label="Open AdCraft AI">{icons['out']}</a></figcaption></figure></div>
      <details class="skills-details"><summary>Explore the toolkit <span>{icons['arrow']}</span></summary><div class="skills-grid">{skills}</div></details>
    </div>''')
experiences=[]
for role,i in [('aiml',0),('fullstack',0),('aiml',1)]:
    e=roles[role]['experience'][i]
    items=''.join(f'<li>{h(text)}</li>' for text in e['details'])
    company=e['company'].split(' · ')[0].replace(' Pvt. Ltd.','')
    experiences.append(f'''<details class="experience"><summary><span class="experience-company">{h(company)}</span><span class="experience-role">{h(e['role'])}</span><span class="experience-date">{h(e['date'])}</span><span class="expand" aria-hidden="true"></span></summary><ul>{items}</ul></details>''')
page='''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Srujan S — AI Engineer & Developer</title><meta name="description" content="Srujan S is an AI engineer and full-stack developer in Bengaluru, building intelligent systems, security tools, and useful digital experiences.">
<meta name="theme-color" content="#f7f9fc"><meta property="og:title" content="Srujan S — AI Engineer & Developer"><meta property="og:description" content="Intelligent systems. Thoughtful engineering. Explore Srujan’s work in AI, full-stack development, and backend engineering."><meta property="og:type" content="website">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;450;500;550;600;650;700&display=swap" rel="stylesheet"><link rel="stylesheet" href="style.css"><script src="app.js" defer></script></head>
<body><a class="skip-link" href="#main">Skip to content</a>
<header class="site-header glass"><a class="brand" href="#home" aria-label="Srujan home"><span class="brand-mark">s.</span><span>Srujan</span></a><nav aria-label="Main navigation"><a href="#work">Work</a><a href="#about">About</a><a href="#experience">Experience</a></nav><a class="nav-contact" href="#contact">Let’s talk <span aria-hidden="true">↗</span></a></header>
<main id="main"><section class="hero wrap" id="home"><div class="hero-main"><div class="hero-copy"><p class="role-line">AI engineer & full-stack developer</p><h1>Srujan S<span>.</span></h1><p class="hero-description">Turning complex ideas into<br class="desktop-break"> intelligent experiences.</p><p class="hero-note">From AI models to the interfaces around them.<br>Built with curiosity. Shipped with care.</p><div class="hero-actions"><a class="button button-dark" href="#work">Explore my work '''+icons['arrow']+'''</a><a class="resume-link" href="'''+h(resume)+'''" target="_blank" rel="noopener noreferrer">View résumé '''+icons['out']+'''</a></div></div>
<div class="hero-art"><img class="hero-sculpture" src="assets/glass-brain.png" alt="Translucent liquid-glass brain with sparse neural connections" width="1254" height="1254" fetchpriority="high"><div class="floating-note glass"><span class="spark" aria-hidden="true"><svg viewBox="0 0 32 32" fill="none"><path d="M16 3v26M3 16h26M7 7l18 18M7 25 25 7"/></svg></span><div><strong>Intelligence, connected.</strong><span>AI · Machine learning</span></div></div></div></div>
<div class="hero-meta"><span class="location"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M19 10c0 5-7 11-7 11S5 15 5 10a7 7 0 1 1 14 0Z"/><circle cx="12" cy="10" r="2.5"/></svg>Bengaluru, India</span><span>Currently at <strong>SISA Information Security</strong></span><a href="#contact"><i class="status-dot" aria-hidden="true"></i>Open to opportunities</a></div>
</section>
<section class="work-section wrap" id="work"><div class="section-heading reveal"><h2>Selected work<span>.</span></h2><p>From the first experiment<br>to the production pipeline.</p></div>
<div class="work-toolbar reveal"><div class="filters glass" role="group" aria-label="Filter work by discipline"><button id="filter-aiml" data-filter="aiml" aria-pressed="true" aria-controls="panel-aiml">AI & machine learning</button><button id="filter-fullstack" data-filter="fullstack" aria-pressed="false" aria-controls="panel-fullstack">Full-stack</button><button id="filter-backend" data-filter="backend" aria-pressed="false" aria-controls="panel-backend">Backend</button></div><span class="work-count" aria-live="polite">5 projects · AI & machine learning</span></div>
'''+''.join(panels)+'''
</section>
<section class="about-section wrap" id="about"><div class="about-intro reveal"><h2>A builder,<br>by instinct<span>.</span></h2><div class="education glass"><span class="education-symbol" aria-hidden="true">⌘</span><div><strong>B.E. Computer Science</strong><p>Global Academy of Technology</p></div><span class="gpa">8.5<small>GPA</small></span></div></div><div class="about-copy reveal"><p class="lead">I’m Srujan, a developer based in Bengaluru, working at the intersection of <em>artificial intelligence</em> and <em>software engineering.</em></p><p>I build across the stack: training models, connecting APIs, and shaping the interfaces people use. My work spans AI supply-chain security, generative video, computer vision, and real-time visualization.</p><p>I’m drawn to complex problems and the thoughtful, useful systems that solve them.</p><a class="text-link" href="'''+h(resume)+'''" target="_blank" rel="noopener noreferrer">More about my background '''+icons['out']+'''</a></div></section>
<section class="experience-section wrap" id="experience"><div class="section-heading reveal"><h2>Learning by building<span>.</span></h2><p>Real systems.<br>Real-world experience.</p></div><div class="experience-list reveal">'''+''.join(experiences)+'''</div>
<div class="recognition reveal"><h3>Built under pressure.</h3><div class="award"><span class="award-mark">1st</span><div><h4>Code Breaker’s Challenge</h4><p>Global Academy of Technology · 2025</p><p>A Hugging Face RAG medical chatbot. The judges’ top pick.</p></div></div><div class="award"><span class="award-mark">↗</span><div><h4>Colossus 2.0</h4><p>Dr. AIT Technical Club · 2024</p><p>Team lead. A top-tier finish among 40+ teams in a 24-hour build.</p></div></div><div class="award"><span class="award-mark">↗</span><div><h4>Sandbox Hackathon</h4><p>Dayananda Sagar College · 2026</p><p>Team lead. Rapid AI prototyping under competition constraints.</p></div></div></div></section>
<section class="contact-section wrap" id="contact"><div class="contact-panel glass reveal"><div class="contact-top"><span><i class="status-dot" aria-hidden="true"></i>Open to what’s next</span><span>Bengaluru, India</span></div><h2>Let’s build<br>something good.</h2><div class="contact-bottom"><p>Have an idea, a role, or an interesting problem?<br>I’d love to hear about it.</p><a class="button button-dark" href="mailto:srujansrnvs@gmail.com">Get in touch '''+icons['arrow']+'''</a></div><div class="email-line"><a href="mailto:srujansrnvs@gmail.com">srujansrnvs@gmail.com</a><button id="copy-email" aria-label="Copy email address">Copy email</button><span id="copy-status" role="status"></span></div></div></section></main>
<footer class="wrap"><a class="brand" href="#home"><span class="brand-mark">s.</span><span>Srujan S</span></a><span class="copyright">© 2026 Srujan S</span><div class="social-links"><a href="https://github.com/srujan186" target="_blank" rel="noopener noreferrer">GitHub ↗</a><a href="https://linkedin.com/in/srujan-srinivas-3541b1286/" target="_blank" rel="noopener noreferrer">LinkedIn ↗</a><a href="tel:+917204970239">Call ↗</a></div></footer>
</body></html>'''
Path('index.html').write_text(page, encoding='utf-8', newline='\n')
print('Built index.html with 15 project perspectives and all source links.')
