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
- **Adobe** connector is linked, but it has no generative image tools.
- A Gemini or OpenAI API key may be configured as an environment secret (`GEMINI_API_KEY` / `OPENAI_API_KEY`). Never ask for keys in chat.

## Publishing (Metricool)
- The Metricool connector is linked. Brand `Nusscafee` (blogId `7418806`), Instagram `nusscafee`, timezone `Asia/Hebron`.
- Media goes in as public raw.githubusercontent.com URLs from this branch, so push the images before scheduling.
- Pattern: post at **20:00** (Metricool's best time) and the matching story at **17:00**. Set `isAiGenerated: true`, because the scenes are AI-generated.
- Scheduled so far: 15–24 Oct daily post + story (`posts/daily/SCHEDULE.md`), 25 Oct the Qunbulet al-Nuss reel (with generated music), and 26–30 Oct five posts from `posts/sample_style/`. The Qunbulet carousel and the first Spanish latte post are made but not scheduled.
- **Captions:** the owner wants them **short**: one line plus an emoji, then `📍 تقاطع شارع ملعب فلسطين، مع شارع التايلاندي`, then 2–3 hashtags.
- `brand/samples/` holds the owner's newest reference posts. Match their layouts.

## Owner feedback (keep applying)
- **No shadow or glow behind text.** Text sits on a darkened or blurred background instead.
- Keep text near the top: headline top-right, a tag pill above it. Don't push text to the bottom.
- Tidy, consistent layout: pill, then 2-line headline, then product label with arrow, then footer.
- **Don't show too much of the place:** blur and darken the background around the product (rembg mask plus blur). See `tools/example_indomie.py`.
