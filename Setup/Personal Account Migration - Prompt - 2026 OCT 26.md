# Personal Account Migration - Prompt - 2026 OCT 26

Paste everything below the line into a new chat in the nickg77 PERSONAL Claude account (claude.ai, code execution on). Run it before migrating.

---

I am migrating this personal account into my Moonflake Team organisation. Custom skills do not migrate, so I need them exported. Do the following in order and do not ask me questions unless a step fails.

1. Find every custom skill available to you. Look in /mnt/skills/user first; if that is empty, search /mnt/skills and any other mounted path for SKILL.md files. Ignore Anthropic built-ins (anything under /mnt/skills/public or /mnt/skills/examples).

2. For each custom skill, compute the sha256 of its SKILL.md and compare the first 12 characters and folder name against this list of skills already saved in my GitHub repo:

anti-sycophancy b77242489e84, brainstorming 6c41331091de, canivibecodeit dc798d7ad9f1, chat-handover 199c9baeea61, cold-outreach-snail-mail 33ef894bf16e, copywriting ab80b91524a7, council abf0bcfb1d73, craft-last-60-days a1199a6a371f, data-clean 0e241eff33c9, doc-polish 490ebfc661df, emails-tasks 3bf5260c31ae, excel-polish b558f924f5a6, fact-check fded991cb6e7, find-skills a759d796ef94, gdoc-comment-analyser 5c13bfc7dc40, humanise-writing 706a6ef6e6e1, interview-me c354146a89c0, italy-private-fleet-outreach-cc 9617500c67a5, italy-private-fleet-outreach cc4d8b681dc9, last-30-days 5b4e617525f6, last-90-days-browser f72f0ccf0e47, last-90-days-cowork e3c2dd7169eb, legalta-lead-gen c16e594bb569, legalta-meeting-transcript-to-tasks 9eaeb4e63eeb, marketplace-listing 6641adb71afa, mom-test-interviews 2e9368f2cf76, outreach-followup e9ce2bcaa998, pdf-to-markdown ce1145ef791f, process-flow-builder 4165295750b4, prompt-refiner b7d784210cb0, rapid-experiment-designer 82e23b0d24bc, ship-it 4305a6b61705, shopping-comparison-table ef113094bd3a, skill-enhancer 75edf3e2fbbd, software-vendor-evaluation 2cdf9b9a9f5e, ste 7c619f88d8a5, thnk-sensing 50b0f699600f, truck-cartel-municipal-outreach-cc d079c985b1a4, truck-cartel-municipal-outreach 6c366451d895, visual-cohesion-audit 24a441ba6a37

3. Show me a table: skill name, status (NEW = not in list, CHANGED = name in list but hash differs, SAME).

4. Put every NEW and CHANGED skill folder, complete with all files, into one zip named "Personal Skills - Export - 2026 OCT 26.zip" (one top-level folder per skill) and give me the download link. Also give me a separate zip per skill so I can upload each one straight into Moonflake.

5. Write out everything you remember about me (memory) as a markdown file named "Personal Memory - Export - 2026 OCT 26.md", grouped by topic (work, job search, health, family, preferences, ongoing projects). Give me the download link.

6. List every project you can see in this account: name, one-line purpose, and whether it has custom instructions. If you cannot list projects, say so plainly.

7. List every connector and integration enabled in this account, so I can reconnect them in Moonflake.
