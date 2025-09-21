#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import pyautogui
from PIL import Image
import base64
import io
import time

def test_screenshot():
    print("📸 Testez screenshot-ul...")
    
    # 1. Testez endpoint-ul /api/status
    print("1️⃣ Testez endpoint-ul /api/status...")
    try:
        response = requests.get("http://localhost:5000/api/status", timeout=10)
        print(f"✅ Status: {response.status_code}")
        print(f"📄 Răspuns: {response.json()}")
    except Exception as e:
        print(f"❌ Eroare la /api/status: {e}")
        return
    
    # 2. Fac screenshot
    print("2️⃣ Încerc să fac screenshot...")
    try:
        pyautogui.FAILSAFE = False
        screenshot = pyautogui.screenshot()
        screenshot = screenshot.resize((1280, 720), Image.Resampling.LANCZOS)
        img_buffer = io.BytesIO()
        screenshot.save(img_buffer, format='PNG', optimize=True, quality=85)
        img_buffer.seek(0)
        img_base64 = base64.b64encode(img_buffer.getvalue()).decode('utf-8')
        print(f"✅ Screenshot capturat, mărime: {len(img_base64)} caractere")
    except Exception as e:
        print(f"❌ Eroare la capturarea screenshot-ului: {e}")
        return
    
    # 3. Trimite screenshot-ul la server
    print("3️⃣ Trimite screenshot-ul la server...")
    try:
        response = requests.post(
            "http://localhost:5000/api/agent/screenshot",
            json={'screenshot': img_base64},
            timeout=30
        )
        print(f"✅ Screenshot trimis: {response.status_code}")
        print(f"📄 Răspuns: {response.json()}")
    except Exception as e:
        print(f"❌ Eroare la trimiterea screenshot: {e}")
        return
    
    # 4. Testez din nou /api/status
    print("4️⃣ Testez din nou /api/status...")
    try:
        time.sleep(2)
        response = requests.get("http://localhost:5000/api/status", timeout=10)
        print(f"✅ Status: {response.status_code}")
        data = response.json()
        print(f"📄 Latest screenshot: {data.get('latest_screenshot')}")
        if data.get('latest_screenshot'):
            print(f"🔗 URL screenshot: http://localhost:5000/api/screenshot/{data['latest_screenshot']}")
    except Exception as e:
        print(f"❌ Eroare la /api/status: {e}")

if __name__ == "__main__":
    test_screenshot()
