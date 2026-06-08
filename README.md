![Python](https://img.shields.io/badge/Python-3.14-blue)
![Django](https://img.shields.io/badge/Django-6.x-green)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple)

# Django Blog

A minimalist personal blog built with Django for publishing notes about programming, technology and everyday life.

The project is inspired by simple static blogs, but uses a database to manage content while keeping the writing experience focused on Markdown.

## Features

* Markdown-based posts
* Markdown-based posts
* Code syntax highlighting
* Automatic light and dark theme
* RSS feed
* Sitemap
* Archive grouped by year

## Tech Stack

* Python 3
* Django 6
* Bootstrap 5

## Install

Clone the repository:

```bash
git clone https://github.com/prs2rnn/django-blog.git
cd django-blog
```

Install dependencies:

```bash
poetry install
```

Apply migrations:

```bash
make migrate
```

Run the development server:

```bash
make runserver
```

Open:

```
http://127.0.0.1:8000
```

## Project Structure

```
apps/
├── core/      # Home, About, Contact pages
└── posts/     # Blog application

static/        # CSS, JS, images, fonts
templates/     # Django templates
```

## Contributing

Contributions are welcome!

You can help by:

- Reporting bugs
- Suggesting features
- Improving architecture
- Writing tests

## License

This project is licensed under the MIT License.
