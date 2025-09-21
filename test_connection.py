#!/usr/bin/env python3
"""
Test Connection - Testează conexiunea BebeConn
Script pentru testarea conexiunii între agent și server
"""

import time
import requests
import json
from datetime import datetime

def test_server_connection(server_url="http://localhost:5000"):
    """Testează conexiunea la server."""
    print(f"🔗 Testez conexiunea la server: {server_url}")
    
    try:
        # Test endpoint de status
        response = requests.get(f"{server_url}/api/status", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print("✅ Server conectat cu succes!")
            print(f"   Status: {data.get('status', 'Unknown')}")
            print(f"   Timestamp: {data.get('timestamp', 'Unknown')}")
            return True
        else:
            print(f"❌ Server răspunde cu status {response.status_code}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Nu se poate conecta la server")
        print("   Verifică dacă serverul rulează")
        return False
    except requests.exceptions.Timeout:
        print("❌ Timeout la conexiunea la server")
        return False
    except Exception as e:
        print(f"❌ Eroare la conexiunea la server: {e}")
        return False

def test_agent_heartbeat(server_url="http://localhost:5000"):
    """Testează trimiterea heartbeat-ului de la agent."""
    print(f"💓 Testez heartbeat-ul agentului...")
    
    try:
        import bebe_conn
        
        agent = bebe_conn.BebeAgent(server_url=server_url)
        success = agent.send_heartbeat()
        
        if success:
            print("✅ Heartbeat trimis cu succes!")
            print(f"   Timestamp: {datetime.now().strftime('%H:%M:%S')}")
            return True
        else:
            print("❌ Heartbeat eșuat")
            return False
            
    except Exception as e:
        print(f"❌ Eroare la trimiterea heartbeat-ului: {e}")
        return False

def test_agent_screenshot(server_url="http://localhost:5000"):
    """Testează capturarea și trimiterea screenshot-ului."""
    print(f"📸 Testez screenshot-ul agentului...")
    
    try:
        import bebe_conn
        
        agent = bebe_conn.BebeAgent(server_url=server_url)
        
        # Captură screenshot
        screenshot_data = agent.take_screenshot()
        if screenshot_data:
            print(f"✅ Screenshot capturat: {len(screenshot_data)} caractere")
            
            # Trimite screenshot
            success = agent.send_screenshot()
            if success:
                print("✅ Screenshot trimis cu succes!")
                return True
            else:
                print("❌ Screenshot nu a fost trimis")
                return False
        else:
            print("❌ Nu s-a putut captura screenshot-ul")
            return False
            
    except Exception as e:
        print(f"❌ Eroare la screenshot: {e}")
        return False

def test_system_info():
    """Testează obținerea informațiilor despre sistem."""
    print(f"📊 Testez informațiile despre sistem...")
    
    try:
        import bebe_conn
        
        agent = bebe_conn.BebeAgent()
        system_info = agent.get_system_info()
        
        if system_info:
            basic = system_info.get('basic_info', {})
            stats = system_info.get('system_stats', {})
            processes = system_info.get('running_processes', [])
            
            print("✅ Informații despre sistem obținute!")
            print(f"   Platforma: {basic.get('platform', 'Unknown')}")
            print(f"   CPU: {stats.get('cpu_percent', 0):.1f}%")
            print(f"   RAM: {stats.get('memory_percent', 0):.1f}%")
            print(f"   Procese: {len(processes)}")
            return True
        else:
            print("❌ Nu s-au putut obține informații despre sistem")
            return False
            
    except Exception as e:
        print(f"❌ Eroare la informațiile despre sistem: {e}")
        return False

def test_full_cycle(server_url="http://localhost:5000"):
    """Testează ciclul complet de monitorizare."""
    print(f"🔄 Testez ciclul complet de monitorizare...")
    
    try:
        import bebe_conn
        
        agent = bebe_conn.BebeAgent(server_url=server_url)
        
        # Test heartbeat
        print("   💓 Testez heartbeat...")
        if not agent.send_heartbeat():
            print("   ❌ Heartbeat eșuat")
            return False
        
        # Test screenshot
        print("   📸 Testez screenshot...")
        screenshot_data = agent.take_screenshot()
        if not screenshot_data:
            print("   ❌ Screenshot eșuat")
            return False
        
        if not agent.send_screenshot():
            print("   ❌ Trimitere screenshot eșuat")
            return False
        
        # Test informații sistem
        print("   📊 Testez informații sistem...")
        system_info = agent.get_system_info()
        if not system_info:
            print("   ❌ Informații sistem eșuate")
            return False
        
        print("✅ Ciclul complet de monitorizare funcționează!")
        return True
        
    except Exception as e:
        print(f"❌ Eroare în ciclul complet: {e}")
        return False

def main():
    """Funcția principală."""
    print("=" * 70)
    print("🧪 BEBECONN - TEST CONEXIUNE")
    print("=" * 70)
    print("   Testează conexiunea și funcționalitatea librăriei")
    print("=" * 70)
    print()
    
    # URL-ul serverului
    server_url = input("URL server (default: http://localhost:5000): ").strip()
    if not server_url:
        server_url = "http://localhost:5000"
    
    print(f"\n🎯 Testez conexiunea la: {server_url}")
    print()
    
    # Teste
    tests = [
        ("Server Connection", lambda: test_server_connection(server_url)),
        ("System Info", test_system_info),
        ("Agent Heartbeat", lambda: test_agent_heartbeat(server_url)),
        ("Agent Screenshot", lambda: test_agent_screenshot(server_url)),
        ("Full Cycle", lambda: test_full_cycle(server_url))
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n{'='*50}")
        print(f"🧪 TEST: {test_name}")
        print('='*50)
        
        try:
            if test_func():
                passed += 1
                print(f"✅ {test_name} - SUCCESS")
            else:
                print(f"❌ {test_name} - FAILED")
        except Exception as e:
            print(f"❌ {test_name} - ERROR: {e}")
        
        time.sleep(1)  # Pauză între teste
    
    # Rezultat final
    print(f"\n{'='*70}")
    print(f"📊 REZULTAT FINAL: {passed}/{total} teste trecute")
    print('='*70)
    
    if passed == total:
        print("🎉 Toate testele au trecut! Librăria funcționează perfect!")
        print("\n🚀 Poți folosi:")
        print("   python start_monitor.py    # Pornire interactivă")
        print("   bebe-conn start            # Pornire directă")
        print("   bebe-conn start --ngrok    # Cu acces extern")
    else:
        print("❌ Unele teste au eșuat. Verifică configurația.")
        print("\n🔧 Soluții posibile:")
        print("   1. Pornește serverul: bebe-conn server")
        print("   2. Verifică portul (5000)")
        print("   3. Verifică firewall-ul")
        print("   4. Reinstalează librăria: pip install -e .")

if __name__ == "__main__":
    main()
