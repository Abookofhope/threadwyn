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

# markup attributes the tree walk translates, which the script scan cannot see
markup = s[s.index("<svg"):s.index("<script>")]
for a in ("aria-label", "placeholder", "title"):
    for m in re.finditer(a + r'="([^"]+)"', markup):
        v = m.group(1).strip()
        if v and " " in v or (v and v[0].isupper()):
            cands.add(v)

# the precise contract: every literal handed straight to t() or tf() must have
# a key, whatever it starts with. The sentence-shaped scan above cannot see keys
# that begin with a brace or a lowercase letter.
for m in re.finditer(r'(?<![\w.$])tf?\(\s*("(?:[^"\\\n]|\\.)*")', code):
    try: v = json.loads(m.group(1))
    except Exception: continue
    if v.strip(): cands.add(v)

missing = sorted(c for c in cands if c not in keys)
print("keys %d  scanned %d  MISSING %d" % (len(keys), len(cands), len(missing)))
if "-v" in sys.argv:
    for m2 in missing: print(json.dumps(m2, ensure_ascii=False))

# `t` is the translate function; anything that shadows it in a scope which also
# calls t() throws "t is not a function" only when that branch is reached.
code_lines = code.split("\n")
stack, depth, shadowed = [], 0, []
for i, ln in enumerate(code_lines):
    m = re.search(r'function\s*\w*\s*\(([^)]*)\)', ln)
    if m:
        stack.append({"shadow": "t" in [p.strip() for p in m.group(1).split(",")], "depth": depth})
    if re.search(r'\bvar\b[^;]*\bt\b\s*(=|,|;)', ln) and stack:
        stack[-1]["shadow"] = True
    if re.search(r'(?<![\w.$])t\(', ln) and stack and any(f["shadow"] for f in stack):
        shadowed.append((i + 1, ln.strip()[:100]))
    depth += ln.count("{") - ln.count("}")
    while stack and depth <= stack[-1]["depth"]:
        stack.pop()
print("t() called where t is shadowed: %d" % len(shadowed))
for ln, txt in shadowed: print("  line", ln, "|", txt)

# the reverse of the shadowing check: `t.name` / `t.on` where t is NOT a local
# in scope is a property read on the translate function. Renaming a loop
# variable away from t and missing one use of it produced "undefined is under
# the chart", and no t( call was involved to flag it.
stack, depth, strays_t = [], 0, []
for i, ln in enumerate(code_lines):
    m = re.search(r'function\s*\w*\s*\(([^)]*)\)', ln)
    if m:
        stack.append({"has": "t" in [p.strip() for p in m.group(1).split(",")], "depth": depth})
    if re.search(r'\bvar\b[^;]*\bt\b\s*(=|,|;)', ln) and stack:
        stack[-1]["has"] = True
    if re.search(r'(?<![\w.$"\'])t\.[a-zA-Z]', ln) and not ln.strip().startswith(("/*", "*", "//")):
        if not any(f["has"] for f in stack):
            strays_t.append((i + 1, ln.strip()[:100]))
    depth += ln.count("{") - ln.count("}")
    while stack and depth <= stack[-1]["depth"]:
        stack.pop()
print("t.property where t is the translator: %d" % len(strays_t))
for ln, txt in strays_t: print("  line", ln, "|", txt)
