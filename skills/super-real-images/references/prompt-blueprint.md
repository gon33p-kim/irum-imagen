# Production prompt blueprint

Use only the blocks that affect the requested image. Keep the prompt specific and coherent rather than long for its own sake.

## Shot specification

1. **Subject:** adult age when relevant, visible physical traits, expression, identity anchors, and the subject's relationship to the camera.
2. **Styling:** garment silhouette, material, color, fit, natural wrinkles, makeup level, hair state, and accessories.
3. **Place:** a concrete location with two to four physical details that explain the light or action.
4. **Moment:** one observable action and one small reaction. Describe the frame as a captured instant.
5. **Light:** time, source, direction, bounce surface, shadow behavior, highlight roll-off, and any plausible mixed color temperatures.
6. **Camera:** framing, camera height or angle, focal length, aperture, depth of field, and capture feel.
7. **Finish:** realistic texture plus restrained film or sensor behavior. Name a film stock only when its visible qualities are also stated.
8. **Constraints:** accidental text, logos, artifacts, or unwanted retouching. Do not exclude content the user requested.

## Practical choices

| Need | Useful choice | Visible effect |
|---|---|---|
| Environment and movement | 28-35mm, f/2-f/4 | More spatial context and believable depth |
| Everyday candid portrait | 50mm, f/1.8-f/2.8 | Natural perspective with moderate separation |
| Intimate portrait | 85mm, f/1.8-f/2.8 | Compressed background and focused expression |
| Soft daylight skin | Portra 160/400 or Pro 400H-inspired | Gentle contrast, restrained color, smooth highlights |
| Warm lively daylight | Gold 200 or Superia 400-inspired | Warm highlights or modest saturation with visible grain |
| Low light and mixed sources | Vision3 500T or Cinestill 800T-inspired | Tungsten response, visible grain, mild highlight halation |

Do not combine several focal lengths, film stocks, or competing time-of-day cues in one frame.

## English production skeleton

```text
[Adult subject and stable identity anchors], [wardrobe/material and grooming], in [specific place with a few physical details]. Captured while [small action] with [micro-expression or natural reaction], [relationship to camera].

Lighting: [real time or practical source], [direction], [named bounce surface], realistic shadow gradients, smooth highlight roll-off, [mixed source only if plausible].

Camera: [framing and camera height], [one focal length], [one aperture], [handheld/candid/documentary/smartphone feel], [scene-appropriate depth of field or motion blur].

Texture and finish: [skin/material/environment details], [one film or sensor behavior with its visible qualities], natural contrast and color.

Constraints: preserve [required identity/product/composition anchors]; avoid [two to five likely artifacts].
```

## Example

```text
An adult Korean woman with a short black bob and wispy bangs, light natural makeup, wearing a soft gray knit cardigan, in a small apartment kitchen with a pale stone counter and an open window. Captured just after the lid of her iced coffee shifts and a few droplets splash; she pulls one shoulder back and laughs in surprise, looking toward the cup rather than posing for the camera.

Lighting: late-afternoon window light from camera left, soft bounce from the pale counter under her eyes, warm room light faintly mixing in the background, natural shadow gradients, smooth highlight roll-off on skin and droplets.

Camera: waist-up candid frame from counter height, 50mm, f/2.2, handheld snapshot feel, slight background motion blur while the eyes remain naturally sharp.

Texture and finish: visible pores and fine facial hair, natural skin sheen, knit weave, condensation on the cup, restrained Portra 400-inspired grain and gentle warm highlights.

Constraints: keep the same face and haircut; no beauty-filter skin, no HDR, no sharpening halos, no accidental readable labels or logos.
```

## Repair prompts

Use a focused repair instruction when the composition already works:

- **Plastic skin:** restore visible pores, fine facial hair, subtle tonal variation, and natural specular highlights while preserving identity and makeup.
- **Flat light:** preserve the scene; establish the named key-light direction, bounce fill from the specified surface, and smooth highlight roll-off.
- **Rigid pose:** preserve wardrobe and composition; shift the subject into the described mid-action moment with relaxed shoulders and a natural micro-expression.
- **Hair mass:** preserve hairstyle; separate a few fine strands and flyaways according to the scene's airflow without making the hair messy overall.
- **Overprocessed result:** reduce HDR contrast, edge sharpening, saturation, and artificial clarity; retain natural texture and scene-appropriate grain.
