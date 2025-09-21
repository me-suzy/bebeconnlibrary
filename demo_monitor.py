#!/usr/bin/env python3
"""
Demo BebeConn - Monitorizare Laptop de la Distanță
Demonstrează utilizarea librăriei BebeConn pentru monitorizarea laptopului
"""

import time
import sys
import threading
from datetime import datetime

def demo_basic_usage():
    """Demo utilizare de bază a librăriei."""
    print("=" * 60)
    print("🖥️  BEBECONN - DEMO MONITORIZARE LAPTOP DE LA DISTANȚĂ")
    print("=" * 60)
    print()
    
    try:
        # Import librăria
        import bebe_conn
        print("✅ Librăria BebeConn importată cu succes!")
        print()
        
        # Demonstrează inițializarea claselor
        print("🔧 Inițializare componente...")
        
        # BebeConn principal
        bebe = bebe_conn.BebeConn(
            ngrok=False,           # Local (fără ngrok)
            port=5000,             # Portul serverului
            screenshot_interval=60 # Screenshot la fiecare 60 secunde
        )
        print("   ✅ BebeConn inițializat")
        
        # Server separat
        server = bebe_conn.BebeServer(port=5001)
        print("   ✅ BebeServer inițializat pe portul 5001")
        
        # Agent separat
        agent = bebe_conn.BebeAgent(
            server_url="http://localhost:5001",
            screenshot_interval=30
        )
        print("   ✅ BebeAgent inițializat")
        
        return bebe, server, agent
        
    except ImportError as e:
        print(f"❌ Eroare la importarea librăriei: {e}")
        print("   Instalează librăria: pip install -e .")
        return None, None, None
    except Exception as e:
        print(f"❌ Eroare la inițializare: {e}")
        return None, None, None

def demo_system_info(agent):
    """Demo obținerea informațiilor despre sistem."""
    print("\n" + "=" * 60)
    print("📊 DEMO - INFORMATII DESPRE SISTEM")
    print("=" * 60)
    
    try:
        # Obține informații despre sistem
        system_info = agent.get_system_info()
        
        if system_info:
            # Informații de bază
            basic = system_info.get('basic_info', {})
            print(f"🖥️  Platforma: {basic.get('platform', 'Unknown')}")
            print(f"💻 Procesor: {basic.get('processor', 'Unknown')}")
            print(f"🧠 RAM: {basic.get('total_memory', 'Unknown')} GB")
            print(f"💾 Disk: {basic.get('disk_usage', 'Unknown')}%")
            
            # Statistici sistem
            stats = system_info.get('system_stats', {})
            print(f"⚡ CPU Usage: {stats.get('cpu_percent', 0):.1f}%")
            print(f"🧠 RAM Usage: {stats.get('memory_percent', 0):.1f}%")
            print(f"💾 Disk Usage: {stats.get('disk_percent', 0):.1f}%")
            
            # Procese active
            processes = system_info.get('running_processes', [])
            print(f"🔧 Procese active: {len(processes)}")
            
            # Top 5 procese
            if processes:
                print("\n📋 Top 5 procese (după CPU):")
                for i, proc in enumerate(processes[:5], 1):
                    name = proc.get('name', 'Unknown')
                    cpu = proc.get('cpu_percent', 0)
                    memory = proc.get('memory_percent', 0)
                    print(f"   {i}. {name} - CPU: {cpu:.1f}%, RAM: {memory:.1f}%")
            
            print("\n✅ Informații despre sistem obținute cu succes!")
            
        else:
            print("⚠️  Nu s-au putut obține informații despre sistem")
            
    except Exception as e:
        print(f"❌ Eroare la obținerea informațiilor: {e}")

def demo_screenshot(agent):
    """Demo capturarea screenshot-ului."""
    print("\n" + "=" * 60)
    print("📸 DEMO - CAPTURARE SCREENSHOT")
    print("=" * 60)
    
    try:
        print("📸 Captură screenshot...")
        screenshot_data = agent.take_screenshot()
        
        if screenshot_data:
            print(f"✅ Screenshot capturat cu succes!")
            print(f"   Mărime: {len(screenshot_data)} caractere (base64)")
            print(f"   Dimensiune aproximativă: {len(screenshot_data) * 3 // 4} bytes")
        else:
            print("❌ Nu s-a putut captura screenshot-ul")
            
    except Exception as e:
        print(f"❌ Eroare la capturarea screenshot-ului: {e}")

def demo_heartbeat(agent):
    """Demo trimiterea heartbeat-ului."""
    print("\n" + "=" * 60)
    print("💓 DEMO - HEARTBEAT")
    print("=" * 60)
    
    try:
        print("💓 Trimit heartbeat...")
        success = agent.send_heartbeat()
        
        if success:
            print("✅ Heartbeat trimis cu succes!")
            print(f"   Timestamp: {datetime.now().strftime('%H:%M:%S')}")
        else:
            print("❌ Heartbeat eșuat")
            
    except Exception as e:
        print(f"❌ Eroare la trimiterea heartbeat-ului: {e}")

def demo_monitoring_loop(agent, duration=30):
    """Demo bucla de monitorizare."""
    print("\n" + "=" * 60)
    print(f"🔄 DEMO - MONITORIZARE CONTINUĂ ({duration}s)")
    print("=" * 60)
    
    start_time = time.time()
    heartbeat_count = 0
    screenshot_count = 0
    
    try:
        while time.time() - start_time < duration:
            # Heartbeat
            if agent.send_heartbeat():
                heartbeat_count += 1
                print(f"💓 Heartbeat #{heartbeat_count} - {datetime.now().strftime('%H:%M:%S')}")
            
            # Screenshot (la fiecare 10 secunde în demo)
            if int(time.time() - start_time) % 10 == 0 and int(time.time() - start_time) > 0:
                screenshot_data = agent.take_screenshot()
                if screenshot_data:
                    screenshot_count += 1
                    print(f"📸 Screenshot #{screenshot_count} - {datetime.now().strftime('%H:%M:%S')}")
            
            time.sleep(2)  # Verifică la fiecare 2 secunde
            
        print(f"\n✅ Monitorizare completă!")
        print(f"   💓 Heartbeat-uri trimise: {heartbeat_count}")
        print(f"   📸 Screenshot-uri capturate: {screenshot_count}")
        
    except KeyboardInterrupt:
        print("\n⏹️  Monitorizare oprită de utilizator")
    except Exception as e:
        print(f"\n❌ Eroare în bucla de monitorizare: {e}")

def demo_web_dashboard():
    """Demo pornirea dashboard-ului web."""
    print("\n" + "=" * 60)
    print("🌐 DEMO - DASHBOARD WEB")
    print("=" * 60)
    
    print("🌐 Pornesc dashboard-ul web...")
    print("   📱 Accesează: http://localhost:5000")
    print("   🔗 Sau: http://192.168.1.131:5000")
    print("   ⏹️  Apasă Ctrl+C pentru a opri")
    print()
    
    try:
        # Pornește sistemul complet
        import bebe_conn
        bebe_conn.start(ngrok=False, port=5000, screenshot_interval=60)
        
    except KeyboardInterrupt:
        print("\n⏹️  Dashboard oprit de utilizator")
    except Exception as e:
        print(f"\n❌ Eroare la pornirea dashboard-ului: {e}")

def main():
    """Funcția principală."""
    print("🚀 BEBECONN - DEMO MONITORIZARE LAPTOP")
    print("   Librăria pentru monitorizarea laptopului de la distanță")
    print()
    
    # Demo inițializare
    bebe, server, agent = demo_basic_usage()
    
    if not agent:
        print("\n❌ Nu s-a putut inițializa librăria. Ieșire...")
        return
    
    # Demo informații sistem
    demo_system_info(agent)
    
    # Demo screenshot
    demo_screenshot(agent)
    
    # Demo heartbeat
    demo_heartbeat(agent)
    
    # Întrebă utilizatorul ce vrea să facă
    print("\n" + "=" * 60)
    print("🎯 ALEGE O OPȚIUNE:")
    print("=" * 60)
    print("1. 🔄 Monitorizare continuă (30 secunde)")
    print("2. 🌐 Pornește dashboard web")
    print("3. 📊 Afișează informații despre sistem")
    print("4. 📸 Captură screenshot")
    print("5. 💓 Trimite heartbeat")
    print("6. ❌ Ieșire")
    print()
    
    try:
        choice = input("Alege opțiunea (1-6): ").strip()
        
        if choice == "1":
            demo_monitoring_loop(agent, 30)
        elif choice == "2":
            demo_web_dashboard()
        elif choice == "3":
            demo_system_info(agent)
        elif choice == "4":
            demo_screenshot(agent)
        elif choice == "5":
            demo_heartbeat(agent)
        elif choice == "6":
            print("👋 La revedere!")
        else:
            print("❌ Opțiune invalidă")
            
    except KeyboardInterrupt:
        print("\n👋 La revedere!")
    except Exception as e:
        print(f"\n❌ Eroare: {e}")

if __name__ == "__main__":
    main()
