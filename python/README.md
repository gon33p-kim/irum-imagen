# irum-imagen Python SDK

Codex에 로그인된 ChatGPT 계정을 사용해 GPT Image 2.5 이미지를 생성하고
편집하는 Python SDK입니다. 비공개 Codex 백엔드에 의존하므로 예고 없이
동작이 변경될 수 있습니다.

## GitHub에서 설치

```bash
pip install "git+https://github.com/IrumHahn/irum-imagen.git#subdirectory=python"
```

## 사용법

```python
from irum_imagen import Client

client = Client(provider="private-codex")
result = client.generate_image(
    prompt="흰 배경의 파란색 머그컵 제품 사진",
    image_model="gpt-image-2.5-flare",
    output_path="./mug.png",
)
print(result.saved_path)
```

기본 이미지 모델은 `gpt-image-2.5-flare`입니다. 정밀 편집에는
`gpt-image-2.5-sunburst`를 지정하세요.

```python
result = client.generate_image(
    prompt="제품 형태는 유지하고 배경만 스튜디오로 변경",
    image_paths="./product.png",
    image_model="gpt-image-2.5-sunburst",
    output_path="./product-edited.png",
)
```

드라이런은 실제 생성 없이 요청 구조를 반환합니다.

```python
result = client.generate_image(prompt="인증 확인", dry_run=True)
print(result.request)
```

전체 설치·보안·문제 해결 가이드는 저장소 루트의 `README.md`를 참고하세요.
