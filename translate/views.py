from django.shortcuts import render
import requests
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent


# Create your views here.


def translate(request):
    if request.method == "POST":
        text = request.POST["input_area"]
        with open(os.path.join(BASE_DIR, "API_KEY.txt")) as f:
            API_KEY = f.read()
        params = {
            "auth_key": API_KEY,
            "text": text,
            "target_lang": 'JA'  # 出力テキストの言語を英語に設定
        }
        deepl_request = requests.post(
            "https://api-free.deepl.com/v2/translate", data=params)
        result = deepl_request.json()
        translated_text = result["translations"][0]["text"]
        print(translated_text)
        return render(request, 'translate/translate_main.html',
                      {"output_text": translated_text, "input_text": text})

    else:
        pass

    return render(request, 'translate/translate_main.html', {})
