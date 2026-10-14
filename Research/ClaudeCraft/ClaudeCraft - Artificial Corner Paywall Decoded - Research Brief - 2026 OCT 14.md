# What is behind the Artificial Corner "Claude Code for Non-Techies" paywall? - ClaudeCraft last 60 days
Window: 15 Aug to 14 Oct 2026 (features and habits; widened to 90 days where thin) | Sources: 8 Anthropic doc pages, 4 Artificial Corner posts, 4 other practitioners, community snippets

## Answer
These four paywalled sections are inferred from Anthropic's troubleshooting docs and from Frank Andrade's own free posts. The likely content is: PATH, plan and permission errors; "ask Claude" as the way to get unstuck; three or four starter tasks that build up to skills; and his setup (three context files, Opus by default, a "turn this into a skill" habit). You already do most of this, so for your own learning it's low value. The useful angle is as a template for onboarding non-technical clients or teammates. Confidence: 65% on the categories, 40% on the specifics.

## What the docs say (current)
- Install: native installer recommended; Homebrew, WinGet and npm (Node 22+, never sudo) also work. The Desktop app's Code tab needs no install. Free plan excluded. [Setup](https://code.claude.com/docs/en/setup)
- Error table: `command not found: claude` (PATH, ~/.local/bin), "native installation exists but not in PATH", EACCES, HTML-instead-of-script (region or proxy), WSL1 Exec format error, OAuth invalid code, 403 after login. No "looks stuck" entry, and the installer shows no download progress. [Troubleshoot install](https://code.claude.com/docs/en/troubleshoot-install)
- Desktop permission modes: Manual (default), Accept edits, Plan, Auto, Bypass. These match Frank's "Auto vs Manual". [Desktop](https://code.claude.com/docs/en/desktop)
- Getting unstuck: Esc to stop, Esc Esc or /rewind, /doctor (now proposes fixes), /clear after two failed corrections. [Best practices](https://code.claude.com/docs/en/best-practices), [Checkpointing](https://code.claude.com/docs/en/checkpointing)

## Decoded: the four sections
| Teaser item | Most likely content | Basis | Confidence |
|---|---|---|---|
| Install that looks stuck, errors almost everyone hits | (1) Installer or app download is silent: wait, don't close it. (2) The terminal password prompt shows no characters while you type, which reads as frozen. (3) macOS "Claude would like to access Documents/Downloads" pop-up hidden behind the window. (4) "Git required" when picking a folder: Xcode Command Line Tools prompt on Mac, Git for Windows on PC. (5) Free-plan sign-in failure that looks like a login error. (6) `command not found` after a terminal install, fixed by opening a new window. | Docs error table; [CC for Everyone](https://ccforeveryone.com/guides/claude-code-installation-problems) (Jul); Reddit macOS prompt complaints | 55% (items 2-4 inferred) |
| What getting stuck looks like | The same move each time: paste the error or a screenshot back into Claude and ask "what went wrong and fix it". Also Esc to interrupt when it loops, saying "no" at a permission prompt and redirecting, and a new chat when it goes off course. The YouTube task probably got stuck installing yt-dlp or ffmpeg (Homebrew and password prompt). | Free section ("ask Claude whenever stuck", "tried a few ways that failed"); docs | 65% |
| First tasks, in order | (1) Ask it about your own computer or tidy one messy folder (Downloads). (2) A task regular Claude refuses: download or convert files. (3) Write about-me, voice and working-rules files or a CLAUDE.md. (4) After a run that worked, say "turn this into a skill" (skill-creator). (5) Possibly scheduled tasks or a connector. Each step links to one of his earlier guides. | [Claude setup](https://artificialcorner.com/p/claude-setup) (Mar), [Cowork guide](https://artificialcorner.com/p/cowork-beginners-guide), [Claude lessons](https://artificialcorner.com/p/claude-lessons) (2 Sep) | 50% on order, 70% on items |
| How I use it every day | Opus about 95% of the time. Three .md context files. Skill-creator always on, and 80-90% of skills built from "turn this into a skill". Short CLAUDE.md, hooks for rules that must hold. Few MCP servers (CLIs preferred). /context and /usage checks. Stagger work around the 5-hour usage windows. Parallel sessions. | Same three posts | 70% |

## Where they agree
Start in the Desktop app, not the terminal. Ask Claude to fix its own errors. Learn by tidying one folder. Turn repeat work into skills. Keep CLAUDE.md lean.

## Where they disagree (and why)
Git for Windows: the setup page says optional, the quickstart says recommended. Frank says leave the app on Auto; the docs default to Manual and say to use Git or checkpoints as a safety net, because Bash-made changes can't be rewound.

## Contrarian view
"Leave it on Auto" from day one is poor advice for a beginner on their main machine. One mistaken bulk move or delete outside a Git folder can't be undone with /rewind. A throwaway folder plus Manual for the first hour is safer, and costs only some extra clicks.

## Applied to your task
- Don't pay for it for your own use. You build skills, so the paywalled half is below your level.
- Use it as a template for onboarding Thomas or Arlind, or future AI-consultancy clients: Desktop app, throwaway folder, the six-error checklist above, then folder tidy, then a refused task, then a context file, then "turn this into a skill".
- Prompt ready to paste for a client's first session: "I'm new to Claude Code. Look at my Downloads folder and propose how to organise it. Don't delete anything; move anything you're unsure about into a folder called _review. Show me the plan before you move a file."

## Why this might be wrong
It's all inferred from the free half and older posts. A 54-minute unedited session could have hit problems specific to Diana's machine (Windows, a corporate laptop) that no guide predicts. Not considered: Frank offers a free Claude course and might send the full video if you reply asking for it, or a team member may already subscribe.

## Stale or rejected sources
- "Windows needs Git Bash": outdated (now optional, PowerShell fallback).
- "Ask" mode label: renamed to Manual.
- CC for Everyone (21 Jul): older than 60 days. Kept only where it matches the current docs.
- Simon Willison, Ethan Mollick, Allie K. Miller: nothing beginner-specific in the window.
