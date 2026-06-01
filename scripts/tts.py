import os
import sys
import subprocess
import argparse

# 配置路径
SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(SKILL_DIR, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)


def list_voices():
    """列出所有可用的 edge-tts 语音"""
    cmd = ["edge-tts", "--list-voices"]
    subprocess.run(cmd, check=True)


def generate_tts(text, voice, output_path, rate="+0%", pitch="+0Hz"):
    """生成 TTS 语音文件"""
    cmd = [
        "edge-tts",
        "--voice", voice,
        "--text", text,
        "--write-media", output_path,
        "--rate", rate,
        "--pitch", pitch,
    ]
    print(f"正在生成语音... 音色: {voice}, 语速: {rate}, 音调: {pitch}")
    subprocess.run(cmd, check=True)
    print(f"语音已保存: {output_path}")
    return output_path


def main():
    parser = argparse.ArgumentParser(description="文字转语音工具 (Text-to-Speech)")
    parser.add_argument("--text", help="要朗读的文字")
    parser.add_argument("--voice", default="zh-CN-XiaoyiNeural", help="音色名称 (默认: zh-CN-XiaoyiNeural)")
    parser.add_argument("--output", default=None, help="输出文件名 (默认: 自动生成)")
    parser.add_argument("--rate", default="+0%", help="语速 (如 +30%%, -10%%)")
    parser.add_argument("--pitch", default="+0Hz", help="音调 (如 +10Hz, -5Hz)")
    parser.add_argument("--list-voices", action="store_true", help="列出所有可用语音")

    args = parser.parse_args()

    # 列出语音模式
    if args.list_voices:
        list_voices()
        return

    # 检查文本
    if not args.text:
        # 尝试从 stdin 读取
        if not sys.stdin.isatty():
            args.text = sys.stdin.read().strip()
        if not args.text:
            parser.error("请提供 --text 参数或通过管道传入文字")

    # 确定输出文件名
    if args.output:
        output_name = args.output
    else:
        # 取文本前 20 个字符作为文件名
        sanitized = "".join(c for c in args.text[:20] if c.isalnum() or c in " _-").strip()
        sanitized = sanitized if sanitized else "speech"
        output_name = f"{sanitized}.mp3"

    # 确保输出路径在 output 目录下
    output_path = os.path.join(OUTPUT_DIR, output_name)

    # 生成语音
    generate_tts(args.text, args.voice, output_path, args.rate, args.pitch)

    # 输出结果路径（供 skill 捕获）
    print(f"RESULT:{output_path}")


if __name__ == "__main__":
    main()
