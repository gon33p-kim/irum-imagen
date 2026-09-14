---
name: super-real-images
description: Generate or edit photorealistic people and lifestyle photos with believable lighting, camera behavior, skin texture, and candid motion. Use for 슈퍼리얼, AI 인플루언서, 실사 인물, lifestyle or editorial photos, and requests to remove an artificial AI look; do not route illustration, anime, or 3D requests here unless the user wants them converted into photography.
---

# Super Real Images

Create the requested image, not merely a prompt, when an image-generation or editing tool is available. Return a prompt only when the user explicitly asks for one or generation is unavailable.

## Preserve the brief

- Keep supplied identity, product, wardrobe, location, composition, aspect ratio, text, and visual references unless the user asks to change them.
- For edits, include every target image in the editing call and describe only the intended changes. Inspect a local target image before editing it.
- If an exact person or product must be preserved but its reference is missing, ask for that reference. Resolve ordinary omissions with sensible photographic defaults.
- Treat required text, logos, labels, and signage as intentional content. Exclude them only when they are not part of the brief.

## Build photographic reality

Use four linked controls. Each detail must agree with the scene.

1. **Lighting first:** choose a real time or practical light source, its direction, a believable bounce surface, and smooth highlight roll-off. Mixed light should name both sources, such as cool window light with a warm lamp.
2. **Camera reality:** choose one plausible focal length, aperture, framing, camera height, and capture feel. Use handheld, candid, documentary, or smartphone language when it supports the shot. Do not combine contradictory lens or exposure claims.
3. **Material and skin texture:** keep pores, fine facial hair, slight tonal variation, natural sheen, fabric weave, wrinkles, condensation, steam, and surface reflections where visible. Use only a few scene-relevant imperfections.
4. **Life motion:** capture a small action or reaction rather than a static pose. Use flyaway hairs, shifting fabric, a mid-bite pause, a hand adjusting an object, a half-smile, or environmental motion that has a visible cause.

Read [references/prompt-blueprint.md](references/prompt-blueprint.md) when composing a production prompt or diagnosing an artificial result.

## Generate and inspect

1. Form a compact shot specification: subject, styling, place, moment, light, action, camera, finish, output size, and exclusions.
2. Send the production prompt and the required references to the available image-generation or editing tool. Do not claim completion before an image exists.
3. Inspect the result at useful resolution. Check face and identity, eyes and teeth, hair, hands, object contact, reflections, readable text, lighting direction, background geometry, and requested framing.
4. Correct the highest-impact defect with a focused edit or regeneration. Preserve successful parts of the image and avoid rewriting the entire scene unless composition failed.
5. Deliver the image and briefly state the chosen photographic direction. Distinguish generated, reviewed, selected, and merely proposed outputs.

Use [references/shot-library.md](references/shot-library.md) when the user wants ideas, multiple scene types, a tasteful sensual mood, or lifestyle variations. Use [references/batch-and-qc.md](references/batch-and-qc.md) for recurring characters, large batches, or selecting the best images.

## Avoid the synthetic look

Remove these failure patterns when they appear: plastic skin, perfect bilateral symmetry, doll-like eyes, hair rendered as one solid mass, uniform studio lighting in an everyday scene, clipped highlights, excessive HDR, sharpening halos, impossible reflections, rigid posing, malformed hands or object contact, and accidental lettering.

Prefer positive photographic descriptions. Add a short constraint line only for likely failures, for example: natural shadow gradients, smooth highlight roll-off, restrained grain, no beauty-filter skin, no HDR, no sharpening halos, and no accidental readable text or logos.

Do not treat maximum detail, extreme sharpness, or a film-stock name by itself as realism. A convincing image needs coherent light, optics, material response, and human behavior.
