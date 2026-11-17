import json,glob,os,re,sys
f=sorted(glob.glob('.claude/auto/runs/*session-%03d.jsonl'%int(sys.argv[1])),key=os.path.getmtime)[-1]
calls=ag=agy=0;res=None;wk=None;den=[];uses={}
for l in open(f,encoding='utf-8'):
    m=re.search(r'"seven_day":\{"utilization":([0-9.]+)',l)
    if m:wk=m.group(1)
    try:e=json.loads(l)
    except:continue
    if e.get('type')=='assistant':
        for c in e['message'].get('content') or []:
            if c.get('type')=='tool_use':
                uses[c['id']]=json.dumps(c.get('input'))[:150]
                if e.get('parent_tool_use_id') is None:
                    calls+=1
                    if c['name']=='Agent':ag+=1
                    if 'agy ' in str(c.get('input',{}).get('command','')):agy+=1
    if e.get('type')=='user':
        for c in e.get('message',{}).get('content') or []:
            if isinstance(c,dict) and c.get('is_error') and 'approval' in str(c.get('content')):den.append(uses.get(c['tool_use_id']))
    if e.get('type')=='result':res=e
mu={k[7:13]:round(v['costUSD'],2) for k,v in (res or {}).get('modelUsage',{}).items()}
print('calls',calls,'agents',ag,'agy',agy,'cost',round((res or {}).get('total_cost_usd',0),2),mu,'weekly',wk)
for d in den: print('  DENIED',d)
