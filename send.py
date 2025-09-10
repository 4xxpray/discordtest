import requests
import os

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK"]

data = {
    "content": "#  🔴 STREAMING 

@everyone",
    "embeds": [
        {
            "title": "Ảnh ngày " + __import__("datetime").datetime.now().strftime("%d/%m/%Y"),
            "image": {
                "url": "https://cdn.discordapp.com/attachments/1124268225585233960/1415399453975904276/Khong_Co_Tieu_e865_20250911010634.png?ex=68c310f6&is=68c1bf76&hm=7612e5a0bf77efad633a887292dec673b94cf29df6c0b8bc70e0fc6b8bc70e0c678e0fc6bcd&"
            }
        }
    ]
}

response = requests.post(WEBHOOK_URL, json=data)

if response.status_code == 204:
    print("✅ Sent thành công")
else:
    print("❌ Lỗi gửi:", response.status_code, response.text)
