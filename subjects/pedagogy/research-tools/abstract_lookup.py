import sys
import sys,json,urllib.request,urllib.parse,re
sys.stdout.reconfigure(encoding="utf-8")
def get(u):
    try: return json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'research-client'}),timeout=25))
    except Exception as e: return {'err':str(e)}
for q in sys.argv[1:]:
    print('=====',q)
    if q.startswith('10.'):
        cr=get('https://api.crossref.org/works/'+urllib.parse.quote(q))
        m=cr.get('message',{})
        print('CR:',m.get('title'),m.get('container-title'),m.get('volume'),m.get('issue'),m.get('page'),m.get('issued',{}).get('date-parts'))
        print('CR abs:',re.sub('<[^>]+>','',m.get('abstract','') or '')[:1300])
        e=get('https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI:"'+q+'"')
    else:
        e=get('https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=3&query='+urllib.parse.quote(q))
    for r in e.get('resultList',{}).get('result',[])[:2]:
        print('EPMC:',r.get('authorString','')[:120],'|',r.get('title'),'|',r.get('journalTitle') or r.get('journalInfo',{}).get('journal',{}).get('title'),r.get('pubYear'),r.get('journalInfo',{}).get('volume'),r.get('pageInfo'),r.get('doi'))
        print('  ABS:',re.sub('<[^>]+>','',r.get('abstractText','') or '')[:1300])
    if q.startswith('10.'):
        s=get('https://api.semanticscholar.org/graph/v1/paper/DOI:'+q+'?fields=title,abstract,tldr')
        print('S2 abs:',(s.get('abstract') or '')[:1300],'| TLDR:',(s.get('tldr') or {}).get('text'))
