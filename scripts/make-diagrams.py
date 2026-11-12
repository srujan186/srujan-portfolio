from pathlib import Path
base='<svg xmlns="http://www.w3.org/2000/svg" width="800" height="600" viewBox="0 0 800 600"><defs><linearGradient id="g" x2="1" y2="1"><stop stop-color="#fff"/><stop offset="1" stop-color="#dce8f5"/></linearGradient><filter id="shadow"><feDropShadow dx="0" dy="15" stdDeviation="20" flood-color="#7c99b4" flood-opacity=".18"/></filter></defs><rect width="800" height="600" fill="#edf3f9"/><circle cx="400" cy="265" r="200" fill="none" stroke="#d8e4ef"/><circle cx="400" cy="265" r="150" fill="none" stroke="#dae6f0"/>'
end='</svg>'
shield='<g filter="url(#shadow)"><rect x="285" y="145" width="230" height="230" rx="60" fill="url(#g)" stroke="white" stroke-width="3"/><path d="M400 197 459 220v52c0 40-59 67-59 67s-59-27-59-67v-52Z" fill="none" stroke="#6a8ba9" stroke-width="4"/><path d="m374 265 18 18 35-38" fill="none" stroke="#6a8ba9" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></g><text x="400" y="459" font-family="Arial,sans-serif" font-size="29" fill="#354f68" text-anchor="middle">Morpheus</text><text x="400" y="496" font-family="Arial,sans-serif" font-size="17" fill="#72869a" text-anchor="middle">Scan · Isolate · Remediate</text>'
Path('assets/security.svg').write_text(base+shield+end, encoding='utf-8')
for filename,labels,title in [('rag',['Documents','Retrieval','LLM'],'Retrieval-augmented generation'),('pipeline',['Discover','Enrich','SBOM'],'SISA PRISM pipeline')]:
    shapes='<path d="M230 265H570" stroke="#9eb5cb" stroke-width="2" stroke-dasharray="6 7"/>'
    for x,label in zip([190,400,610],labels):
        shapes+=f'<g filter="url(#shadow)"><rect x="{x-80}" y="202" width="160" height="126" rx="28" fill="url(#g)" stroke="white" stroke-width="2"/></g><text x="{x}" y="272" font-family="Arial,sans-serif" font-size="21" text-anchor="middle" fill="#4d6b85">{label}</text>'
    shapes+=f'<text x="400" y="459" font-family="Arial,sans-serif" font-size="25" fill="#354f68" text-anchor="middle">{title}</text><text x="400" y="496" font-family="Arial,sans-serif" font-size="17" fill="#72869a" text-anchor="middle">System concept</text>'
    Path(f'assets/{filename}.svg').write_text(base+shapes+end, encoding='utf-8')
