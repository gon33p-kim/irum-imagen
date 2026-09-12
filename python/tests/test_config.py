from __future__ import annotations

from src.irum_imagen.config import DEFAULT_IMAGE_MODEL, PRIVATE_CODEX_PROVIDER, resolve_config


def test_resolve_config_uses_env_defaults(monkeypatch, tmp_path):
    monkeypatch.setenv("CODEX_HOME", str(tmp_path / "codex-home"))
    monkeypatch.setenv("IRUM_IMAGEN_BASE_URL", "https://example.com/base")
    monkeypatch.setenv("IRUM_IMAGEN_PROVIDER", "private-codex")
    monkeypatch.setenv("IRUM_IMAGEN_MODEL", "model-x")
    monkeypatch.setenv("IRUM_IMAGEN_ORIGINATOR", "origin-x")
    monkeypatch.setenv("IRUM_IMAGEN_OUTPUT", str(tmp_path / "out.png"))
    monkeypatch.setenv("IRUM_IMAGEN_IMAGE_MODEL", "gpt-image-2.5-sunburst")

    config = resolve_config()

    assert config["codexHome"].endswith("codex-home")
    assert config["baseUrl"] == "https://example.com/base"
    assert config["authFile"].endswith("auth.json")
    assert config["installationIdFile"].endswith("installation_id")
    assert config["generatedImagesDir"].endswith("generated_images")
    assert config["provider"] == PRIVATE_CODEX_PROVIDER
    assert config["defaultModel"] == "model-x"
    assert config["defaultImageModel"] == "gpt-image-2.5-sunburst"
    assert config["defaultOriginator"] == "origin-x"
    assert config["defaultOutputPath"] == str(tmp_path / "out.png")


def test_resolve_config_defaults_image_model_to_flare(monkeypatch):
    monkeypatch.delenv("IRUM_IMAGEN_IMAGE_MODEL", raising=False)
    config = resolve_config()
    assert config["defaultImageModel"] == DEFAULT_IMAGE_MODEL
    assert DEFAULT_IMAGE_MODEL == "gpt-image-2.5-flare"
