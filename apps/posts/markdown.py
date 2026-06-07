import bleach
import markdown


def render_markdown(text: str):
    html = markdown.markdown(
        text,
        extensions=[
            "fenced_code",
            "tables",
            "toc",
            "codehilite",
        ],
    )

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
        "*": ["class"],
        "a": [
            "href",
            "target",
            "rel",
            "title",
        ],
        "img": ["src", "alt", "width", "height"],
    }

    return bleach.clean(html, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRIBUTES)
