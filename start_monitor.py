#!/usr/bin/env python3
"""
Start Monitor - Pornire rapidă BebeConn
Script simplu pentru pornirea sistemului de monitorizare
"""

import sys
import time
from datetime import datetime

def show_banner():
    """Afișează banner-ul aplicației."""
    print("=" * 70)
    print("🖥️  BEBECONN - MONITORIZARE LAPTOP DE LA DISTANȚĂ")
    print("=" * 70)
    print("   Librăria Python pentru monitorizarea laptopului")
    print("   cu interfață web și actualizări în timp real")
    print("=" * 70)
    print()

def show_menu():
    """Afișează meniul principal."""
    print("🎯 ALEGE O OPȚIUNE:")
    print("-" * 40)
    print("1. 🚀 Pornire locală (localhost:5000)")
    print("2. 🌐 Pornire cu ngrok (acces extern)")
    print("3. 🔧 Pornire doar serverul")
    print("4. 🤖 Pornire doar agentul")
    print("5. 📊 Demo informații sistem")
    print("6. 📸 Demo screenshot")
    print("7. 🔄 Demo monitorizare continuă")
    print("8. ❌ Ieșire")
    print()

def start_local():
    """Pornește sistemul local."""
    print("🚀 Pornesc sistemul local...")
    print("   📱 Dashboard: http://localhost:5000")
    print("   🔗 Rețea: http://192.168.1.131:5000")
    print("   ⏹️  Apasă Ctrl+C pentru a opri")
    print()
    
    try:
        import bebe_conn
        bebe_conn.start(ngrok=False, port=5000, screenshot_interval=120)
    except KeyboardInterrupt:
        print("\n⏹️  Sistem oprit de utilizator")
    except Exception as e:
        print(f"\n❌ Eroare: {e}")

def start_ngrok():
    """Pornește sistemul cu ngrok."""
    print("🌐 Pornesc sistemul cu ngrok...")
    print("   📱 Vei primi URL-ul ngrok în terminal")
    print("   ⏹️  Apasă Ctrl+C pentru a opri")
    print()
    
    try:
        import bebe_conn
        bebe_conn.start(ngrok=True, port=5000, screenshot_interval=120)
    except KeyboardInterrupt:
        print("\n⏹️  Sistem oprit de utilizator")
    except Exception as e:
        print(f"\n❌ Eroare: {e}")

def start_server_only():
    """Pornește doar serverul."""
    print("🔧 Pornesc doar serverul...")
    print("   📱 Dashboard: http://localhost:5000")
    print("   ⏹️  Apasă Ctrl+C pentru a opri")
    print()
    
    try:
        import bebe_conn
        bebe_conn.start_server(port=5000)
    except KeyboardInterrupt:
        print("\n⏹️  Server oprit de utilizator")
    except Exception as e:
        print(f"\n❌ Eroare: {e}")

def start_agent_only():
    """Pornește doar agentul."""
    print("🤖 Pornesc doar agentul...")
    print("   🌐 Conectare la: http://localhost:5000")
    print("   ⏹️  Apasă Ctrl+C pentru a opri")
    print()
    
    try:
        import bebe_conn
        bebe_conn.start_agent(server_url="http://localhost:5000", screenshot_interval=120)
    except KeyboardInterrupt:
        print("\n⏹️  Agent oprit de utilizator")
    except Exception as e:
        print(f"\n❌ Eroare: {e}")

def demo_system_info():
    """Demo informații despre sistem."""
    print("📊 Demo informații despre sistem...")
    print()
    
    try:
        import bebe_conn
        
        agent = bebe_conn.BebeAgent()
        system_info = agent.get_system_info()
        
        if system_info:
            basic = system_info.get('basic_info', {})
            stats = system_info.get('system_stats', {})
            processes = system_info.get('running_processes', [])
            
            print("🖥️  INFORMATII SISTEM:")
            print(f"   Platforma: {basic.get('platform', 'Unknown')}")
            print(f"   Procesor: {basic.get('processor', 'Unknown')}")
            print(f"   RAM: {basic.get('total_memory', 'Unknown')} GB")
            print(f"   CPU Usage: {stats.get('cpu_percent', 0):.1f}%")
            print(f"   RAM Usage: {stats.get('memory_percent', 0):.1f}%")
            print(f"   Disk Usage: {stats.get('disk_percent', 0):.1f}%")
            print(f"   Procese active: {len(processes)}")
            
            if processes:
                print("\n🔧 TOP 5 PROCESE:")
                for i, proc in enumerate(processes[:5], 1):
                    name = proc.get('name', 'Unknown')
                    cpu = proc.get('cpu_percent', 0)
                    memory = proc.get('memory_percent', 0)
                    print(f"   {i}. {name} - CPU: {cpu:.1f}%, RAM: {memory:.1f}%")
            
            print("\n✅ Informații obținute cu succes!")
        else:
            print("❌ Nu s-au putut obține informații")
            
    except Exception as e:
        print(f"❌ Eroare: {e}")

def demo_screenshot():
    """Demo screenshot."""
    print("📸 Demo screenshot...")
    print()
    
    try:
        import bebe_conn
        
        agent = bebe_conn.BebeAgent()
        screenshot_data = agent.take_screenshot()
        
        if screenshot_data:
            print(f"✅ Screenshot capturat cu succes!")
            print(f"   Mărime: {len(screenshot_data)} caractere (base64)")
            print(f"   Dimensiune: {len(screenshot_data) * 3 // 4} bytes")
        else:
            print("❌ Nu s-a putut captura screenshot-ul")
            
    except Exception as e:
        print(f"❌ Eroare: {e}")

def demo_monitoring():
    """Demo monitorizare continuă."""
    print("🔄 Demo monitorizare continuă (30 secunde)...")
    print("   ⏹️  Apasă Ctrl+C pentru a opri")
    print()
    
    try:
        import bebe_conn
        
        agent = bebe_conn.BebeAgent()
        start_time = time.time()
        heartbeat_count = 0
        screenshot_count = 0
        
        while time.time() - start_time < 30:
            # Heartbeat
            if agent.send_heartbeat():
                heartbeat_count += 1
                print(f"💓 Heartbeat #{heartbeat_count} - {datetime.now().strftime('%H:%M:%S')}")
            
            # Screenshot la fiecare 10 secunde
            if int(time.time() - start_time) % 10 == 0 and int(time.time() - start_time) > 0:
                screenshot_data = agent.take_screenshot()
                if screenshot_data:
                    screenshot_count += 1
                    print(f"📸 Screenshot #{screenshot_count} - {datetime.now().strftime('%H:%M:%S')}")
            
            time.sleep(2)
            
        print(f"\n✅ Monitorizare completă!")
        print(f"   💓 Heartbeat-uri: {heartbeat_count}")
        print(f"   📸 Screenshot-uri: {screenshot_count}")
        
    except KeyboardInterrupt:
        print("\n⏹️  Monitorizare oprită")
    except Exception as e:
        print(f"❌ Eroare: {e}")

def main():
    """Funcția principală."""
    show_banner()
    
    while True:
        show_menu()
        
        try:
            choice = input("Alege opțiunea (1-8): ").strip()
            print()
            
            if choice == "1":
                start_local()
            elif choice == "2":
                start_ngrok()
            elif choice == "3":
                start_server_only()
            elif choice == "4":
                start_agent_only()
            elif choice == "5":
                demo_system_info()
            elif choice == "6":
                demo_screenshot()
            elif choice == "7":
                demo_monitoring()
            elif choice == "8":
                print("👋 La revedere!")
                break
            else:
                print("❌ Opțiune invalidă. Încearcă din nou.")
            
            print("\n" + "=" * 70)
            input("Apasă Enter pentru a continua...")
            print()
            
        except KeyboardInterrupt:
            print("\n👋 La revedere!")
            break
        except Exception as e:
            print(f"\n❌ Eroare: {e}")
            input("Apasă Enter pentru a continua...")

if __name__ == "__main__":
    main()
