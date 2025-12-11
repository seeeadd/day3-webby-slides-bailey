#!/usr/bin/env python3
"""
Merge all Day 3 slide PDFs into a single combined PDF.
"""

import os
import re
from pathlib import Path
from PyPDF2 import PdfMerger, PdfReader


def extract_slide_range(filename):
    """Extract starting slide number from filename for sorting."""
    # Match patterns like "slides 1-12", "slide 131", "slides 20-27d"
    match = re.search(r'slides?\s*(\d+)', filename, re.IGNORECASE)
    if match:
        return int(match.group(1))
    return 999999  # Put unmatched at end


def main():
    base_dir = Path(__file__).parent
    pdf_dir = base_dir / 'pdf_output'

    # Find all Day 3 PDFs
    pdf_files = list(pdf_dir.glob('DAY 3*.pdf'))

    if not pdf_files:
        print("No Day 3 PDF files found in pdf_output/")
        return

    # Sort by slide number
    pdf_files.sort(key=lambda f: extract_slide_range(f.name))

    print(f"Found {len(pdf_files)} Day 3 PDF files to merge:\n")

    merger = PdfMerger()
    total_pages = 0

    for pdf_file in pdf_files:
        reader = PdfReader(str(pdf_file))
        page_count = len(reader.pages)
        total_pages += page_count
        print(f"  {pdf_file.name} ({page_count} pages)")
        merger.append(str(pdf_file))

    # Output path
    output_path = base_dir / 'DAY 3 - Complete Slides.pdf'

    # Write merged PDF
    merger.write(str(output_path))
    merger.close()

    print(f"\n{'='*60}")
    print(f"Merged PDF created: {output_path.name}")
    print(f"Total pages: {total_pages}")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()
