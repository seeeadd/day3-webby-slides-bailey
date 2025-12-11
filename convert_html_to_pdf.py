#!/usr/bin/env python3
"""
HTML Slides to PDF Converter
Converts Day 3 HTML slides to PDF using Playwright with Chromium.

Requirements:
- printBackground: true (render all backgrounds)
- Screen media type (not print)
- Exact colors (no dark mode, no auto-adjustments)
- Base64 embedded fonts (Ogg, Satoshi)
- 1920x1080 viewport and page size
- No margins
- Scale: 1
"""

import asyncio
import os
import glob
import sys
from pathlib import Path

# Path to existing Chromium binary
CHROMIUM_PATH = os.path.expanduser('~/.cache/ms-playwright/chromium-1194/chrome-linux/chrome')

from playwright.async_api import async_playwright


async def convert_html_to_pdf(html_path: str, pdf_path: str):
    """Convert a single HTML file to PDF with exact visual fidelity."""

    print(f"Converting: {os.path.basename(html_path)}")

    async with async_playwright() as p:
        # Launch Chromium with specific settings to avoid color changes
        browser = await p.chromium.launch(
            headless=True,
            executable_path=CHROMIUM_PATH,  # Use existing Chromium binary
            args=[
                '--disable-gpu',
                '--disable-software-rasterizer',
                '--disable-dev-shm-usage',
                '--no-sandbox',
                '--disable-setuid-sandbox',
                # Disable any forced colors or dark mode
                '--force-color-profile=srgb',
                '--disable-features=ForcedColors',
                '--disable-features=DarkMode',
                '--disable-features=WebContentsForceDark',
            ]
        )

        # Create browser context with screen color scheme (not dark)
        context = await browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            device_scale_factor=1,
            color_scheme='light',  # Prevent dark mode
            forced_colors='none',  # No forced colors
        )

        page = await context.new_page()

        # Force screen media type (NOT print) to preserve all styles
        await page.emulate_media(media='screen', color_scheme='light')

        # Load the HTML file
        file_url = f'file://{os.path.abspath(html_path)}'
        await page.goto(file_url, wait_until='networkidle')

        # Wait for fonts to load
        await page.wait_for_timeout(2000)

        # Inject CSS to ensure print styles don't override screen styles
        # and to set up proper page breaks
        await page.add_style_tag(content='''
            /* Quick shadow kill switch */
            *,
            *::before,
            *::after {
                box-shadow: none !important;
                text-shadow: none !important;
                filter: none !important; /* kills drop-shadow() etc */
            }

            /* Force screen media styles for PDF */
            @media print {
                * {
                    -webkit-print-color-adjust: exact !important;
                    print-color-adjust: exact !important;
                    color-adjust: exact !important;
                }

                body {
                    -webkit-print-color-adjust: exact !important;
                    print-color-adjust: exact !important;
                }

                .slide {
                    page-break-after: always;
                    page-break-inside: avoid;
                    break-after: page;
                    break-inside: avoid;
                }

                .slide:last-child {
                    page-break-after: auto;
                }
            }

            /* Ensure slides break properly */
            .slide {
                page-break-after: always !important;
                page-break-inside: avoid !important;
            }

            .slide:last-child {
                page-break-after: auto !important;
            }
        ''')

        # Get slide count for logging
        slide_count = await page.evaluate('document.querySelectorAll(".slide").length')
        print(f"  Found {slide_count} slides")

        # Generate PDF with exact settings
        await page.pdf(
            path=pdf_path,
            # Use exact 1920x1080 dimensions (convert to inches at 96 DPI for PDF)
            # 1920px / 96 = 20 inches, 1080px / 96 = 11.25 inches
            width='1920px',
            height='1080px',
            # Critical: print backgrounds (colors, images, gradients)
            print_background=True,
            # Use CSS page size
            prefer_css_page_size=True,
            # No margins - let HTML handle layout
            margin={
                'top': '0',
                'right': '0',
                'bottom': '0',
                'left': '0'
            },
            # Scale 1:1
            scale=1,
            # No header/footer
            display_header_footer=False,
        )

        await browser.close()

    print(f"  Saved: {os.path.basename(pdf_path)}")
    return slide_count


async def main():
    """Convert all Day 3 HTML slide files to PDFs."""

    base_dir = Path(__file__).parent

    # Find all Day 3 HTML files (excluding MEGA COMPILED per user request)
    html_files = sorted(glob.glob(str(base_dir / 'DAY 3 slide*.html')))

    # Filter out the MEGA COMPILED file
    html_files = [f for f in html_files if 'MEGA COMPILED' not in f]

    if not html_files:
        print("No Day 3 HTML slide files found!")
        sys.exit(1)

    print(f"Found {len(html_files)} Day 3 HTML slide files to convert:\n")
    for f in html_files:
        print(f"  - {os.path.basename(f)}")
    print()

    # Create output directory for PDFs
    output_dir = base_dir / 'pdf_output'
    output_dir.mkdir(exist_ok=True)

    total_slides = 0

    for html_file in html_files:
        # Generate PDF filename
        html_name = os.path.basename(html_file)
        pdf_name = html_name.replace('.html', '.pdf')
        pdf_path = output_dir / pdf_name

        try:
            slides = await convert_html_to_pdf(html_file, str(pdf_path))
            total_slides += slides
        except Exception as e:
            print(f"  ERROR: {e}")
            continue

    print(f"\n{'='*60}")
    print(f"Conversion complete!")
    print(f"Total slides converted: {total_slides}")
    print(f"PDF files saved to: {output_dir}")
    print(f"{'='*60}")


if __name__ == '__main__':
    asyncio.run(main())
