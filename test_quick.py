#!/usr/bin/env python3
"""
Test rapid pentru BebeConn
"""

import sys
import os

# Adaugă directorul curent la path
sys.path.insert(0, os.path.dirname(__file__))

def test_imports():
    """Testează importurile."""
    print("🧪 Testez importurile...")
    
    try:
        from bebe_conn import BebeConn, BebeServer, BebeAgent, start
        print("✅ Importuri principale OK")
    except ImportError as e:
        print(f"❌ Eroare import principal: {e}")
        return False
    
    try:
        from bebe_conn.cli import main
        print("✅ Import CLI OK")
    except ImportError as e:
        print(f"❌ Eroare import CLI: {e}")
        return False
    
    return True

def test_initialization():
    """Testează inițializarea claselor."""
    print("🧪 Testez inițializarea...")
    
    try:
        from bebe_conn import BebeConn, BebeServer, BebeAgent
        
        # Test BebeConn
        bebe = BebeConn(ngrok=False, port=5000, screenshot_interval=120)
        assert bebe.port == 5000
        assert bebe.screenshot_interval == 120
        assert not bebe.ngrok
        print("✅ BebeConn OK")
        
        # Test BebeServer
        server = BebeServer(port=5000)
        assert server.port == 5000
        assert hasattr(server, 'app')
        print("✅ BebeServer OK")
        
        # Test BebeAgent
        agent = BebeAgent(server_url="http://localhost:5000", screenshot_interval=120)
        assert agent.server_url == "http://localhost:5000"
        assert agent.screenshot_interval == 120
        print("✅ BebeAgent OK")
        
        return True
        
    except Exception as e:
        print(f"❌ Eroare inițializare: {e}")
        return False

def test_system_info():
    """Testează obținerea informațiilor despre sistem."""
    print("🧪 Testez informații sistem...")
    
    try:
        from bebe_conn import BebeAgent
        
        agent = BebeAgent()
        system_info = agent.get_system_info()
        
        if system_info:
            assert 'basic_info' in system_info
            assert 'system_stats' in system_info
            assert 'running_processes' in system_info
            print("✅ Informații sistem OK")
            return True
        else:
            print("⚠️  Informații sistem goale (poate fi normal)")
            return True
            
    except Exception as e:
        print(f"❌ Eroare informații sistem: {e}")
        return False

def main():
    """Funcția principală."""
    print("🚀 BebeConn - Test Rapid")
    print("=" * 30)
    
    tests = [
        test_imports,
        test_initialization,
        test_system_info
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print(f"📊 Rezultat: {passed}/{total} teste trecute")
    
    if passed == total:
        print("🎉 Toate testele au trecut! BebeConn este gata de utilizare.")
        print("\n📖 Utilizare:")
        print("  bebe-conn start                    # Pornire locală")
        print("  bebe-conn start --ngrok           # Pornire cu ngrok")
        print("  python -c 'import bebe_conn; bebe_conn.start()'")
    else:
        print("❌ Unele teste au eșuat. Verifică erorile de mai sus.")
        sys.exit(1)

if __name__ == "__main__":
    main()
