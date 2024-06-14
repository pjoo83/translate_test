from googletrans import Translator


def translate_text(text, src_lang='auto', dest_lang='zh-cn'):
    translator = Translator()  # 不需要指定service_urls，除非有特殊需求
    try:
        result = translator.translate(text, dest=dest_lang)
        return result.text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    # 示例：将中文翻译成英文

if __name__ == '__main__':
    chinese_text = "اس {number} ممبروں کو پیغامات بھیجیں"
    translated_text = translate_text(chinese_text)
    print(translated_text)