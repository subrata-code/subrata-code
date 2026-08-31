# Customizing SUBRATA — DIGITAL UNIVERSE

GitHub profile READMEs are static Markdown. `config/profile.yml` is the human source of truth. After you change a value, update the matching surface listed below.

## Identity

| Field | Files |
| --- | --- |
| Name, headline, role | `README.md`, `assets/hero/hero.svg`, `assets/hero/hero-light.svg`, `assets/cards/profile-card.svg` |
| Education / graduation | `assets/cards/profile-card.svg`, `assets/sections/mission.svg` |
| GitHub username | `README.md` stats URLs |
| LeetCode username | `README.md` leetcard URL (currently `subrata2005`) |

## Mission

| Field | File | How to edit |
| --- | --- | --- |
| Mission bars | `assets/sections/mission.svg` | Change the inner `rect` width (max `210`) and the label text (`PRIMARY`, `ACTIVE`, …). Do not present widths as measured skill. |

Regenerate from the design script if you prefer a bulk refresh:

```bash
python tools/generate_assets.py
```

Then re-apply any manual text edits.

## Skills

Skill icons live in `README.md` as `skillicons.dev` image URLs. Add or remove icon ids in those `i=` lists. Do not add skill names as visible text.

## Projects

Edit card copy in `assets/cards/project-*.svg`. Edit the `href` on each project `<a>` in `README.md`. Replace `EDIT_ME` with a real URL before linking.

## Social

Known URLs live in `README.md`. Instagram and GeeksforGeeks are unlinked until you replace `EDIT_ME` in `config/profile.yml` and wrap the badge in an `<a href="...">`.

## Achievements

Only add milestones that actually happened. Replace a `LOCKED` slot in `assets/sections/achievements.svg` and mention it in `config/profile.yml`.

## Theme

Colors are defined at the top of `tools/generate_assets.py` and copied into SVG `<defs>`. Dark mode is primary. Light variants exist for hero, profile card, footer, skills, stats, and LeetCode.

## Stats services

GitHub username must remain `subrata-code`. LeetCode username must remain `subrata2005` unless you change both `config/profile.yml` and the README card URL.
