
COLLISION REPORT
================

## Renamed Keyframes

### featured-in-lto.html
  - shimmer → featured-shimmer
  - sparkle-pulse → featured-sparkle-pulse

### offer low ticket.html
  - shimmer → offer-shimmer
  - twinkle → offer-twinkle

### story low ticket.html
  - twinkle → story-twinkle

### testimonials low ticket.html
  - dot-pulse → testimonials-dot-pulse

### offer stack low ticket.html
  - dot-pulse → stack-dot-pulse

### final close low ticket.html
  - sparkle-pulse → close-sparkle-pulse

## Renamed IDs
  - No ID duplicates found across files (no renaming needed)

## Consolidated Root Variables
  - Variables from hero-lto.html, offer low ticket.html, and testimonials low ticket.html
    were consolidated into a single :root block
  - Common variables: --coral, --teal, --gold, --bg-cream, --bg-warm,
    --text-primary, --text-secondary, --text-body, --text-muted, etc.

## Scoped JavaScript
  - testimonials low ticket.html: Wrapped in IIFE, selectors scoped to .sec-testimonials
  - offer stack low ticket.html: Wrapped in IIFE, selectors scoped to .sec-stack
  - faq low ticket.html: Wrapped in IIFE, selectors scoped to .sec-faq

## Section Wrappers Applied
  - hero → <section class="sec sec-hero" data-sec="hero">
  - featured → <section class="sec sec-featured" data-sec="featured">
  - offer → <section class="sec sec-offer" data-sec="offer">
  - story → <section class="sec sec-story" data-sec="story">
  - testimonials → <section class="sec sec-testimonials" data-sec="testimonials">
  - stack → <section class="sec sec-stack" data-sec="stack">
  - faq → <section class="sec sec-faq" data-sec="faq">
  - close → <section class="sec sec-close" data-sec="close">
  - footer → <footer class="sec sec-footer" data-sec="footer">
