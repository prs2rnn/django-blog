import bleach
import markdown


def render_markdown(text: str):
    md = markdown.Markdown(
        extensions=[
            "fenced_code",
            "tables",
            "toc",
            "codehilite",
            "attr_list",
        ],
    )

    html = md.convert(text)
    toc = ""
    if len(md.toc_tokens) >= 2:
        toc = md.toc

    ALLOWED_TAGS = bleach.sanitizer.ALLOWED_TAGS | {
        "p",
        "div",
        "span",
        "pre",
        "code",
        "h1",
        "h2",
        "h3",
        "h4",
        "ul",
        "ol",
        "li",
        "table",
        "thead",
        "tbody",
        "tr",
        "th",
        "td",
        "blockquote",
        "a",
        "img",
        "figure",
        "figcaption",
    }
    ALLOWED_ATTRIBUTES = {
        "*": ["class", "id"],
        "a": [
            "href",
            "target",
            "rel",
            "title",
        ],
        "img": ["src", "alt", "width", "height"],
    }

    html = bleach.clean(html, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRIBUTES)
    toc = bleach.clean(toc, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRIBUTES)

    return html, toc
