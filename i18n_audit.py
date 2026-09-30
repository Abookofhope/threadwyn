# -*- coding: utf-8 -*-
import io, re, json, sys
s = io.open("/home/user/threadwyn/src/index.html", encoding="utf-8").read()

start = s.index("var I18N = { fr:{")
end = s.index('\n} };', start) + len('\n} };')
keys = set(re.findall(r'\n\s*"((?:[^"\\]|\\.)*)"\s*:', s[start:end]))
spans = [(start, end)]
for m in re.finditer(r'\}\)\(\[(.*?)\]\);', s, re.S):
    spans.append(m.span())
    try:
        for d in json.loads("[" + m.group(1) + "]"):
            if isinstance(d, dict): keys |= set(d.keys())
    except Exception:
        for k in re.findall(r'"((?:[^"\\]|\\.)*)"\s*:', m.group(1)): keys.add(k)

def unesc(v):
    try: return json.loads('"' + v + '"')
    except Exception: return v
keys = set(unesc(k) for k in keys)

cut = list(s)
for a, b in spans:
    for i in range(a, b): cut[i] = " "
code = "".join(cut)
code = code[code.index("<script>"):]

SKIP = {"Threadwyn  ·  ", "THREADWYN — "}
cands = set()
for m in re.finditer(r'"((?:[^"\\\n]|\\.){6,200})"', code):
    v = unesc(m.group(1))
    if " " not in v: continue
    if not re.match(r'^[A-Z“(]', v): continue
    if re.search(r'</?[a-z]+[ >/]', v): continue
    if re.match(r'^\(?(display-mode|prefers-color)', v): continue
    if v in SKIP: continue
    cands.add(v)

missing = sorted(c for c in cands if c not in keys)
print("keys %d  scanned %d  MISSING %d" % (len(keys), len(cands), len(missing)))
if "-v" in sys.argv:
    for m2 in missing: print(json.dumps(m2, ensure_ascii=False))
