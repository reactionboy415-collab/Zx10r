import cloudscraper
import json
import random
import string
import time
import threading
import os
from flask import Flask

# --- RENDER PORT EXPOSURE (Flask) ---
app = Flask(__name__)

@app.route('/')
def health():
    return "Ghost Injector is Running 24/7!", 200

def run_port():
    # Render default port 10000 bind kar raha hai
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# --- INJECTOR LOGIC ---
def generate_random_params(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_fake_ip():
    return ".".join(map(str, (random.randint(0, 255) for _ in range(4))))

def ghost_view_injector():
    target_link = "https://t.me/CatalystMystery/357"
    order_count = 0
    url = "https://monadze.com/fgm/api.php"
    
    # Create scraper with Cloudflare bypass
    scraper = cloudscraper.create_scraper()
    
    print(f"🔱 --- TG GHOST INJECTOR v6.0 (RENDER 24/7) --- 🔱")
    print(f"📡 Target: {target_link}")

    while True:
        try:
            order_count += 1
            fake_ip = generate_fake_ip()
            masked_link = f"{target_link}?auth={generate_random_params()}&sid={generate_random_params()}"
            
            headers = {
                "Accept": "application/json, text/plain, */*",
                "Content-Type": "application/json",
                "Origin": "https://smm8.com",
                "Referer": "https://smm8.com/",
                "X-Forwarded-For": fake_ip,
                "X-Real-IP": fake_ip,
                "User-Agent": f"Mozilla/5.0 (Linux; Android {random.randint(10, 14)}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{random.randint(1000, 9999)}.0 Mobile Safari/537.36",
                "X-Requested-With": "XMLHttpRequest"
            }

            payload = {
                "link": masked_link,
                "service": "30889", 
                "quantity": "200"
            }

            print(f"🚀 [Order #{order_count}] Fake IP: {fake_ip} | Injecting...")
            response = scraper.post(url, headers=headers, json=payload, timeout=30)
            
            if response.status_code == 200:
                res_data = response.json()
                if "order" in res_data:
                    print(f"✅ SUCCESS! Order ID: {res_data['order']}")
                else:
                    error_msg = res_data.get('error', 'Unknown Rejected')
                    print(f"⚠️ Server Response: {error_msg}")
                    if "active order" in error_msg.lower():
                        print("💀 Cooldown: Waiting 60s...")
                        time.sleep(60)
            else:
                print(f"❌ HTTP Error: {response.status_code}")

            # Anti-Ban Delay (Human Behavior)
            wait_time = random.randint(25, 50)
            print(f"⏳ Sleeping {wait_time}s...")
            time.sleep(wait_time)

        except Exception as e:
            print(f"⚠️ Loop Error: {e}")
            time.sleep(20)

if __name__ == "__main__":
    # Port 10000 bind karne ke liye Flask thread start karo
    threading.Thread(target=run_port, daemon=True).start()
    # Main Injector chalao
    ghost_view_injector()
