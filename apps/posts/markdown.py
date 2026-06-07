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
        "pre",
        "code",
        "div",
        "span",
    }
    ALLOWED_ATTRIBUTES = {"*": ["class"]}

    return bleach.clean(html, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRIBUTES)
