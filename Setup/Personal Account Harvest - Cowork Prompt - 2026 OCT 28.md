# Personal Account Harvest - Cowork Prompt - 2026 OCT 28

Before you start:
1. Clone the skills repo to your computer, for example into ~/Claude/nick-claude.
2. Open the Claude desktop app signed in to the nickg77 PERSONAL account, start a Cowork task, and select that repo folder.
3. In Chrome, sign in to claude.ai as the personal account and make sure Claude in Chrome is on.

Paste everything below the line into that Cowork task.

---

I am moving this personal Claude account into my Moonflake Team organisation. Custom skills and published artefacts do not migrate, and publishing is not available on Team. Harvest both into the repo folder you have open. Work through it without asking me questions unless you are blocked by a login, a permission prompt or a missing button.

STEP 1 - SKILLS

1a. Check your own environment first. Search every mounted path for SKILL.md files (for example ~/.claude/skills, /mnt/skills/user, any "synced" folder). Ignore Anthropic built-ins (anything under /mnt/skills/public or /mnt/skills/examples). Copy each custom skill folder, complete with all files, into skills/incoming/<skill-name>/ in the repo.

1b. If 1a finds nothing, use Claude in Chrome: open claude.ai > Customize > Skills (or Settings > Capabilities > Skills). For each custom skill, use its download option if one exists and unzip it into skills/incoming/<skill-name>/.

1c. If neither works, tell me, and I will run the fallback prompt in "Personal Account Migration - Prompt - 2026 OCT 27.md" in a claude.ai chat instead.

1d. Do not overwrite anything under skills/general, skills/legalta or skills/personal. The skills already in the repo are listed in skills/README.md with a sha256 (first 12 characters) of each SKILL.md. For each folder in skills/incoming, compute that hash and delete the folder from incoming if the name and hash both match an existing skill (SAME). Keep NEW and CHANGED ones.

STEP 2 - ARTEFACTS

2a. Using Claude in Chrome, open claude.ai and go to the Artifacts page in the sidebar. List every artefact: title, the chat it came from, and whether it is published (has a public link).

2b. For each artefact, open it and save the full source into artefacts/<type>/<Title> - Artefact - <YYYY MMM DD>.<ext> in the repo, where type is html, react, markdown, code, svg or other, and the date is when it was created if shown, otherwise today. Use the artefact's download or copy button; do not retype it. For React artefacts save the .jsx source.

2c. Create artefacts/README.md with one table: title, file path, published (yes/no), public link if any, source chat title, and a "who relies on this link" column left blank for me.

STEP 3 - COMMIT

Commit everything with the message "Harvest skills and artefacts from personal account before migration" and push to the current branch. If pushing is blocked, tell me and leave the commit in place.

STEP 4 - REPORT

Reply with: number of skills found (NEW, CHANGED, SAME), number of artefacts saved, any published artefacts, and anything you could not save and why.
