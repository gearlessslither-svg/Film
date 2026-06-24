---
name: idea-engine
description: Daily AIGC short-video idea engine for Chinese-audience topics, trend/sample scanning, safety screening, duration and image-count planning, music/editing suggestions, and production-ready storyboard refinement. Use when the user asks for “点子发动机”, daily AIGC video ideas, viral AIGC image/video analysis, topic selection, trend reports, safe generatable concepts, or turning a chosen idea into keyframes, image prompts, video prompts, and editing guidance.
---

# 点子发动机 / Idea Engine

## Overview

Use this skill to help the user produce repeatable AIGC video concepts that are attractive to Chinese audiences, feasible for current image/video generators, and low-risk to generate. The skill supports both daily ideation and deeper production planning after an idea is selected.

The target length is flexible: recommend the natural duration for the idea, usually 10 seconds to 3 minutes. Duration is not a fixed requirement; it determines the required number of images/keyframes and production cost.

## Modes

Choose the mode from the user request:

- **Daily idea mode:** Produce 8-12 candidate AIGC video ideas.
- **Trend scan mode:** Search for 10 current AIGC videos/images or style samples with notable traffic or strong aesthetics; report why they work and what production techniques can be borrowed. Browse the web for this mode and cite sources with observation time.
- **Selection mode:** When the user picks one idea, expand it into a production plan with story, duration, keyframes, image count, prompts, and editing rhythm.
- **Risk rescue mode:** If an idea is likely to fail because of celebrity likeness, copyrighted IP, policy friction, or video-model difficulty, rewrite it into safer archetypes while preserving the intent.

## Daily Idea Workflow

When the user asks for daily ideas:

1. Produce 8-12 idea cards.
2. Prefer topics Chinese audiences naturally recognize or enjoy: classic novels, folklore, old TV dramas, childhood cartoons, old games, internet nostalgia, exam/school memories, local urban legends, dreamcore/weirdcore, wuxia/xianxia tropes, historical what-ifs, retro Hong Kong/Taiwan/Mainland aesthetics, or familiar everyday scenes transformed by AIGC.
3. Require a clear AIGC advantage: impossible camera movement, period texture, animation-to-live-action reinterpretation, live-action-to-anime reinterpretation, dreamlike transformation, miniature/world-scale contrast, genre collision, or visual style that would be expensive to shoot.
4. Avoid ideas that depend on exact living celebrity likeness, exact copyrighted character replication, explicit franchise marks, graphic violence, sexual content, public-figure political claims, or unsafe acts. Use archetypes and “inspired by” visual language instead.
5. Recommend natural duration and image count. Do not force 1 minute.
6. Treat music carding/editing as optional upside, not a requirement.

Each idea card should include:

- Title
- One-line hook
- Why Chinese audiences may care
- AIGC advantage / reversal
- Suggested duration
- Estimated image/keyframe count
- Visual style
- Risk level and safer wording
- Video generation feasibility
- Optional music/editing suggestion
- Score summary

Use the detailed rubric in `references/rubric.md` when scoring many ideas.

## Trend Scan Workflow

When the user asks for a daily report, viral examples, current AIGC samples, or “今天有什么能借鉴的”:

1. Browse current web sources. Search broadly; if social platforms are inaccessible, use public search results, creator pages, articles, reposts, and image/video pages. Say when a platform could not be inspected directly.
2. Gather 10 samples. Prefer samples that are either high-traffic, widely discussed, or unusually stylish even if niche.
3. For each sample, report:
   - Source/link and observed metric if available
   - What the viewer sees
   - Why it likely gained traffic
   - Production technique
   - What can be borrowed safely
   - What to avoid copying directly
4. End with 3-5 actionable opportunities for the user’s own daily video pipeline.

Use `references/templates.md` for report structure.

## Selection Workflow

When the user picks an idea:

1. Restate the chosen direction in one paragraph.
2. Choose duration based on narrative density, not habit:
   - 10-20s: one visual gag, one transformation, one atmospheric loop, one memeable contrast.
   - 20-45s: one setup, one turn, one payoff.
   - 45-90s: short story or trailer with 2-4 beats.
   - 90s-3m: full mini-MV, multi-act narrative, richer worldbuilding.
3. Estimate image/keyframe count:
   - Fast montage: 1 image per 2-4 seconds.
   - Normal cinematic: 1 image per 4-6 seconds.
   - Slow atmospheric: 1 image per 6-10 seconds.
   - Complex action/transformations: add inserts and transition frames.
4. Output a production brief:
   - story structure
   - keyframe list
   - image prompts
   - video prompts
   - continuity anchors
   - optional music/editing plan
   - generation risk notes
5. If the user uses the film tool, format outputs so they can become storyboard cards and versions.

## Safety And Feasibility Rules

- Do not rely on exact living celebrity likeness in generation prompts. During brainstorming, “X-like market positioning” can be discussed, but final prompts should use archetypes such as “middle-aged charismatic strategist with sharp blue eyes and a controlled smile.”
- For copyrighted IP, avoid exact names, logos, costumes, and character replicas unless the user is working with owned/authorized material. Preserve the emotional function through genre, era, palette, and archetype.
- Prefer concepts where video models can maintain continuity: simple core characters, clear environments, limited props, repeatable visual motifs.
- Flag likely video-generation failure points: too many famous faces, exact text, crowds, complex hands, exact choreography, heavy violence, precise franchise details, or many continuity-critical characters.
- If risk is high but the idea is valuable, propose a safe substitute rather than discarding it.

## Output Style

Be decisive. The user wants usable ideas, not vague brainstorming. Make tradeoffs visible: why an idea can trend, why it may fail, and what the cheapest strong version is.

When providing a shortlist, recommend a top pick and explain why. When a user rejects a direction, update the heuristic rather than defending the previous idea.

## References

- `references/rubric.md`: scoring model, duration-to-image-count heuristics, and risk grading.
- `references/templates.md`: reusable output templates for daily ideas, trend reports, and selected-idea production plans.
