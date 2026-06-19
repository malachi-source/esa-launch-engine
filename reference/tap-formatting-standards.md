# TAP Document Formatting Standards

## Page Rules
- Sections NEVER break across pages. The section header and all its content must stay together.
- If a section won't fit on the current page, the ENTIRE section moves to the next page.
- 5-7 pages total (including cover page). No padding.

## Design Quality
- Fortune 500 level design: gold accent bars, branded tables, dark callout boxes, full branded cover page
- Client brand colors throughout (from form fields 48-50: primary, secondary, accent)
- Navy headers on tables with alternating row shading
- Compact fonts: 8.5-9pt for body/tables to keep within page limits

## Technical Implementation (python-docx)
- Set `cantSplit` on ALL table rows so tables cannot break across pages
- Set `keepNext` and `keepLines` on all paragraphs within a section
- Only release `keepNext` on the LAST element of each section (allowing breaks between sections)
- Margins: 0.6" top, 0.5" bottom, 0.85" left/right
