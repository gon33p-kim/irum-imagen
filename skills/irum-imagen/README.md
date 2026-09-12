# irum-imagen Agent Skill

Codex·Claude Code·Cursor 같은 Agent Skill 호환 도구에서 `irum-imagen`을
명시적으로 호출하기 위한 배포 폴더입니다.

## 설치

먼저 CLI를 설치합니다.

```bash
npm install -g https://github.com/IrumHahn/irum-imagen/archive/refs/heads/main.tar.gz
```

그다음 스킬을 설치합니다.

```bash
npx skills add IrumHahn/irum-imagen --skill irum-imagen
```

수동 설치 경로:

| 도구 | 경로 |
| --- | --- |
| Codex | `~/.codex/skills/irum-imagen/` |
| Claude Code | `~/.claude/skills/irum-imagen/` |
| OpenCode | `~/.config/opencode/skills/irum-imagen/` |
| Cursor·Continue·Gemini CLI | `.agents/skills/irum-imagen/` |

## 호출 예시

```text
$irum-imagen을 사용해서 흰 배경의 화장품 제품 사진을 만들어줘.
```

이 스킬은 일반 이미지 요청에 자동 실행되지 않도록 설정되어 있으므로
`$irum-imagen`을 명시해서 호출하세요.

## 직접 검증

```bash
irum-imagen \
  --prompt "파란색 정사각형 아이콘" \
  --image-model gpt-image-2.5-flare \
  --dry-run
```

실제 생성, 이미지 편집, 모델 선택, 보안 주의사항은 저장소 루트
`README.md`를 참고하세요.
