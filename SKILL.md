---
name: text-to-speech
description: 将文字转为语音音频文件（MP3） - 基于 edge-tts 引擎，支持多语种多音色，输入文字交付音频文件。
metadata:
  qwenpaw:
    emoji: "🔊"
---

# 文字转语音 (Text-to-Speech)

## 什么时候用
- 用户要求"朗读这段文字"、"生成语音"、"配音"、"语音输出"时
- 需要将文字内容转为 MP3 音频文件时
- 用户提供长文本希望转为可听的语音时
- 需要为视频、课件、有声书准备配音素材时

## 核心逻辑
1. **接收文字**：通过 `--text` 参数或管道传入需要朗读的文字
2. **语音生成**：调用 `edge-tts` 引擎生成高质量 MP3 音频
3. **交付文件**：将生成的音频文件返回给用户

## 支持的语音

列出所有可用语音：
```bash
edge-tts --list-voices
```

常用中文语音：
| 语音名 | 性别 | 风格 |
|--------|------|------|
| zh-CN-XiaoxiaoNeural | 女声 | 亲切自然（推荐） |
| zh-CN-XiaoyiNeural | 女声 | 活泼热情 |
| zh-CN-YunjianNeural | 男声 | 成熟稳重 |
| zh-CN-YunxiNeural | 男声 | 阳光开朗 |
| zh-CN-YunyangNeural | 男声 | 新闻播报 |
| zh-CN-XiaochenNeural | 女声 | 轻松幽默 |

## 如何使用

### 基本用法
```bash
python scripts/tts.py --text "你好世界，欢迎使用文字转语音工具"
```

### 指定音色
```bash
python scripts/tts.py --text "今天天气真不错" --voice zh-CN-XiaoxiaoNeural
```

### 调节语速
```bash
python scripts/tts.py --text "这是一段较快的语速" --rate +30%
```

### 指定输出文件名
```bash
python scripts/tts.py --text "你好" --voice zh-CN-YunjianNeural --output myvoice.mp3
```

## 参数说明
| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--text` | 要朗读的文字（必填） | - |
| `--voice` | 音色名称 | zh-CN-XiaoyiNeural |
| `--output` | 输出文件名 | output.mp3 |
| `--rate` | 语速（如 +30%, -10%） | +0% |
| `--pitch` | 音调（如 +10Hz, -5Hz） | +0Hz |

## 交付物
- MP3 音频文件，可直接播放或用于其他制作。
