# irum-imagen

Codex에 로그인된 ChatGPT 계정을 이용해 GPT Image 2.5 이미지를 생성하고
편집하는 CLI, Node.js/Python SDK, Agent Skill 패키지입니다.

> [!WARNING]
> 이 프로젝트는 OpenAI의 공식 공개 API가 아닌 Codex의 비공개 백엔드 경로를
> 사용합니다. 예고 없이 동작이 바뀌거나 중단될 수 있으며, OpenAI 공식 제품이
> 아닙니다.

## 제공 기능

- GPT Image 2.5 Flare를 기본 이미지 모델로 사용
- GPT Image 2.5 Sunburst 선택 가능
- 텍스트 이미지 생성과 기존 이미지 편집
- 정사각형·가로형·세로형 출력 크기 요청
- 실제 호출 없이 인증과 요청 구조를 확인하는 드라이런
- Codex, Claude Code, Cursor 등에서 사용할 수 있는 Agent Skill
- 디버그 출력의 토큰·계정 ID·이미지 데이터 자동 마스킹

## 학생용 빠른 설치

### 1. 준비사항

- Node.js 20 이상
- Codex CLI 또는 Codex 데스크톱 앱에서 ChatGPT 로그인 완료
- 해당 ChatGPT 계정에서 이미지 생성 기능 사용 가능

로그인 상태를 확인합니다.

```bash
codex login status
```

### 2. CLI 설치

현재 GitHub 저장소에서 직접 설치합니다.

```bash
npm install -g https://github.com/IrumHahn/irum-imagen/archive/refs/heads/main.tar.gz
```

설치를 확인합니다.

```bash
irum-imagen --version
irum-imagen --help
```

짧은 별칭 `iim`도 사용할 수 있습니다.

### 3. 안전한 드라이런

이미지를 생성하거나 사용량을 소모하지 않고 인증과 모델 지정만 확인합니다.

```bash
irum-imagen \
  --prompt "파란색 정사각형 아이콘" \
  --image-model gpt-image-2.5-flare \
  --dry-run
```

출력의 `tools[0].model`이 `gpt-image-2.5-flare`인지 확인하세요.

### 4. 첫 이미지 생성

```bash
irum-imagen \
  --prompt "흰 배경 위에 놓인 파란색 머그컵, 자연스러운 제품 사진, 글자 없음" \
  --output ./blue-mug.png
```

성공하면 JSON의 `savedPath`에 저장된 PNG 경로가 표시됩니다.

## GPT Image 2.5 모델 선택

Flare가 기본값이므로 일반 생성에서는 모델 옵션을 생략할 수 있습니다.

```bash
# 빠른 일반 생성: gpt-image-2.5-flare
irum-imagen --prompt "따뜻한 수채화풍 서울 골목" --output ./seoul.png

# 정밀 편집·최고 품질: gpt-image-2.5-sunburst
irum-imagen \
  --prompt "제품의 형태와 로고는 유지하고 배경만 밝은 스튜디오로 변경" \
  --image ./product.png \
  --image-model gpt-image-2.5-sunburst \
  --output ./product-edited.png
```

`--model`은 이미지 모델이 아니라 요청을 지휘하는 메인 모델을 지정합니다.
이미지 모델은 반드시 `--image-model`로 선택하세요.

## 이미지 편집과 여러 참고 이미지

```bash
# 한 장 편집
irum-imagen \
  --prompt "고양이에게 빨간 모자를 씌워줘" \
  --image ./cat.png \
  --output ./cat-hat.png

# 여러 장을 참고해 새 이미지 생성
irum-imagen \
  --prompt "첫 이미지의 구도와 두 번째 이미지의 색감을 결합해줘" \
  --image ./composition.png \
  --image ./colors.png \
  --output ./combined.png
```

입력 형식은 PNG, JPG/JPEG, GIF, WebP를 지원합니다.

## 출력 크기

```bash
irum-imagen \
  --prompt "노을이 지는 산 풍경" \
  --size 1536x1024 \
  --output ./sunset.png
```

요청 가능한 값:

- `auto`
- `1024x1024`, `2048x2048`
- `1536x1024`, `2048x1152`, `3840x2160`
- `1024x1536`, `2160x3840`

비공개 백엔드 특성상 실제 반환 크기는 요청값과 다를 수 있습니다.

## Agent Skill 설치

CLI를 먼저 설치한 뒤 Agent Skill을 설치합니다.

```bash
npx skills add IrumHahn/irum-imagen --skill irum-imagen
```

Codex에서 다음처럼 명시적으로 호출할 수 있습니다.

```text
$irum-imagen을 사용해서 흰 배경의 화장품 제품 사진을 만들어줘.
```

수동 설치 경로는 다음과 같습니다.

| 도구 | 설치 경로 |
| --- | --- |
| Codex | `~/.codex/skills/irum-imagen/` |
| Claude Code | `~/.claude/skills/irum-imagen/` |
| OpenCode | `~/.config/opencode/skills/irum-imagen/` |
| Cursor·Continue·Gemini CLI | 프로젝트의 `.agents/skills/irum-imagen/` |

배포용 스킬 원본은 [`skills/irum-imagen`](skills/irum-imagen)에 있습니다.

## Node.js SDK

```bash
npm install https://github.com/IrumHahn/irum-imagen/archive/refs/heads/main.tar.gz
```

```javascript
import { createProvider, resolveConfig } from "irum-imagen";

const config = resolveConfig({ provider: "private-codex" });
const provider = createProvider(config);

const result = await provider.generateImage({
  prompt: "미니멀한 파란색 아이콘",
  model: "gpt-5.4",
  imageModel: "gpt-image-2.5-flare",
  outputPath: "./icon.png",
});

console.log(result.savedPath);
```

## Python SDK

```bash
pip install "git+https://github.com/IrumHahn/irum-imagen.git#subdirectory=python"
```

```python
from irum_imagen import Client

client = Client(provider="private-codex")
result = client.generate_image(
    prompt="미니멀한 파란색 아이콘",
    image_model="gpt-image-2.5-flare",
    output_path="./icon.png",
)
print(result.saved_path)
```

## 환경 변수

필요한 경우에만 사용하세요.

| 변수 | 용도 |
| --- | --- |
| `IRUM_IMAGEN_IMAGE_MODEL` | 기본 이미지 모델 |
| `IRUM_IMAGEN_MODEL` | 메인 모델 |
| `IRUM_IMAGEN_PROVIDER` | `private-codex`, `codex-cli`, `auto` |
| `IRUM_IMAGEN_OUTPUT` | 기본 출력 경로 |
| `IRUM_IMAGEN_AUTH_FILE` | Codex 인증 파일 경로 |

이미지 모델을 확실히 지정하려면 `private-codex` 공급자를 사용하세요.
`codex-cli` 폴백은 특정 이미지 모델을 보장하지 못하므로 명시적 모델 지정 시
실패하도록 설계되어 있습니다.

## 문제 해결

### `irum-imagen: command not found`

Node.js 20 이상인지 확인하고 CLI를 다시 설치한 뒤 새 터미널을 여세요.

```bash
node --version
npm install -g https://github.com/IrumHahn/irum-imagen/archive/refs/heads/main.tar.gz
```

### 인증 파일 또는 401 오류

Codex에서 다시 로그인한 뒤 드라이런을 실행하세요.

```bash
codex login
irum-imagen --prompt "인증 확인" --dry-run
```

### 이미지를 받지 못함

계정의 이미지 생성 권한과 사용 한도를 확인하세요. 비공개 백엔드가 변경된
경우에는 이 저장소의 Issues에서 최신 상태를 확인하세요.

## 보안 주의사항

- `~/.codex/auth.json`을 복사하거나 다른 사람에게 보내지 마세요.
- 인증 토큰, 계정 ID, 개인 이미지가 포함된 디버그 파일을 공유하지 마세요.
- 학생 각자가 자신의 기기에서 자신의 ChatGPT 계정으로 로그인해야 합니다.
- 공개 또는 공동 컴퓨터에서는 사용 후 Codex 로그아웃 상태를 확인하세요.

## 개발 및 검증

```bash
npm install
npm test
npm run check
npm run build:types

python3 -m pip install -e "./python[dev]"
python3 -m pytest python/tests
```

## 출처와 라이선스

이 프로젝트는 Jeffrey (Dongkyu) Kim의
[`NomaDamas/god-tibo-imagen`](https://github.com/NomaDamas/god-tibo-imagen)을
기반으로 이름, 설치 경험, 학생용 가이드와 Agent Skill을 정리한 파생 프로젝트입니다.
원본과 이 프로젝트는 MIT 라이선스를 따릅니다. 자세한 내용은
[`NOTICE.md`](NOTICE.md)와 [`LICENSE`](LICENSE)를 확인하세요.
