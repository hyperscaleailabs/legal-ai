from pathlib import Path

import frontmatter
import markdown
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

POSTS_DIR = Path(__file__).parent.parent.parent / "content" / "posts"


def _load_post(filepath: Path) -> dict:
    post = frontmatter.load(str(filepath))
    content_html = markdown.markdown(
        post.content,
        extensions=["extra", "nl2br"],
    )
    words = len(post.content.split())
    return {
        "slug": filepath.stem,
        "title": post.get("title", "Untitled"),
        "date": post.get("date"),
        "date_str": post.get("date").strftime("%B %d, %Y") if post.get("date") else "",
        "author": post.get("author", "LegalAI Team"),
        "excerpt": post.get("excerpt", ""),
        "image": post.get("image", ""),
        "image_alt": post.get("image_alt", ""),
        "tags": post.get("tags", []),
        "content_html": content_html,
        "reading_time": max(1, words // 200),
    }


def _get_all_posts() -> list[dict]:
    posts = []
    for filepath in POSTS_DIR.glob("*.md"):
        try:
            posts.append(_load_post(filepath))
        except Exception:
            pass
    return sorted(posts, key=lambda p: p["date"] or "", reverse=True)


@router.get("/blog", response_class=HTMLResponse)
async def blog_index(request: Request):
    posts = _get_all_posts()
    return templates.TemplateResponse(
        "blog_index.html", {"request": request, "posts": posts}
    )


@router.get("/blog/{slug}", response_class=HTMLResponse)
async def blog_post(request: Request, slug: str):
    filepath = POSTS_DIR / f"{slug}.md"
    if not filepath.exists():
        raise HTTPException(status_code=404, detail="Post not found")
    post = _load_post(filepath)
    related = [p for p in _get_all_posts() if p["slug"] != slug][:2]
    return templates.TemplateResponse(
        "blog_post.html", {"request": request, "post": post, "related": related}
    )
