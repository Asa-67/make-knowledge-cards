---
name: make-knowledge-cards
description: Convert user-provided articles or local Markdown/TXT text into concise knowledge cards. Extract important concepts, keep one concept per card, remove duplicates, and never invent information.
---

# Make Knowledge Cards

Convert supplied article or Markdown/TXT content into concise knowledge cards.

## Core behavior

- Produce approximately 5–8 cards when enough meaningful material exists.
- Do not force the count when the source is too short.
- Extract important knowledge rather than minor details.
- Keep one main concept per card.
- Remove duplicate or substantially overlapping cards.
- Do not introduce facts that are absent from the source.
- Preserve source meaning while keeping explanations concise.
- Prefer a source-provided example; otherwise provide a self-test question.
- Use the source language unless another language is requested.

## Card format

1. **Title** — short concept name.
2. **Core Knowledge** — key fact, rule, definition, or relationship.
3. **Concise Explanation** — brief source-grounded explanation.
4. **Example or Self-test Question** — source example when available, otherwise a question.

## Input

Supported input:
- Text pasted directly by the user.
- Markdown (`.md`) content.
- Plain text (`.txt`) content.

## Quality rules

Before returning cards, check that every card is supported by the source, each card focuses on one concept, similar cards are merged, important concepts are represented first, and the count is not artificially increased.

## Unsupported features

- Web scraping or web-page crawling.
- PDF parsing.
- Anki export.
- Graphical user interface.

## Output template

### Card 1 — [Title]

**Core Knowledge:** [key knowledge]

**Concise Explanation:** [brief explanation]

**Example / Self-test:** [example or question]
