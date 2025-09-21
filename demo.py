#!/usr/bin/env python3
"""
Demo rapid pentru librăria BebeConn
"""

import time
import sys

def demo_import():
    """Demo import și inițializare."""
    print("=== DEMO BebeConn Library ===")
    print()
    
    print("1. Import librărie...")
    try:
        import bebe_conn
        print("   OK - Librăria importată cu succes")
    except ImportError as e:
        print(f"   EROARE - Nu pot importa librăria: {e}")
        return False
    
    print("\n2. Test inițializare...")
    try:
        # Test inițializare fără pornire
        bebe = bebe_conn.BebeConn(ngrok=False, port=5000, screenshot_interval=120)
        print("   OK - BebeConn inițializat")
        
        server = bebe_conn.BebeServer(port=5000)
        print("   OK - BebeServer inițializat")
        
        agent = bebe_conn.BebeAgent(server_url="http://localhost:5000")
        print("   OK - BebeAgent inițializat")
        
    except Exception as e:
        print(f"   EROARE - Inițializare: {e}")
        return False
    
    print("\n3. Test informații sistem...")
    try:
        agent = bebe_conn.BebeAgent()
        system_info = agent.get_system_info()
        
        if system_info and 'basic_info' in system_info:
            basic = system_info['basic_info']
            print(f"   OK - Sistem: {basic.get('platform', 'Unknown')}")
            print(f"   OK - Procese: {len(system_info.get('running_processes', []))}")
        else:
            print("   ATENTIONARE - Informații sistem incomplete")
            
    except Exception as e:
        print(f"   EROARE - Informații sistem: {e}")
        return False
    
    return True

def demo_usage():
    """Demo utilizare."""
    print("\n=== UTILIZARE ===")
    print()
    print("Pentru a porni sistemul complet:")
    print("  bebe-conn start")
    print()
    print("Pentru a porni cu acces extern (ngrok):")
    print("  bebe-conn start --ngrok")
    print()
    print("Pentru a porni cu configurații personalizate:")
    print("  bebe-conn start --ngrok --port 8080 --screenshot 60")
    print()
    print("Pentru a porni doar serverul:")
    print("  bebe-conn server --port 5000")
    print()
    print("Pentru a porni doar agentul:")
    print("  bebe-conn agent --server-url http://localhost:5000")
    print()
    print("În Python:")
    print("  import bebe_conn")
    print("  bebe_conn.start()")

def main():
    """Funcția principală."""
    print("BebeConn Library - Demo Rapid")
    print("=" * 40)
    
    if not demo_import():
        print("\nEROARE - Demo eșuat. Verifică instalarea.")
        sys.exit(1)
    
    demo_usage()
    
    print("\n" + "=" * 40)
    print("SUCCESS - Librăria este gata de utilizare!")
    print("Pentru a porni sistemul, rulează: bebe-conn start")

if __name__ == "__main__":
    main()
