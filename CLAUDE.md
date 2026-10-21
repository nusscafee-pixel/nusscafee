# نُص كافيه: بوستات إنستجرام

This repo holds the Instagram content for **Nuss Cafe (نُص كافيه)**. The owner talks in Levantine Arabic; reply in the same dialect.

## Where things are
- `*.jpg` in the repo root (1–24): **reference posts**. This is the brand style to match.
- Branch `nusscafee-pixel-patch-1`: **raw product photos** (69 images, beige or marble studio shots).
- `posts/`: finished posts.
- `tools/`: Python (Pillow + raqm) helpers for compositing text, highlights, arrows, footer and scenes.
- `brand/logo_extracted.png`: logo cut from a reference post. It is low-res; ask for a real transparent PNG.

## Brand style (match the reference posts)
- **Mood:** dark, cinematic, moody café scenes. Warm spotlight on the product, deep shadows, charcoal and black tones, palm-leaf shadows. Some posts use a grey wall with a black arch holding the logo.
- **Accent colour:** dark teal `#235C56` to `#2F7068`.
- **Font:** Thmanyah (خط ثمانية). Use **Serif Display Bold** for headlines and **Sans** for small info. The font files are NOT in the repo because of the licence; ask the owner to attach `Thmanyah-Font-Family.zip`.
- **Kashida / مدّ الحروف:** always stretch letters with tatweel `ـ`, e.g. `قهـــوة`, `صريـــح`, `آيـــس`. The owner insists on this.
- **Headline:** witty dialect line, white, top-right. One key word sits on a slightly skewed teal block.
- **Product label:** hand-drawn white curved arrow pointing at the product, with a bold name on a small teal block and a description underneath.
- **Footer:** bottom-left teal dot and vertical line, `عنواننا` on a teal block, then `تقاطع شارع ملعب فلسطين، مع شارع التايلاندي`. Logo bottom-right, or inside the arch.
- **Size:** 1080×1350 (4:5).

## Workflow the owner wants
1. Cut out the product from its photo.
2. Generate a realistic scene around it with an AI image tool. The bar-pouring reference is `9.jpg`.
3. Composite the text and branding with `tools/`.

## Image generation
The owner wants generation fully hooked up so Claude can work alone.
- **Magnific** connector is linked and is the chosen generator. Check `account_balance` first. Nano Banana Pro (`imagen-nano-banana-2`) with the product photo as an `image` reference and `9.jpg` as a `style` reference works well. Upload repo images by their raw.githubusercontent.com URL.
- Magnific results are served from `pikaso.cdnpk.net`. That host must be in the environment's allowed domains, or the container can't download results to composite text on them.
- **Cheap fallback:** the ChatGPT model on Magnific (`gpt-2-mini`, "GPT 2.5") at `quality: low`, `resolution: 1k`, ratio 3:4 costs **15 credits** and looks good. Nano Banana Pro costs 75. Use `simulate_cost` to check prices.
- **Adobe** connector is linked, but it has no generative image tools.
- A Gemini or OpenAI API key may be configured as an environment secret (`GEMINI_API_KEY` / `OPENAI_API_KEY`). Never ask for keys in chat.

## Numbers
- Always use **English digits** (10, 3), never Arabic-Indic (١٠).

## Opening hours
- **Saturday to Thursday:** 10:00 to 22:00. **Friday:** 15:00 to 22:00.
- They close at **22:00**. Never imply late-night or after-closing service, and never schedule a call-to-action story after 22:00.

## Publishing (Metricool)
- The Metricool connector is linked. Brand `Nusscafee` (blogId `7418806`), Instagram `nusscafee`, timezone `Asia/Hebron`.
- Media goes in as public raw.githubusercontent.com URLs from this branch, so push the images before scheduling.
- Pattern: post at **20:00** (Metricool's best time) and the matching story at **17:00**. **Set `isAiGenerated: false`.** The owner does not want the AI label on posts.
- **3 posts a day** (owner asked to intensify), plus stories. Slots: **10:30** (world20 posts), **13:00** (Indomie campaign), **20:00** (daily/sample posts). Stories at **17:00** (daily) and **18:00** (campaign). On Fridays (opens 15:00) use **15:30 / 18:30 / 20:00**.
- Scheduled so far, all in Metricool:
  - 15–24 Oct: daily post and story (`posts/daily/SCHEDULE.md`).
  - 17–19 Oct: three Indomie posts at 13:00.
  - 20–29 Oct:
    - Campaign `camp_post01-10` at 13:00 (Friday 23rd at 15:30).
    - `camp_story01-10` at 18:00.
    - World20 `w07–w16` at 10:30 (Friday 23rd at 18:30).
  - 17–22 Oct (Sat–Thu): "الشتا قرّب" humor series (`posts/winter_humor/`, `tools/winter_humor.py`). Posts at **16:00**, stories at **19:00**. Items: hot chocolate, cappuccino, mint tea, brownie, espresso, hot latte.
  - 25 Oct: the Qunbulet reel at 20:00.
  - 26–30 Oct: sample_style posts at 20:00.
  - 30 Oct: `w17` at 15:30 and the Qunbulet carousel at 18:30.
  - 31 Oct: `w18` at 10:30, the Spanish latte post at 13:00, and `w19` at 20:00.
  - 1 Nov: `w20` at 10:30.
  - The schedule runs out after 1 Nov, so new content is needed from 2 Nov.
  - 2 Nov 20:00: "مين إنت بالشتا" #1 (uuid `1327492236464965757`), on a generated scene. Posts 2 and 5 are made; 3, 4 and 6 wait for credits.
- **Captions:** the owner wants them **short**: one line plus an emoji, then `📍 تقاطع شارع ملعب فلسطين، مع شارع التايلاندي`, then 2–3 hashtags.
- `brand/samples/` holds the owner's newest reference posts. Match their layouts.

## Owner feedback (keep applying)
- **No shadow or glow behind text.** Text sits on a darkened or blurred background instead.
- Keep text near the top: headline top-right, a tag pill above it. Don't push text to the bottom.
- Tidy, consistent layout: pill, then 2-line headline, then product label with arrow, then footer.
- **Keep the place details.** The owner tried a blurred background and reverted it; they prefer the scene visible. Frame the scene so the top is calm for the text.
- **Indomie is served plain with spices only.** No egg, cheese or vegetables.
- **Keep the original style.** That means a dark cinematic generated scene, the headline top-right with a teal highlight, the product label with an arrow, and the footer, as in winter_humor and world20. The owner rejected flat graphic or cutout "modern" layouts (`posts/modern/`, called "هبل") and doodle-heavy redesigns. Don't propose new visual directions unless asked.
- **No posts made from the plain menu/studio photos with a dark grade.** The owner rejected this (`posts/who_winter/`). Every post needs a generated scene with an idea, like the winter_humor series.

## Editorial layouts (`tools/world20_layouts.py`)
There are five typography layouts, all without shadows:
- **A:** giant single word with a magazine header line.
- **B:** stacked column with a teal rule.
- **C:** centred minimal.
- **D:** big teal quote mark.
- **E:** outlined giant word.

Text color switches to dark automatically over light backgrounds. The product label is auto-placed from a rembg mask.

## Instagram skills (`.claude/skills/ig-*`)
- These are installed from github.com/Jakeschincariol/instagram-agent-skill (MIT), with the owner's approval.
- They cover planning (`/ig-plan`), stories, captions, comment replies, DMs, profile audits and post-mortems.
- They write text only. They don't post, and they don't replace Metricool.
- Brand voice lives in `brand/voice.md`. Copy it to `~/.claude/instagram/voice.md` before using them.
- They are English-centric. For Arabic captions, follow the caption rules above, which take priority.
