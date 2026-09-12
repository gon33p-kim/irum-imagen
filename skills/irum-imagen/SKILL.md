---
name: irum-imagen
description: >-
  Generate or edit images with GPT Image 2.5 through the irum-imagen CLI and
  the user's local Codex ChatGPT authentication. Use when the user explicitly
  invokes irum-imagen or asks to use this package for an image task.
---

# irum-imagen

Use the `irum-imagen` CLI to generate images from text or edit supplied images.
The tool uses the user's own local Codex ChatGPT login and an unsupported private
backend.

## Preconditions

1. Confirm `irum-imagen` is on `PATH`. If missing, tell the user to run:

   ```bash
   npm install -g https://github.com/IrumHahn/irum-imagen/archive/refs/heads/main.tar.gz
   ```

2. Confirm Codex reports a ChatGPT login with `codex login status`. If the local
   login or `~/.codex/auth.json` is unavailable, stop and tell the user to log in.
   Never request, print, copy, or fabricate authentication tokens.

## Model selection

- The private provider defaults to `gpt-image-2.5-flare`. Use it for fast,
  high-quality everyday generation.
- Use `--image-model gpt-image-2.5-sunburst` when editing precision or maximum
  capability matters.
- `--model` controls the main orchestration model; it does not select the image
  model.
- When an exact image model matters, use `--provider private-codex`. The
  `codex-cli` fallback cannot guarantee an image model.

## Generate

Always provide an explicit output path so the result is easy to find.

```bash
irum-imagen \
  --prompt "flat blue square icon, white background, no text" \
  --output ./out.png
```

## Edit with reference images

Pass each supplied PNG, JPG/JPEG, GIF, or WebP with a separate `--image` flag.
Preserve the user's requested subject, layout, text, and visual medium.

```bash
irum-imagen \
  --prompt "Keep the product unchanged and replace only the background" \
  --image ./product.png \
  --image-model gpt-image-2.5-sunburst \
  --output ./product-edited.png
```

## Output size

Use `--size` only when the user requests a format. Supported values are `auto`,
`1024x1024`, `2048x2048`, `1536x1024`, `2048x1152`, `3840x2160`,
`1024x1536`, and `2160x3840`. The private backend may return dimensions that
differ from the request.

## Verification

Use a dry run when diagnosing authentication or confirming exact model routing:

```bash
irum-imagen \
  --prompt "request check" \
  --image-model gpt-image-2.5-flare \
  --dry-run
```

Verify that `request.body.tools[0].model` contains the requested image model.
After a live run, confirm the saved file is a valid image and report the JSON
`savedPath` to the user. Show the resulting image when the client supports it.
