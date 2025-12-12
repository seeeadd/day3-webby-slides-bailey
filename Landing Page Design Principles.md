# MASTER PROMPT: Section Building for High-Converting Sales Pages

> **Use this prompt when building ANY section of a sales page. Read completely before writing a single line of code.**

---

## PHASE 1: THINK BEFORE YOU BUILD

**STOP. Do not write code yet.**

Before generating any code, you must complete this creative thinking phase. This is not optional. The quality of the final output depends entirely on the quality of thinking that precedes it.

### 1.1 — Understand the Section's Job

Answer these questions in your thinking:

```
1. What is this section's ONE job? (If you can't name it in 5 words, you don't understand it yet)
2. What question is the reader asking when they arrive here?
3. What must they believe/feel/understand before scrolling past?
4. What's the emotional state I'm designing FOR? What emotional state should they leave with?
5. Where does this fit in the overall argument arc?
```

### 1.2 — Find the Creative Angle

Don't default to the obvious. Ask yourself:

```
1. What's the CLICHÉ way to present this? (Name it so you can avoid it)
2. What would make someone stop and think "huh, I've never seen it done this way"?
3. What visual METAPHOR could represent this concept? (Not literal, metaphorical)
4. What composition would create TENSION or INTRIGUE?
5. What small detail could reward someone who's paying attention?
6. How can the LAYOUT itself reinforce the MESSAGE? (Form follows function)
```

### 1.3 — Plan the Visual Hierarchy

Before any code, sketch mentally:

```
1. What's the DOMINANT element? (The thing that captures 60% of attention)
2. What's the SUPPORTING element? (Adds context, 30% attention)
3. What's the DETAIL layer? (Rewards close inspection, 10% attention)
4. What's the EYE PATH? (Entry point → Journey → Exit/CTA)
5. Where does ASYMMETRY create interest without chaos?
```

---

## PHASE 2: DESIGN PRINCIPLES (Non-Negotiable)

### 2.1 — The "Underrated Genius" Standard

Every section must pass this test: **"Could this section exist on ANY course launch page, or could it ONLY exist on THIS page for THIS offer?"**

**PURSUE:**
- Hyper-contextual graphics that reference the specific offer, audience, or creator
- Intentional imperfection — hand-drawn elements, organic shapes, slight asymmetry
- Unexpected compositions — break the grid in controlled ways, overlap layers, off-center placements
- "Easter eggs" — clever details that reward attention without demanding it
- Typography as design — headlines with personality, not just "big text"
- Depth through craft — textures, layered backgrounds, considered shadows
- Section transitions that feel designed, not just "next section"

**AVOID AT ALL COSTS:**
- Generic icon libraries (Heroicons, Feather, FontAwesome, Lucide defaults)
- Predictable grids (3 equal cards, 4 equal cards, repeat)
- Corporate illustration styles ("blob people", generic SaaS graphics)
- Template spacing that every page uses
- Perfect symmetry everywhere
- Decorative elements that mean nothing (random shapes floating)
- Headlines sitting in plain rectangles
- UI components copied verbatim from any library

### 2.2 — Visual Hierarchy Rules

```
HIERARCHY = What appears important

You control this with:
├── SIZE (bigger = more important, but not everything can be big)
├── WEIGHT (bold draws eyes, use surgically)
├── SPACING (isolation creates importance, proximity creates relationship)
├── COLOR CONTRAST (high contrast = primary, low contrast = secondary)
├── POSITION (top-left anchors in western reading, center commands attention)
└── DEPTH (foreground vs background, shadows, layers)

THE TEST: If you blur your eyes, can you still tell what's most important?
If everything looks equally important, nothing is important.
```

### 2.3 — The Scroll Equation

```
Every scroll must:
├── ANSWER the question they had when they arrived at this section
├── CREATE a new question that pulls them to the next section
└── REWARD them with something worth the scroll (insight, visual delight, clarity)

If a section doesn't do all three → rethink it.
```

### 2.4 — Density Philosophy: Layered Richness

Not sparse minimalism. Not cluttered chaos. **Layered richness.**

```
Each section should have:
├── PRIMARY LAYER: The main message/visual (can't miss it)
├── SECONDARY LAYER: Supporting context (noticed on second look)
├── TEXTURE LAYER: Background depth, subtle patterns, ambient details
└── DELIGHT LAYER: Small moments that make it feel crafted

Think: A well-designed magazine spread, not a PowerPoint slide.
```

### 2.5 — Animation Philosophy: Statement Moments

Motion should be **memorable at key moments**, not constant.

```
USE ANIMATION FOR:
├── Section entrances (elements revealing with purpose)
├── Key insight moments (the "aha" should feel like an "aha")
├── Interactive feedback (hovers, clicks feel alive)
├── Scroll-triggered reveals (content earns attention as they commit)
└── Emphasis on transformations (before/after, price reveals, etc.)

DO NOT:
├── Animate everything (it becomes noise)
├── Use default ease-in-out for everything (boring)
├── Make them wait for content to appear (frustrating)
└── Distract from the message with motion (form over function)

EVERY ANIMATION SHOULD HAVE A REASON.
"It looks cool" is not a reason. "It emphasizes the transformation" is.
```

---

## PHASE 3: BRAND SYSTEM

### 3.1 — Color Palette (Black Friday Exclusive Edition)

```css
/* PRIMARY - The Foundation */
--chiffon-white: #FAF9F7;        /* Subtle warm white — primary background */
--dark-aqua: #1B4D4A;            /* Deep teal — headlines, primary text */
--light-aqua: #2D7A75;           /* Lighter teal — accents, interactive */

/* SECONDARY - Bailey's Warmth */
--matured-pink: #C17B7B;         /* Sophisticated dusty rose */
--soft-coral: #E8A598;           /* Warm accent moments */
--blush: #F5E6E0;                /* Pink-tinted neutrals */

/* ACCENT - Exclusive Feel */
--champagne: #F7E7CE;            /* Warm gold-adjacent */
--soft-gold: #D4AF37;            /* Subtle luxury moments (use sparingly) */

/* FUNCTIONAL */
--text-primary: #1B4D4A;         /* Dark aqua for main text */
--text-secondary: #5A7A78;       /* Muted teal for supporting text */
--text-muted: #8FA5A3;           /* Light teal for tertiary */

/* ILLUSTRATION PALETTE — Can expand but must harmonize */
Allow: Deeper teals, muted corals, warm creams, soft sage, dusty rose variations
Avoid: Neon anything, pure black, cold grays, saturated primaries
```

### 3.2 — Typography System

```css
/* HEADLINES — Ogg */
font-family: 'Ogg', serif;
/* Use: Bold or Black weight */
/* Character: Editorial, sophisticated, warm authority */
/* Sizes: 48-72px desktop, 32-48px mobile for main headlines */

/* BODY — Satoshi Variable */
font-family: 'Satoshi Variable', sans-serif;
/* Use: Medium weight (500) for body, Regular (400) for secondary */
/* Character: Modern, clean, friendly, readable */
/* Sizes: 18-20px desktop, 16-18px mobile */

/* MONO — For labels, tags, small caps moments */
font-family: 'JetBrains Mono', 'SF Mono', monospace;
/* Use: Uppercase, letter-spaced for labels like "STEP 1", "MODULE 3" */
/* Character: Technical credibility, structured */
/* Sizes: 11-14px, always letter-spaced (0.1em+) */

/* HANDWRITTEN — For personality moments */
/* Use: Annotations, callouts, "authentic" moments */
/* Character: Personal, Bailey's voice, human */
/* Apply to: Key phrases, margin notes, emphasis that feels personal */
/* Create these as SVG paths or use a script font sparingly */
```

### 3.3 — Visual Motifs (Use Contextually)

```
ALLOWED MOTIFS:
├── Dollar signs (styled, not emoji) — for value/money moments
├── Sparkles/glows — luxury feel, "aha" moments, special elements
├── Stars — success, premium, standout features
├── Organic shapes — blobs, waves for backgrounds (not generic, make them custom)
├── Hand-drawn underlines — emphasis, Bailey's personal touch
├── Tape/sticky notes — annotations, "real" feeling additions
├── Circles/rings — highlighting, calling attention
├── Arrows (hand-drawn style) — directing attention, flow
└── Stamps/badges — exclusivity, guarantees, "this page only"

RULES:
- Every motif must serve a PURPOSE (emphasis, direction, delight)
- No floating decorations that don't relate to content
- Contextual > decorative (a dollar sign near pricing = good, random dollar sign = bad)
- Quality > quantity (one perfect sparkle > five generic ones)
```

---

## PHASE 4: CUSTOM GRAPHICS MANDATE

### 4.1 — The Rule

**Every graphic must be custom-made for this specific context. Zero exceptions.**

When you need a visual element, you CREATE it as a custom SVG that:
1. Directly relates to the copy/concept it supports
2. Could only exist on THIS page for THIS offer
3. Uses the brand color palette (or harmonious illustration extensions)
4. Has enough detail to feel crafted, not enough to feel cluttered
5. Works at the size it will be displayed

### 4.2 — Graphic Types to Create

```
ILLUSTRATIONS:
├── Product representations (what they're getting, visualized)
├── Concept visualizations (abstract ideas made tangible)
├── Process diagrams (steps, flows, timelines)
├── Comparison visuals (before/after, this vs that)
└── Metaphor illustrations (the concept as a visual story)

UI GRAPHICS:
├── Custom bullets (not circles, not checkmarks — something better)
├── Section dividers (not just lines)
├── Background shapes (organic, layered, purposeful)
├── Highlight treatments (not just yellow highlighter)
└── Card treatments (borders, corners, shadows — all custom)

TYPOGRAPHIC GRAPHICS:
├── Stylized headlines (type as image when needed)
├── Pull quotes with personality
├── Handwritten annotations
├── Emphasized phrases (inline treatments)
└── Labels and badges
```

### 4.3 — Illustration Style Guide

```
THE VIBE: Editorial whimsy meets practical clarity

CHARACTERISTICS:
├── Literal enough to understand (you know what it IS)
├── Whimsical enough to delight (it has PERSONALITY)
├── Detailed enough to feel crafted (time was spent)
├── Simple enough to not overwhelm (serves the message)

TECHNIQUES:
├── Mix geometric and organic shapes
├── Use stroke + fill combinations
├── Layer elements for depth
├── Add small imperfections (slightly uneven lines, organic curves)
├── Include contextual details (Etsy references, product hints, Bailey's world)

COLOR APPLICATION:
├── Primary color for main shapes
├── Secondary colors for accents and details
├── Soft shadows for depth (not harsh drop shadows)
├── Occasional gold/sparkle for premium moments
```

---

## PHASE 5: LAYOUT PATTERNS

### 5.1 — Asymmetry Framework

Asymmetry creates visual interest. But controlled asymmetry, not chaos.

```
TECHNIQUES:
├── Off-center headlines (not always centered)
├── Unequal columns (60/40 or 70/30 splits)
├── Overlapping elements (images crossing section boundaries)
├── Varied card sizes in grids (one big, two small)
├── Staggered vertical rhythm (not everything aligned to same baseline)
├── Elements breaking the container edge

THE RULE: Every asymmetric choice needs a BALANCING element.
If headline is left, balance with a visual right.
If one card is big, the others should feel intentionally smaller.
Tension, not chaos.
```

### 5.2 — Section Pattern Library

Not rigid templates — starting points to subvert and customize.

```
PATTERN: HERO
├── Dominant headline (Ogg, large, can be multi-line)
├── Supporting context line (Satoshi, smaller)
├── Primary visual OR pattern-interrupt element
├── NO CTA in hero (unless it's above-fold sales page)
├── Scroll invitation (subtle, not "scroll down" text)

PATTERN: STORY/PAIN
├── Text-forward (copy does the work)
├── One supporting visual that COMPLETES the thought
├── Emotional resonance > information density
├── Reader should be nodding

PATTERN: PARADIGM SHIFT
├── Before/After or Old Way/New Way structure
├── Visual comparison (table, split screen, transformation graphic)
├── The "reframe" should hit visually, not just in words

PATTERN: FEATURE/PILLAR CARDS
├── NOT equal-size cards in a row
├── Hierarchy even within the grid (one featured, others supporting)
├── Each card has a custom illustration (never generic icons)
├── Cards feel like products, not list items

PATTERN: PROOF/TESTIMONIALS
├── Story-driven (context, not just quote)
├── Visual variety in presentation
├── Results highlighted typographically
├── Feels like case studies, not reviews

PATTERN: COMPARISON TABLE
├── Clear "winner" column (visually emphasized)
├── Not a boring HTML table
├── Styled rows, custom checkmarks, visual hierarchy
├── The choice should feel obvious

PATTERN: PRICE/OFFER
├── Treat like a "product card" — framed, special
├── Value stack visualization (not just a bullet list)
├── Price has visual treatment (crossed out, emphasized, etc.)
├── Guarantee badge/element nearby
├── CTA is unmissable

PATTERN: FAQ
├── Not default accordion styling
├── Questions feel conversational
├── Answers are concise, personality intact
├── Consider: Do they all need to expand? Some could be inline.

PATTERN: FINAL CTA
├── Recaps the transformation promise
├── Button is THE dominant element
├── Creates "two choices" tension if appropriate
├── After-CTA element (signature, reassurance, etc.)
```

### 5.3 — Mobile-First Structure

```
RULES:
├── Design mobile first, enhance for desktop
├── One dominant element per screen-height
├── No side-by-side elements under 768px (stack everything)
├── Touch targets minimum 44px
├── Buttons full-width on mobile
├── Text size never below 16px on mobile (no tiny text)

DESKTOP ENHANCEMENTS:
├── Use horizontal space for comparisons
├── Multi-column layouts for proof/cards
├── More breathing room (but not too much)
├── Hover states add delight
├── Sticky elements optional
```

---

## PHASE 6: CONVERSION MECHANICS

### 6.1 — The Scroll Psychology

```
FOLD 1 (Hero): "What is this, and is it for me?"
→ Clear promise, audience identification, intrigue to continue

FOLD 2-3 (Pain): "Do they understand my situation?"
→ Resonance, "she gets it", emotional connection

FOLD 4 (Paradigm): "Is there actually a different way?"
→ Reframe, new possibility, hope

FOLD 5-6 (Solution): "What exactly is this thing?"
→ Clarity on the offer, the mechanism, the vehicle

FOLD 7-8 (Proof): "Does this actually work?"
→ Evidence, results, credibility

FOLD 9 (Offer): "What do I get and what does it cost?"
→ Value stack, price anchor, clear exchange

FOLD 10 (Risk): "What if it doesn't work for me?"
→ Guarantee, safety, objection handling

FOLD 11+ (Close): "Why should I act now?"
→ Scarcity, urgency, decision framing

EACH FOLD MUST EARN THE NEXT FOLD.
```

### 6.2 — CTA Strategy

```
PRIMARY CTA:
├── One style only (color, shape, size consistent)
├── Action-oriented label ("Join the Accelerator" not "Submit")
├── Appears after value is established (not too early)
├── Impossible to miss (contrast, size, position)
├── Repeats at strategic points (after proof, after guarantee, final)

MICRO-INTERACTIONS:
├── Hover state that feels alive (subtle scale, glow, color shift)
├── Click feedback (tactile feeling)
├── Consider pulse or subtle animation to draw eye

PLACEMENT:
├── After major "proof" moments
├── After price/value reveal
├── After guarantee
├── Final section (with "two paths" framing if appropriate)
├── NOT in hero (unless above-fold sales page)
├── NOT after every section (overkill)
```

### 6.3 — Urgency Elements

```
COUNTDOWN TIMER:
├── Real deadline (Black Friday end date)
├── Styled to match brand (not default red urgency)
├── Positioned near CTA (reinforces action)
├── Not overwhelming, but visible

SCARCITY INDICATOR:
├── Stock/spots indicator if appropriate
├── Styled subtly (not flashing red alerts)
├── Near CTA or price section

VISUAL URGENCY (throughout):
├── "Black Friday Exclusive" badges
├── "This page only" treatments
├── Limited-time visual language
├── But NEVER scammy — authentic urgency only
```

---

## PHASE 7: TECHNICAL EXECUTION

### 7.1 — Stack

```
├── React components (Framer-compatible)
├── Tailwind CSS (utility-first, but custom where needed)
├── Custom SVG graphics (inline, not external files)
├── Framer Motion for animations
├── Mobile-first responsive design
```

### 7.2 — Component Structure

```jsx
// Every section should be a self-contained component
const SectionName = () => {
  return (
    <section className="relative [section-specific-classes]">
      {/* Background layer */}
      <div className="absolute inset-0 [background-treatment]">
        {/* Textures, shapes, ambient elements */}
      </div>
      
      {/* Content layer */}
      <div className="relative z-10 [container-classes]">
        {/* Actual content */}
      </div>
      
      {/* Decorative layer (if needed) */}
      <div className="absolute [positioned-decoratives]">
        {/* Floating elements, overlays */}
      </div>
    </section>
  )
}
```

### 7.3 — Animation Patterns

```jsx
// Scroll-triggered entrance (Framer Motion)
<motion.div
  initial={{ opacity: 0, y: 30 }}
  whileInView={{ opacity: 1, y: 0 }}
  viewport={{ once: true, margin: "-100px" }}
  transition={{ duration: 0.6, ease: [0.22, 1, 0.36, 1] }}
>
  {/* Content */}
</motion.div>

// Staggered children
<motion.div
  variants={{
    hidden: {},
    visible: { transition: { staggerChildren: 0.1 } }
  }}
  initial="hidden"
  whileInView="visible"
  viewport={{ once: true }}
>
  {items.map((item, i) => (
    <motion.div
      key={i}
      variants={{
        hidden: { opacity: 0, y: 20 },
        visible: { opacity: 1, y: 0 }
      }}
    >
      {item}
    </motion.div>
  ))}
</motion.div>

// Hover micro-interaction
<motion.button
  whileHover={{ scale: 1.02, boxShadow: "0 10px 40px rgba(27,77,74,0.2)" }}
  whileTap={{ scale: 0.98 }}
  transition={{ type: "spring", stiffness: 400, damping: 17 }}
>
  CTA Text
</motion.button>
```

### 7.4 — Responsive Breakpoints

```css
/* Mobile first — default styles are mobile */

/* Tablet */
@media (min-width: 768px) { /* md: */ }

/* Desktop */
@media (min-width: 1024px) { /* lg: */ }

/* Large desktop */
@media (min-width: 1280px) { /* xl: */ }

/* In Tailwind: */
/* Default = mobile */
/* md: = tablet */
/* lg: = desktop */
/* xl: = large screens */
```

---

## PHASE 8: QUALITY CHECKLIST

Before delivering ANY section, verify:

### Visual Quality
- [ ] No generic icons — all graphics are custom
- [ ] Clear visual hierarchy — blur test passes
- [ ] Asymmetry is intentional and balanced
- [ ] Colors match the brand system
- [ ] Typography is correctly applied
- [ ] Sufficient contrast for readability
- [ ] Animations have purpose

### Conversion Quality
- [ ] Section has ONE clear job
- [ ] Answers the question the reader has at this point
- [ ] Creates reason to keep scrolling
- [ ] CTA (if present) is unmissable
- [ ] Copy is supported, not overshadowed by design

### Technical Quality
- [ ] Mobile-first and fully responsive
- [ ] Clean, semantic HTML structure
- [ ] Performant (no huge images, efficient animations)
- [ ] Accessible (proper contrast, alt text, focus states)
- [ ] Code is organized and commented

### "Underrated Genius" Quality
- [ ] Could NOT exist on any other page (context-specific)
- [ ] Has at least one moment that delights
- [ ] No template fingerprints
- [ ] Someone would want to screenshot this and share

---

## PHASE 9: SECTION-SPECIFIC BRIEF

**Fill this out for each section before building:**

```
SECTION NAME: [Name]

JOB: [One sentence — what this section must accomplish]

READER'S QUESTION: [What are they asking when they arrive here?]

READER'S STATE → DESIRED STATE:
From: [How they feel arriving]
To: [How they should feel leaving]

DOMINANT ELEMENT: [What should capture most attention?]

COMPOSITION IDEA: [Initial layout concept — be specific]

ILLUSTRATION NEEDS: [What custom graphics are needed?]

UNIQUE ANGLE: [What makes this section NOT like every other version?]

ANIMATION MOMENTS: [Where does motion add meaning?]

CTA: [Yes/No — if yes, what label?]
```

---

## THE PRIME DIRECTIVE

When in doubt, return to this:

> **"Am I building something that makes someone stop scrolling and think 'holy shit, whoever made this actually cares'?"**

If the answer is "not quite" — you're not done yet.

The bar is not "good enough." The bar is "I've never seen a course sales page that looks like this, and now I want to buy just because of how premium it feels."

---

**Now proceed to Phase 1 for the specific section you're building.**
