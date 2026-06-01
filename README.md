# 🔊 Text-to-Speech

将文字转为语音音频文件（MP3）的工具。基于 Microsoft Edge TTS 引擎，支持多语种多音色，无需 API 密钥，完全免费。

## ✨ 特点

- 🎯 **即装即用**：一行命令安装，无需注册任何 API
- 🎭 **多音色**：支持 400+ 种语音，包含中文（普通话/粤语/台湾国语/方言）
- ⚡ **快速生成**：基于 Edge TTS 引擎，响应迅速
- 📦 **轻量无依赖**：纯 Python 实现，仅依赖 `edge-tts`
- 🔧 **参数丰富**：支持语速、音调调节

## 📦 安装

```bash
pip install edge-tts
```

## 🚀 快速开始

```bash
# 基本用法（默认 zh-CN-XiaoyiNeural 女声）
python scripts/tts.py --text "你好世界，欢迎使用文字转语音工具"

# 指定音色
python scripts/tts.py --text "今天天气真不错" --voice zh-CN-XiaoxiaoNeural

# 调节语速（+30% 加快，-20% 减慢）
python scripts/tts.py --text "这是一段较快的语速" --rate +30%

# 指定输出文件
python scripts/tts.py --text "你好" --voice zh-CN-YunjianNeural --output myvoice.mp3
```

### 管道输入

```bash
echo "今天天气真不错" | python scripts/tts.py
cat article.txt | python scripts/tts.py --voice zh-CN-YunyangNeural
```

## 🎭 可用音色

### 中文音色总览

| 音色名 | 语言 | 性别 | 风格 |
|--------|------|:----:|------|
| `zh-CN-XiaoxiaoNeural` | 普通话 | 🚺 | 温暖亲切 |
| `zh-CN-XiaoyiNeural` | 普通话 | 🚺 | 活泼热情（默认） |
| `zh-CN-YunjianNeural` | 普通话 | 🚹 | 成熟稳重 |
| `zh-CN-YunxiNeural` | 普通话 | 🚹 | 阳光开朗 |
| `zh-CN-YunxiaNeural` | 普通话 | 🚹 | 可爱萌系 |
| `zh-CN-YunyangNeural` | 普通话 | 🚹 | 新闻播报 |
| `zh-CN-liaoning-XiaobeiNeural` | 东北话 | 🚺 | 幽默风趣 |
| `zh-CN-shaanxi-XiaoniNeural` | 陕西话 | 🚺 | 明亮爽朗 |
| `zh-HK-HiuGaaiNeural` | 粤语 | 🚺 | 亲切 |
| `zh-HK-HiuMaanNeural` | 粤语 | 🚺 | 友好 |
| `zh-HK-WanLungNeural` | 粤语 | 🚹 | 友好 |
| `zh-TW-HsiaoChenNeural` | 国语 | 🚺 | 友好 |
| `zh-TW-HsiaoYuNeural` | 国语 | 🚺 | 友好 |
| `zh-TW-YunJheNeural` | 国语 | 🚹 | 友好 |

查看所有 400+ 音色：

```bash
python scripts/tts.py --list-voices
```

## 📋 参数说明

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--text` | 要朗读的文字（必填，或通过管道传入） | - |
| `--voice` | 音色名称 | `zh-CN-XiaoyiNeural` |
| `--output` | 输出文件名 | 自动以文本命名 |
| `--rate` | 语速（如 `+30%`、`-10%`） | `+0%` |
| `--pitch` | 音调（如 `+10Hz`、`-5Hz`） | `+0Hz` |
| `--list-voices` | 列出所有可用音色 | - |

## 📁 输出

音频文件默认保存在 `output/` 目录下，格式为 MP3。

可用 `--output` 指定完整路径输出到任意位置。

## 🧩 作为 CherryStudio Skill 使用

本项目可注册为 [CherryStudio](https://cherrystudio.ai/) Skill，在对话中直接触发：

```bash
# text-to-speech skill 已注册后，在对话中自动响应
"朗读这段文字" → 自动调用 TTS 生成语音
"生成配音" → 自动调用 TTS 生成配音文件
```

## 📄 许可

MIT License © 2026
