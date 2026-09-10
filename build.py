#!/usr/bin/env python3
"""Build the hosted site from src/.

    python3 build.py        # writes site/

src/index.html is written for the Claude Artifact host, which supplies the
<!doctype>/<head>/<body> skeleton and a small reset. A plain web server does
not, so this adds both. The reset is load-bearing rather than cosmetic: the
app hides controls with the `hidden` attribute, and .btn/.card set
display:flex, which beats the UA sheet's [hidden]{display:none}. Without the
!important rule below every hidden control on the page would show.

It also stamps the service worker's cache name with a hash of the page, so a
deploy invalidates the previous cache by construction. That is the whole
update mechanism: push, and phones pick it up on next open.
"""
import hashlib, os, re, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC  = os.path.join(HERE, "src")
OUT  = os.path.join(HERE, "site")
SHELL = ["sw.js", "manifest.webmanifest", "icon-192.png", "icon-512.png"]

HEAD = """<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<style>
:root{color-scheme:light dark}
body{margin:0;font:14px/1.45 system-ui,-apple-system,sans-serif;background:#faf9f7}
img{max-width:100%}
[hidden]{display:none!important}
</style>"""

def main():
    src = open(os.path.join(SRC, "index.html"), encoding="utf-8").read()
    end = src.find("</style>")
    if end < 0:
        sys.exit("build: no <style> block in src/index.html")
    end += len("</style>")
    head, body = src[:end], src[end:]

    page = ('<!doctype html>\n<html lang="en">\n<head>\n'
            + HEAD + "\n" + head.strip()
            + "\n</head>\n<body>\n" + body.strip() + "\n</body>\n</html>\n")

    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(page)
    for name in SHELL:
        shutil.copy2(os.path.join(SRC, name), os.path.join(OUT, name))
    open(os.path.join(OUT, ".nojekyll"), "w").close()

    stamp = hashlib.sha256(page.encode("utf-8")).hexdigest()[:8]
    sw_path = os.path.join(OUT, "sw.js")
    sw = open(sw_path, encoding="utf-8").read()
    sw = re.sub(r'var CACHE = "[^"]+";', 'var CACHE = "threadwyn-%s";' % stamp, sw, count=1)
    open(sw_path, "w", encoding="utf-8").write(sw)

    print("site/index.html  %.0f KB" % (len(page.encode("utf-8")) / 1024))
    print("cache name       threadwyn-%s" % stamp)

if __name__ == "__main__":
    main()
