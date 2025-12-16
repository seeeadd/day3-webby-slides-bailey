# BAILEY LOW-TICKET OFFER: MASTER DESIGN SYSTEM
## AI Design & Grow Experience — $67/month Membership Page

> **For Claude Code and any developer building this page.**
> Read completely before writing a single line of code.
> This document is law. Deviate only when you have a better idea AND can articulate why.

---

# PART 0: THE NORTH STAR

## What We're Building

A landing page that sells Bailey's $67/month Etsy membership to busy women aged 35-55. But we're not building a "funnel page." We're building something that looks like a Soho boutique designed it. Something that makes people pause and think "wait, this is a membership site?"

## The Impossible Standard

**The test:** Show this page to someone and ask "What does this company sell?"

- If they say "I don't know, but it looks expensive" → We've won
- If they say "some kind of course or funnel thing" → We've failed

**The bar:** "I've never seen a membership sales page that looks like this, and now I want to join just because of how premium it feels."

## The Audience Reality Check

This page is for:
- Women aged 35-55
- Many are moms squinting at phones
- Many are skeptical (burned by courses before)
- Most are overwhelmed and skim everything
- They need LARGE, READABLE text
- They need CLEAR visual hierarchy
- They need to feel CALM, not pressured

**If you have to squint to read ANYTHING, it's too small. Make it bigger.**

---

# PART 1: THE VIBE

## 1.1 — Reference Energy

Imagine if these brands had a baby who sold Etsy memberships:

| Brand | What We Steal |
|-------|---------------|
| **Aesop** | The negative space, the quiet confidence, typography as design |
| **The Row** | Money whispers, it doesn't scream. Restraint is luxury. |
| **Kinfolk** | Warm, human, considered. Every element earns its place. |
| **Cereal Magazine** | Editorial layouts, dramatic type scale, breathing room |
| **Anthropologie** | Organic textures, warm palette, approachable sophistication |

## 1.2 — What This Is NOT

| Banned Vibe | Why |
|-------------|-----|
| ClickFunnels energy | Desperate, loud, template-feeling |
| "BUY NOW" red buttons | Pressure tactics alienate our audience |
| Gradients everywhere | Dated, generic, screams "I used Canva" |
| Tiny text with big headlines only | Our audience can't read 14px body copy |
| Generic stock photography | Feels fake, breaks trust |
| Perfect symmetry everywhere | Boring, expected, template fingerprint |
| "Look at all this value!" stacking | Overwhelming, the opposite of calm |

## 1.3 — The Design Philosophy (Memorize This)

### Negative Space is the Luxury
Cheap designs fill every pixel. Expensive designs let things breathe. When in doubt, add more space, not more elements. The whitespace IS the design.

### Typography Does 80% of the Work
We're not relying on illustrations or flashy graphics. The typography itself should feel like art. Size contrast should be dramatic. Weight choices should be intentional.

### Restraint Over Decoration
One accent color, not five. One interaction pattern, not twelve. If you're about to add something decorative, ask "does this earn its place?"

### Warmth Without Cheese
The warmth comes from the color palette, the rounded corners, the generous spacing. NOT from excessive friendliness or emojis or "hey girl!" energy.

### Details That Reward Attention
The person who glances should think "that's nice." The person who looks closely should think "oh wow, they really thought about this."

---

# PART 2: THE BRAND SYSTEM

## 2.1 — Color Palette

```css
:root {
  /* ═══════════════════════════════════════════════════════════
     BACKGROUNDS — The Canvas
     ═══════════════════════════════════════════════════════════ */
  --bg-cream: #FAF8F5;           /* Primary background — warm, not stark */
  --bg-warm: #F5F1EB;            /* Alternate sections — slight depth */
  --bg-sand: #EDE8E0;            /* Cards, containers — subtle separation */
  --bg-card: #FFFFFF;            /* Card surfaces — clean white */
  
  /* ═══════════════════════════════════════════════════════════
     TEXT — The Voice
     ═══════════════════════════════════════════════════════════ */
  --text-primary: #2D2A26;       /* Headlines, important text — warm charcoal */
  --text-body: #3D3935;          /* Body copy — slightly lighter, very readable */
  --text-secondary: #6B635A;     /* Supporting text — muted brown */
  --text-muted: #8A847B;         /* Tertiary text — quiet */
  --text-faint: #A9A49C;         /* Microcopy — whisper */
  
  /* ═══════════════════════════════════════════════════════════
     ACCENT — The Spark
     ═══════════════════════════════════════════════════════════ */
  --accent-coral: #E07A5F;       /* Primary CTA, highlights — warm coral */
  --accent-coral-hover: #C96A52; /* CTA hover state — deeper coral */
  --accent-coral-soft: rgba(224, 122, 95, 0.1);  /* Soft backgrounds */
  --accent-coral-glow: rgba(224, 122, 95, 0.25); /* Button shadows */
  
  --accent-teal: #1D6B6B;        /* Links, secondary actions — deep teal */
  --accent-teal-hover: #165656;  /* Link hover — darker teal */
  --accent-teal-soft: rgba(29, 107, 107, 0.08); /* Teal backgrounds */
  
  /* ═══════════════════════════════════════════════════════════
     BORDERS & SHADOWS — The Depth
     ═══════════════════════════════════════════════════════════ */
  --border-light: #E8E2D9;       /* Subtle borders — warm taupe */
  --border-medium: #D9D2C7;      /* Stronger borders — still warm */
  --border-dark: #C5BDB2;        /* Emphasis borders */
  
  /* Shadows should feel like natural light, not Photoshop defaults */
  --shadow-xs: 0 1px 2px rgba(45, 42, 38, 0.04);
  --shadow-sm: 0 2px 8px rgba(45, 42, 38, 0.06);
  --shadow-md: 0 4px 16px rgba(45, 42, 38, 0.08);
  --shadow-lg: 0 8px 32px rgba(45, 42, 38, 0.10);
  --shadow-xl: 0 16px 48px rgba(45, 42, 38, 0.12);
  
  /* Card shadow — multi-layer for realism */
  --shadow-card: 
    0 2px 4px rgba(45, 42, 38, 0.02),
    0 4px 12px rgba(45, 42, 38, 0.04),
    0 12px 32px rgba(45, 42, 38, 0.06),
    0 24px 56px rgba(45, 42, 38, 0.04);
  
  /* ═══════════════════════════════════════════════════════════
     SPECIAL — Organic Warmth
     ═══════════════════════════════════════════════════════════ */
  --watercolor-coral: rgba(224, 122, 95, 0.06);
  --watercolor-teal: rgba(29, 107, 107, 0.04);
  --watercolor-warm: rgba(216, 195, 182, 0.12);
}
```

### Color Rules

1. **Never use pure black (#000000)** — Always warm charcoal
2. **Never use pure white (#FFFFFF) for backgrounds** — Always warm cream (cards can be white)
3. **Coral is precious** — Use only for CTAs and key highlights. If everything is coral, nothing is.
4. **Teal is for trust** — Links, secondary actions, anything that needs credibility
5. **When in doubt, add warmth** — Every color should feel like it sat in sunlight

## 2.2 — Typography System

### Font Stack (MUST BE BASE64 EMBEDDED)

```css
/* ═══════════════════════════════════════════════════════════
   CRITICAL: These fonts MUST be embedded as base64
   Do NOT use system fonts as fallback for production
   ═══════════════════════════════════════════════════════════ */

@font-face {
  font-family: 'OGG';
  src: url(data:font/woff2;base64,/* FULL BASE64 STRING HERE */) format('woff2');
  font-weight: 700;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: 'Satoshi';
  src: url(data:font/woff2;base64,/* FULL BASE64 STRING HERE */) format('woff2');
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: 'Satoshi';
  src: url(data:font/woff2;base64,/* FULL BASE64 STRING HERE */) format('woff2');
  font-weight: 500;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: 'Satoshi';
  src: url(data:font/woff2;base64,/* FULL BASE64 STRING HERE */) format('woff2');
  font-weight: 700;
  font-style: normal;
  font-display: swap;
}
```

### Type Scale (THE SIZES ARE NON-NEGOTIABLE)

| Element | Desktop | Tablet | Mobile | Font | Weight | Line Height | Letter Spacing |
|---------|---------|--------|--------|------|--------|-------------|----------------|
| **H1 (Hero)** | 72px | 56px | 40px | OGG | 700 | 1.1 | -0.02em |
| **H2 (Section)** | 48px | 40px | 32px | OGG | 700 | 1.15 | -0.01em |
| **H3 (Subsection)** | 32px | 28px | 24px | OGG | 700 | 1.2 | 0 |
| **H4 (Card Title)** | 24px | 22px | 20px | Satoshi | 700 | 1.3 | 0 |
| **Body Large** | 20px | 18px | 17px | Satoshi | 400 | 1.7 | 0.01em |
| **Body** | 18px | 17px | 16px | Satoshi | 400 | 1.7 | 0.01em |
| **Body Small** | 16px | 15px | 15px | Satoshi | 400 | 1.6 | 0.01em |
| **Label** | 14px | 13px | 12px | Satoshi | 500 | 1.4 | 0.08em (uppercase) |
| **Caption** | 14px | 13px | 13px | Satoshi | 400 | 1.5 | 0.02em |
| **Micro** | 12px | 12px | 11px | Satoshi | 400 | 1.4 | 0.02em |
| **CTA Button** | 18px | 16px | 16px | Satoshi | 700 | 1 | 0.04em (uppercase) |

### Typography Rules

1. **H1 is the star** — It should feel BIG. Take up space. Editorial.
2. **Body text minimum 16px on mobile** — Our audience needs readable text
3. **Trust row/labels in uppercase** with generous letter-spacing (0.08em+)
4. **Tight letter-spacing on headlines** (-0.02em), looser on small text
5. **Never use more than 3 text sizes per section** (excluding tiny labels)

## 2.3 — Spacing System

```css
:root {
  /* Base unit: 8px */
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 20px;
  --space-6: 24px;
  --space-8: 32px;
  --space-10: 40px;
  --space-12: 48px;
  --space-16: 64px;
  --space-20: 80px;
  --space-24: 96px;
  --space-32: 128px;
  
  /* Section padding */
  --section-padding-y: var(--space-24);      /* 96px desktop */
  --section-padding-y-mobile: var(--space-16); /* 64px mobile */
  
  /* Container */
  --container-max: 1200px;
  --container-narrow: 800px;
  --container-text: 680px;
  --container-padding: var(--space-12);      /* 48px */
  --container-padding-mobile: var(--space-6); /* 24px */
}
```

### Spacing Philosophy

- **Generous, not cramped** — Let things breathe
- **Consistent rhythm** — Use the scale, don't invent random values
- **Bigger gaps between sections** than within sections
- **Mobile gets ~70% of desktop spacing** (not 50%, not 100%)

## 2.4 — Border Radius System

```css
:root {
  --radius-sm: 8px;    /* Small elements, tags */
  --radius-md: 12px;   /* Buttons, inputs */
  --radius-lg: 16px;   /* Cards, containers */
  --radius-xl: 20px;   /* Large cards, hero elements */
  --radius-2xl: 24px;  /* Feature cards, major containers */
  --radius-full: 9999px; /* Pills, avatars */
}
```

---

# PART 3: PAGE ARCHITECTURE

## 3.1 — Section Map

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  STICKY HEADER (appears after hero CTA leaves viewport)            ┃
┃  → Hidden initially, slides down smoothly                          ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  SECTION 1: HERO                                                    ┃
┃  ─────────────────────────────────────────────────────────────────  ┃
┃  JOB: Stop the scroll. Make them feel "this is different."          ┃
┃  COMPONENTS:                                                        ┃
┃    • Utility bar (name + help link)                                 ┃
┃    • Trust row (387K sales, $1M+, still runs shop)                  ┃
┃    • Preheader (audience identification)                            ┃
┃    • H1 Headline (the big promise)                                  ┃
┃    • Subhead (expand the promise)                                   ┃
┃    • Two-column: Video + Offer Card                                 ┃
┃    • Start here micro-line                                          ┃
┃  BACKGROUND: Cream with subtle watercolor texture                   ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  SECTION 2: WHAT'S INCLUDED                                         ┃
┃  ─────────────────────────────────────────────────────────────────  ┃
┃  JOB: Show the value stack. Make them feel "this is a lot."         ┃
┃  COMPONENTS:                                                        ┃
┃    • Section headline                                               ┃
┃    • 3 Pillars with deliverables:                                   ┃
┃      → Pillar 1: Products & Niche (stop wondering what to sell)     ┃
┃      → Pillar 2: AI Design (make sellable designs fast)             ┃
┃      → Pillar 3: Traffic (algorithm-proof your shop)                ┃
┃    • Bonus items (if applicable)                                    ┃
┃    • Secondary CTA                                                  ┃
┃  BACKGROUND: Alternate warm background                              ┃
┃  LAYOUT: NOT equal cards. Hierarchy within the grid.                ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  SECTION 3: SOCIAL PROOF STRIP                                      ┃
┃  ─────────────────────────────────────────────────────────────────  ┃
┃  JOB: Quick credibility boost. 3-6 short testimonials.              ┃
┃  FORMAT: Horizontal strip, compact, scannable                       ┃
┃  STYLE: Names + results + 1-2 line quotes                          ┃
┃  BACKGROUND: Cream or subtle teal tint                              ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  SECTION 4: THE STORY                                               ┃
┃  ─────────────────────────────────────────────────────────────────  ┃
┃  JOB: Build connection. "She gets it. She's been there."            ┃
┃  COMPONENTS:                                                        ┃
┃    • Bailey's journey (relatable pain → discovery → results)        ┃
┃    • Key numbers woven in naturally                                 ┃
┃    • Transition to "now I show others"                              ┃
┃  STYLE: Text-forward, intimate, conversational                      ┃
┃  BACKGROUND: Cream                                                  ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  SECTION 5: SOCIAL PROOF (EXPANDED)                                 ┃
┃  ─────────────────────────────────────────────────────────────────  ┃
┃  JOB: Overcome skepticism. "Real people, real results."             ┃
┃  FORMAT: Mixed layout — featured testimonials + grid                ┃
┃  STYLE: Story-driven, results highlighted, feels like case studies  ┃
┃  INCLUDE: Screenshots, specific numbers, transformation arcs        ┃
┃  BACKGROUND: Alternate warm                                         ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  SECTION 6: THE PITCH / OFFER RECAP                                 ┃
┃  ─────────────────────────────────────────────────────────────────  ┃
┃  JOB: Re-summarize everything. Make the decision feel obvious.      ┃
┃  COMPONENTS:                                                        ┃
┃    • "Here's what you get" recap (visual value stack)               ┃
┃    • Price reveal with framing ($67/month = ~$2/day)                ┃
┃    • Guarantee statement                                            ┃
┃    • Primary CTA (large, unmissable)                                ┃
┃  STYLE: Card-based, premium feeling, clear hierarchy                ┃
┃  BACKGROUND: Cream with subtle depth                                ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  SECTION 7: FAQ                                                     ┃
┃  ─────────────────────────────────────────────────────────────────  ┃
┃  JOB: Handle remaining objections. Remove final friction.           ┃
┃  FORMAT: Accordion or inline (test which feels better)              ┃
┃  STYLE: Questions feel conversational, answers are concise          ┃
┃  BACKGROUND: Alternate warm                                         ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  SECTION 8: FINAL CLOSE                                             ┃
┃  ─────────────────────────────────────────────────────────────────  ┃
┃  JOB: Last chance. Create "two paths" moment.                       ┃
┃  COMPONENTS:                                                        ┃
┃    • Recap the transformation promise                               ┃
┃    • Final CTA (THE dominant element)                               ┃
┃    • Reassurance line                                               ┃
┃    • Optional: Bailey signature/sign-off                            ┃
┃  BACKGROUND: Cream                                                  ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  FOOTER                                                             ┃
┃  Simple, clean. Links, copyright, nothing fancy.                    ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

---

# PART 4: SECTION-BY-SECTION SPECIFICATIONS

## SECTION 1: HERO

### Layout (Desktop)

```
Width: 100%
Max-content-width: 1200px
Padding: 0 48px

┌─────────────────────────────────────────────────────────────────────┐
│ UTILITY BAR                                                         │
│ Height: 56px                                                        │
│ [AI Design & Grow Experience]              [Questions? Email us]    │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│                         TRUST ROW                                   │
│     387K+ ETSY SALES  ·  $1M+ FROM DIGITAL PRODUCTS  ·              │
│                    YES, I STILL RUN MY SHOP                         │
│                                                                     │
│               ═══════════ (hairline) ═══════════                    │
│                                                                     │
│                         PREHEADER                                   │
│         For busy people who want Etsy income                        │
│                    without Etsy stress.                             │
│                                                                     │
│                                                                     │
│                            H1                                       │
│           I'll show you what I actually sell                        │
│         on Etsy and how I'd do it again today.                      │
│                                                                     │
│                                                                     │
│                          SUBHEAD                                    │
│              (max-width: 720px, centered)                           │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   ┌───────────────────────┐      ┌──────────────────────────────┐  │
│   │                       │      │                              │  │
│   │                       │      │        OFFER CARD            │  │
│   │       VIDEO           │      │                              │  │
│   │                       │      │   • Bullet 1                 │  │
│   │    (16:9 ratio)       │      │   • Bullet 2                 │  │
│   │   (min-height 420px)  │      │   • Bullet 3                 │  │
│   │                       │      │   • Bullet 4                 │  │
│   │                       │      │   • Bullet 5                 │  │
│   │                       │      │                              │  │
│   │                       │      │   + Plus line                │  │
│   │                       │      │                              │  │
│   │                       │      │   ┌────────────────────┐     │  │
│   │                       │      │   │ START SELLING NOW  │     │  │
│   │                       │      │   └────────────────────┘     │  │
│   │                       │      │                              │  │
│   │                       │      │   $67/mo · Instant access    │  │
│   │                       │      │                              │  │
│   │                       │      │   See everything included →  │  │
│   └───────────────────────┘      └──────────────────────────────┘  │
│                                                                     │
│   Column split: 55% video / 45% card                                │
│   Gap: 48px                                                         │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│        Start here: 15 minute setup, then pick your                  │
│                  first product tonight.                             │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Exact Copy for Hero

**Utility Bar Left:** `AI Design & Grow Experience`
**Utility Bar Right:** `Questions? Email us` (link "Email us" to mailto)

**Trust Row:** `387K+ ETSY SALES  ·  $1M+ FROM DIGITAL PRODUCTS  ·  YES, I STILL RUN MY SHOP`

**Preheader:** `For busy people who want Etsy income without Etsy stress.`

**H1:** 
```
I'll show you what I actually sell
on Etsy and how I'd do it again today.
```
(Line break after "sell" is intentional)

**Subhead:** `I spent years learning what actually moves on Etsy. Now you get the shortcuts I earned: the product decisions, the listing recipe, and the traffic routine I use when Etsy's algorithm gets moody, plus the steps I use to grow beyond Etsy too. Borrow my experience so you start with what I know works.`

**Bullets (in offer card):**
1. `Every morning I post what I would sell next, the exact AI prompt I'd use, and the tags and titles I'd list it with. You pick one and go.`
2. `Choose your path to $5K per month based on your life: audience, bundles, or social, with the same decision rules I used to scale.`
3. `My full $10K shop formula, plus the traffic routine I lean on so sales don't disappear when Etsy traffic dips.`
4. `Pinterest setup the way I actually run it, so you are not relying on Etsy search as your only source of buyers.`
5. `Twice-monthly calls to get real feedback and get unstuck fast. Ask me anything, leave with a clear next move.`

**Plus Line:** `Plus the PLR vault, the build with me shop, the full tools library, and more.`

**CTA Button:** `START SELLING NOW`

**Microcopy:** `$67/month  ·  Instant access  ·  Cancel anytime`

**Reassurance:** `Everything's included. No surprises.`

**Soft Urgency:** `Price goes up as we add more.`

**Secondary Link:** `See everything included`

**Start Here Line:** `Start here: 15 minute setup, then pick your first product tonight.`

### Hero Component Specifications

#### Utility Bar
```css
.utility-bar {
  width: 100%;
  height: 56px;
  background: var(--bg-cream);
  border-bottom: 1px solid var(--border-light);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 48px;
}

.utility-bar__logo {
  font-family: 'Satoshi', sans-serif;
  font-weight: 500;
  font-size: 14px;
  color: var(--text-primary);
  letter-spacing: 0.02em;
}

.utility-bar__help {
  font-family: 'Satoshi', sans-serif;
  font-weight: 400;
  font-size: 14px;
  color: var(--text-secondary);
}

.utility-bar__help a {
  color: var(--accent-teal);
  text-decoration: none;
  position: relative;
}

.utility-bar__help a::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 0;
  height: 1px;
  background: currentColor;
  transition: width 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.utility-bar__help a:hover::after {
  width: 100%;
}
```

#### Trust Row
```css
.trust-row {
  text-align: center;
  padding: 40px 0 32px;
}

.trust-row__text {
  font-family: 'Satoshi', sans-serif;
  font-weight: 500;
  font-size: 14px;
  color: var(--text-secondary);
  text-transform: uppercase;
  letter-spacing: 0.12em;
}

/* Middot separators */
.trust-row__separator {
  margin: 0 16px;
  opacity: 0.4;
}

/* Hairline below */
.trust-row__line {
  width: 80px;
  height: 1px;
  margin: 28px auto 0;
  background: linear-gradient(90deg, transparent, var(--border-medium), transparent);
}
```

#### Headline
```css
.headline {
  text-align: center;
  padding: 24px 24px 0;
  max-width: 900px;
  margin: 0 auto;
}

.headline__text {
  font-family: 'OGG', Georgia, serif;
  font-weight: 700;
  font-size: 72px;
  line-height: 1.1;
  color: var(--text-primary);
  letter-spacing: -0.02em;
}

@media (max-width: 1024px) {
  .headline__text {
    font-size: 56px;
  }
}

@media (max-width: 768px) {
  .headline__text {
    font-size: 44px;
  }
}

@media (max-width: 480px) {
  .headline__text {
    font-size: 36px;
  }
}
```

#### Offer Card
```css
.offer-card {
  background: var(--bg-card);
  border: 1px solid var(--border-light);
  border-radius: 24px;
  padding: 40px;
  box-shadow: var(--shadow-card);
  position: relative;
}

/* Subtle top highlight for depth */
.offer-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 24px;
  right: 24px;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.9), transparent);
  border-radius: 24px 24px 0 0;
}
```

#### Bullets
```css
.offer-bullets {
  list-style: none;
  padding: 0;
  margin: 0 0 24px 0;
}

.offer-bullets__item {
  display: flex;
  gap: 16px;
  padding: 16px 0;
  border-bottom: 1px solid var(--border-light);
}

.offer-bullets__item:last-child {
  border-bottom: none;
}

/* Coral square markers */
.offer-bullets__marker {
  width: 8px;
  height: 8px;
  background: var(--accent-coral);
  border-radius: 2px;
  flex-shrink: 0;
  margin-top: 8px;
}

.offer-bullets__text {
  font-family: 'Satoshi', sans-serif;
  font-weight: 400;
  font-size: 17px;
  line-height: 1.6;
  color: var(--text-body);
}
```

#### CTA Button
```css
.cta-button {
  width: 100%;
  background: var(--accent-coral);
  color: white;
  font-family: 'Satoshi', sans-serif;
  font-weight: 700;
  font-size: 18px;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  padding: 22px 32px;
  border: none;
  border-radius: 14px;
  cursor: pointer;
  box-shadow: 0 4px 16px var(--accent-coral-glow);
  transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
}

.cta-button:hover {
  background: var(--accent-coral-hover);
  transform: translateY(-2px);
  box-shadow: 0 8px 28px var(--accent-coral-glow);
}

.cta-button:active {
  transform: translateY(0);
}
```

#### Video Placeholder
```css
.video-container {
  position: relative;
  aspect-ratio: 16 / 9;
  min-height: 420px;
  background: linear-gradient(145deg, #EDE9E3 0%, #E2DED6 100%);
  border-radius: 20px;
  overflow: hidden;
  box-shadow: var(--shadow-card);
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Subtle noise texture */
.video-container::before {
  content: '';
  position: absolute;
  inset: 0;
  background: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E");
  opacity: 0.03;
  pointer-events: none;
}

.play-button {
  width: 80px;
  height: 80px;
  background: var(--bg-card);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 24px rgba(0,0,0,0.12);
  cursor: pointer;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.play-button:hover {
  transform: scale(1.08);
  box-shadow: 0 8px 32px rgba(0,0,0,0.16);
}

.play-button__icon {
  width: 0;
  height: 0;
  border-style: solid;
  border-width: 14px 0 14px 22px;
  border-color: transparent transparent transparent var(--accent-coral);
  margin-left: 6px;
}
```

### Watercolor Background Treatment

```css
.hero-section {
  position: relative;
  background: var(--bg-cream);
  overflow: hidden;
}

/* Soft watercolor blob - top right */
.hero-section::before {
  content: '';
  position: absolute;
  top: -15%;
  right: -8%;
  width: 55%;
  height: 65%;
  background: radial-gradient(
    ellipse at center,
    var(--watercolor-coral) 0%,
    rgba(224, 122, 95, 0.02) 45%,
    transparent 70%
  );
  pointer-events: none;
  z-index: 0;
}

/* Second blob - bottom left */
.hero-section::after {
  content: '';
  position: absolute;
  bottom: -25%;
  left: -12%;
  width: 45%;
  height: 55%;
  background: radial-gradient(
    ellipse at center,
    var(--watercolor-teal) 0%,
    transparent 60%
  );
  pointer-events: none;
  z-index: 0;
}

/* Content above blobs */
.hero-section > * {
  position: relative;
  z-index: 1;
}
```

---

## STICKY HEADER SPECIFICATION

### Behavior
- Hidden by default (transformed off-screen)
- Appears when hero CTA button scrolls out of viewport
- Uses Intersection Observer (not scroll events)
- Slides down smoothly with cubic-bezier easing
- Desktop: Fixed to top
- Mobile: Fixed to bottom

### Desktop Sticky Header
```css
.sticky-header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 64px;
  background: rgba(255, 255, 255, 0.92);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-bottom: 1px solid var(--border-light);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 48px;
  z-index: 1000;
  transform: translateY(-100%);
  opacity: 0;
  transition: 
    transform 0.4s cubic-bezier(0.4, 0, 0.2, 1), 
    opacity 0.3s ease;
}

.sticky-header.visible {
  transform: translateY(0);
  opacity: 1;
}

.sticky-header__logo {
  font-family: 'Satoshi', sans-serif;
  font-weight: 500;
  font-size: 14px;
  color: var(--text-primary);
}

.sticky-header__center {
  font-family: 'Satoshi', sans-serif;
  font-weight: 400;
  font-size: 14px;
  color: var(--text-secondary);
}

.sticky-header__cta {
  background: var(--accent-coral);
  color: white;
  font-family: 'Satoshi', sans-serif;
  font-weight: 700;
  font-size: 14px;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  padding: 12px 28px;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  transition: background 0.2s ease, transform 0.2s ease;
}

.sticky-header__cta:hover {
  background: var(--accent-coral-hover);
  transform: translateY(-1px);
}
```

### Mobile Sticky Header (Bottom)
```css
@media (max-width: 768px) {
  .sticky-header {
    top: auto;
    bottom: 0;
    height: auto;
    padding: 16px 24px;
    transform: translateY(100%);
    flex-direction: column;
    gap: 8px;
    border-bottom: none;
    border-top: 1px solid var(--border-light);
  }
  
  .sticky-header.visible {
    transform: translateY(0);
  }
  
  .sticky-header__logo,
  .sticky-header__center {
    display: none;
  }
  
  .sticky-header__cta {
    width: 100%;
    padding: 18px 24px;
    font-size: 16px;
  }
  
  /* Add price microcopy on mobile */
  .sticky-header__price {
    font-family: 'Satoshi', sans-serif;
    font-size: 13px;
    color: var(--text-secondary);
    text-align: center;
  }
}
```

### JavaScript for Sticky Header
```javascript
document.addEventListener('DOMContentLoaded', () => {
  const ctaButton = document.querySelector('.cta-button');
  const stickyHeader = document.querySelector('.sticky-header');
  
  if (!ctaButton || !stickyHeader) return;
  
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          stickyHeader.classList.remove('visible');
        } else {
          stickyHeader.classList.add('visible');
        }
      });
    },
    { 
      threshold: 0, 
      rootMargin: '-64px 0px 0px 0px' 
    }
  );
  
  observer.observe(ctaButton);
});
```

---

# PART 5: ANIMATION SYSTEM

## Philosophy
Motion should be **memorable at key moments**, not constant. Every animation needs a reason.

## Entry Animations (On Load)

```css
@keyframes fadeUp {
  from {
    opacity: 0;
    transform: translateY(16px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fade-up {
  animation: fadeUp 0.6s cubic-bezier(0.4, 0, 0.2, 1) forwards;
  opacity: 0;
}

/* Stagger delays */
.delay-1 { animation-delay: 0.1s; }
.delay-2 { animation-delay: 0.15s; }
.delay-3 { animation-delay: 0.2s; }
.delay-4 { animation-delay: 0.25s; }
.delay-5 { animation-delay: 0.3s; }
.delay-6 { animation-delay: 0.35s; }
```

## Scroll-Triggered Animations

Use Intersection Observer for scroll-triggered reveals:

```javascript
const observerOptions = {
  threshold: 0.1,
  rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('is-visible');
      observer.unobserve(entry.target);
    }
  });
}, observerOptions);

document.querySelectorAll('.animate-on-scroll').forEach(el => {
  observer.observe(el);
});
```

```css
.animate-on-scroll {
  opacity: 0;
  transform: translateY(24px);
  transition: opacity 0.6s cubic-bezier(0.4, 0, 0.2, 1),
              transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
}

.animate-on-scroll.is-visible {
  opacity: 1;
  transform: translateY(0);
}
```

## Hover States

```css
/* Links */
.link-hover {
  position: relative;
  transition: color 0.2s ease;
}

.link-hover::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 0;
  height: 1px;
  background: currentColor;
  transition: width 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.link-hover:hover::after {
  width: 100%;
}

/* Cards */
.card-hover {
  transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1),
              box-shadow 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.card-hover:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-xl);
}

/* Buttons */
.button-hover {
  transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
}

.button-hover:hover {
  transform: translateY(-2px);
}

.button-hover:active {
  transform: translateY(0);
}
```

## Respect Reduced Motion

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

# PART 6: RESPONSIVE BREAKPOINTS

```css
/* Mobile first approach */

/* Base = Mobile (< 640px) */

/* Small tablets */
@media (min-width: 640px) { /* sm */ }

/* Tablets */
@media (min-width: 768px) { /* md */ }

/* Small desktop */
@media (min-width: 1024px) { /* lg */ }

/* Desktop */
@media (min-width: 1280px) { /* xl */ }

/* Large desktop */
@media (min-width: 1536px) { /* 2xl */ }
```

## Mobile Rules (Non-Negotiable)

1. **Nothing side-by-side under 768px** — Stack everything
2. **Minimum touch target: 44px** — Buttons, links, interactive elements
3. **Buttons full-width on mobile**
4. **Text never below 15px on mobile** — Our audience needs readable text
5. **Reduce spacing by ~30%** on mobile, not 50%
6. **Container padding: 24px** on mobile (not 16px, too cramped)

---

# PART 7: QUALITY CHECKLIST

Before delivering ANY section, verify every item:

## Visual Quality
- [ ] Fonts are OGG and Satoshi (base64 embedded, NOT system fonts)
- [ ] H1 is at least 72px on desktop, 40px on mobile
- [ ] Body text is at least 17px on desktop, 16px on mobile
- [ ] Clear visual hierarchy — blur test passes
- [ ] Colors match the exact hex codes in the system
- [ ] Sufficient contrast for readability (4.5:1 minimum)
- [ ] Shadows feel like natural light, not harsh
- [ ] Border radius is consistent (uses the system)
- [ ] Spacing uses the defined scale

## Layout Quality
- [ ] Maximum content width is 1200px
- [ ] Text blocks max-width is 680-720px
- [ ] Asymmetry is intentional and balanced
- [ ] No generic equal-card grids
- [ ] Mobile stacks properly
- [ ] Touch targets are 44px minimum

## Animation Quality
- [ ] Animations have purpose (not decorative)
- [ ] Uses cubic-bezier easing (not linear/ease)
- [ ] Respects prefers-reduced-motion
- [ ] Sticky header uses Intersection Observer
- [ ] No janky or laggy movements

## Conversion Quality
- [ ] Section has ONE clear job
- [ ] CTA button is unmissable
- [ ] Copy is readable and scannable
- [ ] Bullets are visually distinct
- [ ] Secondary actions are clearly secondary

## Technical Quality
- [ ] Single HTML file with embedded CSS
- [ ] Semantic HTML structure
- [ ] No external dependencies (fonts are base64)
- [ ] Works at 1440px, 1024px, 768px, 375px
- [ ] No horizontal scroll at any breakpoint
- [ ] Clean, organized, commented code

## "Premium" Quality
- [ ] Could NOT exist on any generic template
- [ ] Has at least one moment that delights
- [ ] Someone would screenshot and share this
- [ ] Feels like it cost $15,000 to make

---

# PART 8: BANNED ELEMENTS

## Never Use These

| Banned | Why |
|--------|-----|
| Generic icon libraries (Heroicons, Lucide, etc.) | Template fingerprint |
| Equal-size card grids (3 cards, 4 cards) | Boring, expected |
| Pure black (#000000) | Cold, harsh |
| Pure white backgrounds (#FFFFFF) | Stark, clinical |
| System fonts | Brand death |
| Em dashes (—) | Client hates them |
| Linear easing on animations | Cheap feeling |
| Scroll-jacking | Frustrating UX |
| Autoplaying video with sound | Annoying |
| Pop-ups on load | Tacky |
| Fake countdown timers | Manipulative |
| "X people viewing this" | Scammy |
| Stock photos of random people | Fake |
| Emojis | Not Bailey's brand |

## Banned Copy Patterns

See the full banned words list provided separately. Key ones:

- No "game-changer," "unlock," "secret sauce"
- No "Here's the thing:" or "Let's be honest:"
- No "Transform your..." or "What if you could..."
- No "It's not about X, it's about Y" structures
- No "Sound familiar?" or "You're not alone"

---

# PART 9: FOR CLAUDE CODE

## Your Role

You're not just executing specs. You're the designer-developer hybrid who:
- Questions anything that feels wrong
- Improves on the specs when you see a better way
- Adds polish details we didn't think of
- Makes decisions that serve the design, not just follow instructions

## What We Expect

1. **Actually use OGG and Satoshi fonts** (base64 embedded)
2. **Make text readable** (our audience is 35-55, many need bigger text)
3. **Add visual warmth** (watercolor textures, organic shapes)
4. **Create depth** (multi-layer shadows, subtle gradients)
5. **Make the CTA pop** (it should be the obvious action)
6. **Tell us what you changed and why**

## Output Format

When you deliver:

1. Confirm fonts are properly embedded (show the @font-face declarations)
2. List any deviations from spec and your reasoning
3. Note any polish details you added
4. Flag any concerns or suggestions for v2

---

# PART 10: THE FINAL TEST

Before considering this done, ask yourself:

> "Would a busy 45-year-old mom, squinting at her phone at 10pm, immediately understand what this is, feel like it's for her, and find the button to join?"

If yes → Ship it.
If no → Keep refining.

---

**This document is the source of truth. Build something beautiful.**
