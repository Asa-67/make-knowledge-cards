#!/usr/bin/env python3
"""Quick structural validation for make-knowledge-cards."""
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parent
REQUIRED=[ROOT/'SKILL.md',ROOT/'README.md',ROOT/'LICENSE',ROOT/'agents'/'openai.yaml']
def main():
    missing=[str(p.relative_to(ROOT)) for p in REQUIRED if not p.is_file()]
    if missing:
        print('Validation failed. Missing files:')
        print('\n'.join(f'  - {x}' for x in missing)); return 1
    skill=(ROOT/'SKILL.md').read_text(encoding='utf-8')
    checks=('make-knowledge-cards','5–8','one concept per card','Do not introduce facts','Markdown','Plain text')
    missing=[x for x in checks if x not in skill]
    if missing:
        print('Validation failed. Missing expected Skill content:')
        print('\n'.join(f'  - {x}' for x in missing)); return 1
    print('Validation passed.')
    return 0
if __name__=='__main__': sys.exit(main())
