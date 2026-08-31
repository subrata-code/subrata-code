# Customizing SUBRATA — DIGITAL UNIVERSE

GitHub profile READMEs are static Markdown. `config/profile.yml` is the human source of truth. After you change a value, update the matching surface listed below.

## Identity

| Field | Files |
| --- | --- |
| Name, headline, role | `README.md`, `assets/hero/hero.svg`, `assets/hero/hero-light.svg`, `assets/cards/profile-card.svg` |
| Education / graduation | `assets/cards/profile-card.svg`, `assets/sections/mission.svg` |
| GitHub username | `README.md` stats URLs, `.github/workflows/snake.yml` |

## Mission and journeys

| Field | File | How to edit |
| --- | --- | --- |
| Mission bars | `assets/sections/mission.svg` | Change the inner `rect` width (max `210`) and the label text (`PRIMARY`, `ACTIVE`, …). Do not present widths as measured skill. |
| DSA statuses | `assets/sections/dsa.svg` | Change the status string and circle color. Allowed: `IN PROGRESS`, `LEARNING`, `QUEUED`. |
| DevOps stages | `assets/sections/devops.svg` | `STAGE` vs `AHEAD` on each node. |

Regenerate from the design script if you prefer a bulk refresh:

```bash
python tools/generate_assets.py
```

Then re-apply any manual text edits.

## Projects

Edit card copy in `assets/cards/project-*.svg`. Edit the `href` on each project `<a>` in `README.md`. Replace `EDIT_ME` with a real URL before linking.

## Social

Known URLs live in `README.md`. Instagram and GeeksforGeeks are unlinked until you replace `EDIT_ME` in `config/profile.yml` and wrap the badge in an `<a href="...">`.

## Achievements

Only add milestones that actually happened. Replace a `LOCKED` slot in `assets/sections/achievements.svg` and mention it in `config/profile.yml`.

## Theme

Colors are defined at the top of `tools/generate_assets.py` and copied into SVG `<defs>`. Dark mode is primary. Light variants exist for hero, profile card, footer, and the snake.

## Snake

1. Repo **Settings → Actions → General**: allow Actions, and allow GitHub Actions to create pull requests / write contents (default `GITHUB_TOKEN` write is enough if the workflow `permissions` stay `contents: write`).
2. Run **Actions → Generate contribution snake → Run workflow**.
3. Generated files replace `assets/snake/*.svg` on the default branch.

## Stats services

Username must remain `subrata-code` in every stats URL. If a card fails to render, the service is down — local SVGs still load.
