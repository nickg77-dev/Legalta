# Claude global CLAUDE.md additions - Draft - 2026 OCT 14

Target: ~/.claude/CLAUDE.md on Nick's Mac (global, all projects). Approved 14 Oct 2026, rule on pinning model IDs dropped by Nick.

## Block to add

```markdown
## Model choice and testing
- Quality gates: any test comparing models or setups uses at least 20 rows. Record run date, model, and effort. Rerun when a new model generation ships.
- Model aliases: use the short aliases (opus, sonnet, haiku) so scripts follow the latest model. After a new generation ships, rerun the relevant quality gate before trusting the output.
- Effort: leave at the default (medium). Raising effort costs more without improving care; max is a retry, never a default.
- Routing: Opus for judgement (research, scoring, fit calls). Sonnet for well-scoped, checkable work. Haiku for mechanical checks, lookups and classification; keep Haiku context under 100k tokens (price jumps 5x above it).
- Before a model or setup decision, run the craft-last-60-days skill. Ignore advice older than the current model generation.

## Building skills
- Skill name: lowercase letters, digits and hyphens only, max 64 characters, and never the words "claude" or "anthropic" (claude.ai rejects them). Put a friendly title in the H1 instead.
- Description: max 1024 characters, no XML or HTML tags. Folder name matches the skill name.
- Before zipping or uploading any skill, run the validator (validate-skill.py) and fix every FAIL.

## Where sessions run
- Default to Local, with Remote Control for access from phone or browser. Cloud only for repos already on GitHub, or unattended parallel jobs.
```

## Prompt to paste into a Local Claude Code session

> Open ~/.claude/CLAUDE.md. Add the block below under a new heading, merging with any existing rules on models, testing or environments instead of duplicating them. Show me the diff before saving. Then, in "Claude Macbook Folder/Projects/01 Work Projects/Legalta/2 Sales/DACH/legalta-enrichment/", rerun the quality gate on 20 rows in two arms: (A) --model opus at default effort; (B) --model sonnet with a Haiku rule-checker pass on each row. Record per row: pass/fail, failure type (judgement or rule breach), tokens and cost. Save results to Legalta/Outputs as "Legalta Enrichment - Quality Gate 20 Rows - Results - YYYY MMM DD", and commit with a one-line reason.
>
> [paste the block above]
