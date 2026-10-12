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
- **Magnific** connector is linked, but the account had ~0 credits. Check `account_balance` first.
- **Adobe** connector is linked, but it has no generative image tools.
- A Gemini or OpenAI API key may be configured as an environment secret (`GEMINI_API_KEY` / `OPENAI_API_KEY`). Never ask for keys in chat.
