#!/usr/bin/env python3
"""Check migration invariants and local URLs in a completed Jekyll build.

Uses only the Python standard library. Run after a production build.
"""

from hashlib import sha256
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "_site"
PAGES = ["index.html", "publications/index.html", "experience/index.html", "honors/index.html", "cv/index.html"]
SELECTED = ["seneviratne2026vega", "abeysinghe2026syncast", "chowdhury2025magnet", "baliah2026vface"]
HOST = "yohanabeysinghe.github.io"


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.refs, self.images, self.ids, self.articles, self.h1 = [], [], [], [], 0
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.append(attrs["id"])
        if tag == "h1":
            self.h1 += 1
        if tag == "article" and "research-entry" in attrs.get("class", ""):
            self.articles.append(attrs.get("id"))
        if tag == "img":
            self.images.append(attrs)
        if tag == "a" or tag in {"link", "img", "script"}:
            value = attrs.get("href", attrs.get("src"))
            if value:
                self.refs.append(value)


def verify():
    errors, checked = [], 0
    parsed = {}
    for name in PAGES:
        path = SITE / name
        if not path.is_file():
            errors.append(f"Missing page: {name}")
            continue
        text = path.read_text()
        page = parsed[name] = Page(text)
        if page.h1 != 1:
            errors.append(f"{name}: expected one h1, got {page.h1}")
        if len(page.ids) != len(set(page.ids)):
            errors.append(f"{name}: duplicate element IDs")
        if re.search(r"you@example|Einstein|prof_pic|Write your biography|under review|first.year PhD|G-PYVRSFMDRL", text, re.I):
            errors.append(f"{name}: stale or template content")
        if not re.search(r"<strong>\s*Yohan\s+Abeysinghe\s*</strong>", text) and name == "publications/index.html":
            errors.append(f"{name}: author emphasis missing")
        for image in page.images:
            if not image.get("alt", "").strip():
                errors.append(f"{name}: image without meaningful alt text")
        for ref in page.refs:
            url = urlsplit(ref)
            if url.scheme or url.netloc:
                continue
            local = unquote(url.path)
            target = SITE / local.lstrip("/") if local.startswith("/") else path.parent / local
            if target.is_dir():
                target /= "index.html"
            if not target.is_file():
                errors.append(f"{name}: broken local URL {ref}")
            elif url.fragment and target.suffix == ".html":
                target_page = Page(target.read_text())
                if unquote(url.fragment) not in target_page.ids:
                    errors.append(f"{name}: missing fragment {ref}")
            checked += 1
        for nav_path in ["/", "/publications/", "/experience/", "/honors/", "/cv/"]:
            if f'href="{nav_path}"' not in text:
                errors.append(f"{name}: missing navigation destination {nav_path}")
        canonical = f'https://{HOST}/' + (name.removesuffix("index.html"))
        if f'rel="canonical" href="{canonical}"' not in text:
            errors.append(f"{name}: incorrect canonical URL")

    if parsed.get("publications/index.html") and set(parsed["publications/index.html"].articles) != set(SELECTED):
        errors.append("Publications page is missing a genuine publication")
    publications = (SITE / "publications/index.html").read_text()
    if f'https://{HOST}/vega_website/' not in publications:
        errors.append("The separately hosted VEGA URL was not preserved")
    for forbidden in ["src", "drafts.txt", "docs", "vendor", "Gemfile", "node_modules", "README.md", ".env"]:
        if (SITE / forbidden).exists():
            errors.append(f"Non-public source material in output: {forbidden}")
    cv = Path("data/Yohan_Abeysinghe_CV.pdf")
    if sha256((ROOT / cv).read_bytes()).digest() != sha256((SITE / cv).read_bytes()).digest():
        errors.append("Public CV was altered while building")
    for project in ["mipnerf", "mipnerf360"]:
        for source in (ROOT / project).rglob("*"):
            if source.is_file():
                output = SITE / source.relative_to(ROOT)
                if not output.is_file() or sha256(source.read_bytes()).digest() != sha256(output.read_bytes()).digest():
                    errors.append(f"Legacy project asset changed or missing: {source.relative_to(ROOT)}")

    if errors:
        raise SystemExit("\n".join(errors))
    print(f"PASS: {len(PAGES)} pages, {checked} local references, publication records, author emphasis, canonical URLs, CV, legacy project assets, and publication exclusions.")


if __name__ == "__main__":
    verify()
