# make-knowledge-cards

Convert articles or local Markdown/TXT content into concise knowledge cards for fast review.

## Features

- Generate approximately **5–8 knowledge cards** when enough source material exists.
- Extract the **most important concepts**.
- Keep **one concept per card**.
- Remove duplicates or substantially overlapping cards.
- **Do not invent information** that is not supported by the source.
- Use fewer cards when the source does not contain enough meaningful concepts.
- Each card includes a title, core knowledge, concise explanation, and an example or self-test question.
- Supports pasted text, Markdown, and plain-text content.

## Project structure

```text
make-knowledge-cards/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── quick_validate.py
├── README.md
└── LICENSE
```

## Usage

Provide an article or Markdown/TXT content and ask the assistant to convert it into knowledge cards.

Example:

> Turn this article into knowledge cards. Extract only the important concepts, avoid duplicates, and do not add information that is not in the article.

## Validation

Run:

```bash
python quick_validate.py
```

## Current limitations

- Web scraping or web-page crawling
- PDF parsing
- Anki export
- GUI functionality

## Version

Current public version: **v0.1.0**

This initial release focuses on the core knowledge-card generation behavior.
