# Batch consistency and quality control

## Lock the subject before varying scenes

Create a compact character or product bible. Separate fixed anchors from variables.

| Fixed anchors | Controlled variables |
|---|---|
| Adult age range, facial geometry, eye shape, nose and lip proportions, skin tone, hair cut and color, body proportions | Expression, pose, wardrobe, location, time, lens, action |
| Product silhouette, dimensions, materials, colors, controls, logo placement | Hand interaction, setting, surface, angle, supporting props |

Use the same approved reference image for every shot when the tool supports references. Repeat the stable anchors with the same wording and change only the variables needed for the new frame. Do not rely on a character name alone to preserve identity.

## Build a 50-image plan

Design the set before generating it. A useful 50-shot structure is five coherent environments by two light states by five actions. Use environment-specific combinations rather than a blind Cartesian product.

Example environments: home, cafe or restaurant, rooftop or riverside, street or transit, and shop or work interior. For each, define:

- one neutral light state and one expressive but plausible light state
- five distinct actions with visible hand or body behavior
- a mix of wide context, medium candid, and close portrait frames
- one signature styling anchor that keeps the character recognizable

Generate in groups of five to ten. Review each group before continuing so repeated defects do not spread through the full set.

## Inspection gate

Reject or repair an image if it has a high-impact defect in any of these areas:

- identity drift, unintended age shift, or changing facial geometry
- mismatched gaze, iris artifacts, fused teeth, or expression that does not fit the action
- hair as a solid shape or motion with no physical cause
- extra, fused, or poorly contacting fingers; utensils, cups, food, or products floating or intersecting
- impossible mirror geometry, reflections, liquids, steam, shadows, or light direction
- plastic skin, excessive smoothing, HDR halos, clipping, or uniform sharpness across all depths
- accidental readable text, broken labels, invented logos, or watermark-like marks
- background architecture or furniture that bends or repeats unnaturally
- failure to match the requested aspect ratio, framing, wardrobe, product, or scene

## Selection score

Score viable images out of 10:

| Criterion | Points |
|---|---:|
| Photographic realism: light, texture, depth, optics | 0-3 |
| Identity or product consistency | 0-3 |
| Anatomy and object interaction | 0-2 |
| Composition and emotional moment | 0-1 |
| Fidelity to the brief | 0-1 |

Keep images scoring 8 or higher, provided none fail the inspection gate. Select a final set for both quality and range; avoid near-duplicates even when each image is individually strong.

Record batch status as planned, generated, reviewed, repaired, selected, and delivered. A prompt list or started generation is not a completed image set.
