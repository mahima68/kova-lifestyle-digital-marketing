# Verification — 30 October 2026

## Content and source checks

- 30 proposed content days numbered 1–30.
- 30 unique keyword ideas.
- 57 search text assets across 3 ad groups, with 15 headlines and 4 descriptions per group.
- Headline and description character lengths checked against 30/90 limits.
- 11 valid SVG artworks and matching PNG exports.
- Synthetic funnel totals and ordering checked: leads ≤ sessions ≤ clicks ≤ impressions.
- 7 HTML pages checked for a single H1, a title and existing internal links.
- Main pages checked for a meta description and image alt text.
- JavaScript syntax checked for the campaign and tracking scripts.

## Browser checks

- Homepage visually reviewed at the default desktop viewport.
- Campaign homepage and landing page visually reviewed at a 390 × 844 mobile breakpoint, with no document-wide horizontal overflow.
- Carousel filter displayed 5 slides.
- Artwork viewer opened and showed caption, CTA and SVG/PNG download links.
- Calculator produced 600 clicks, 495 sessions and approximately 27 leads when the budget was changed to ₹6,000 with the other default assumptions.
- Oversized ad-group selection displayed the matching headline assets and character counts.
- Tagged campaign link opened the landing page with its UTM values.
- Oversized/Sage product exploration updated the visible response.
- Demo form succeeded with a sample email and explicitly confirmed that nothing was saved or sent.
- Returning to the case study displayed page_view, view_item and generate_lead with the selected product and campaign tags, without the sample email.
- No browser console errors were reported in the inspected log.
- Temporary viewport override was reset after testing.

## Limits of verification

No paid media, platform account, keyword volume, real lead delivery, search ranking, email deliverability or product claim was verified. No filmed reel exists. Hosted publication status is reported separately by Sites. Browser-local events are not GA4 events received by an analytics property.

## Additional pre-upload review

A second source/content pass and a new browser pass were completed before upload to GitHub.

- Rechecked all 7 page links, titles, H1s, main-page descriptions, image alt text, ad character counts and the 30-day/30-keyword/57-ad-asset/11-design counts.
- Checked both generated ZIP archives for corrupt entries.
- Named the artwork dialog and added explicit labels to filter selectors.
- Confirmed the Stories filter shows 3 designs and the dialog exposes the selected design's name.
- Confirmed the Email calendar filter shows 4 entries and an ad group shows 19 text assets.
- Checked the zero-budget calculator result: zero clicks, sessions and leads, with CPL undefined.
- Built a Google/CPC campaign link, explored Oversized/Women/Chalk and completed the demo signup with a sample address.
- Confirmed the local log showed the Google/CPC tags and selected concept product, without the sample email.
- Inspected the active marketing page at 390-pixel width with no document-wide horizontal overflow, then reset the temporary viewport.
- No console errors appeared in the inspected browser log.
- Clarified the standalone campaign-pack README so its server command matches the archive's directory layout.

No review can establish that a project has no undiscovered errors. Live ad delivery, actual lead storage, email sending and real business performance remain outside the project.
