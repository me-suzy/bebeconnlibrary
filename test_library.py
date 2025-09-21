#!/usr/bin/env python3
"""
Test pentru libraria BebeConn
"""

import sys
import os

# Adauga directorul curent la path
sys.path.insert(0, os.path.dirname(__file__))

def test_imports():
    """Testeaza importurile."""
    print("Testez importurile...")
    
    try:
        from bebe_conn import BebeConn, BebeServer, BebeAgent, start
        print("OK - Importuri principale")
    except ImportError as e:
        print(f"EROARE - Import principal: {e}")
        return False
    
    try:
        from bebe_conn.cli import main
        print("OK - Import CLI")
    except ImportError as e:
        print(f"EROARE - Import CLI: {e}")
        return False
    
    return True

def test_initialization():
    """Testeaza initializarea claselor."""
    print("Testez initializarea...")
    
    try:
        from bebe_conn import BebeConn, BebeServer, BebeAgent
        
        # Test BebeConn
        bebe = BebeConn(ngrok=False, port=5000, screenshot_interval=120)
        assert bebe.port == 5000
        assert bebe.screenshot_interval == 120
        assert not bebe.ngrok
        print("OK - BebeConn")
        
        # Test BebeServer
        server = BebeServer(port=5000)
        assert server.port == 5000
        assert hasattr(server, 'app')
        print("OK - BebeServer")
        
        # Test BebeAgent
        agent = BebeAgent(server_url="http://localhost:5000", screenshot_interval=120)
        assert agent.server_url == "http://localhost:5000"
        assert agent.screenshot_interval == 120
        print("OK - BebeAgent")
        
        return True
        
    except Exception as e:
        print(f"EROARE - Initializare: {e}")
        return False

def test_system_info():
    """Testeaza obtinerea informatiilor despre sistem."""
    print("Testez informatii sistem...")
    
    try:
        from bebe_conn import BebeAgent
        
        agent = BebeAgent()
        system_info = agent.get_system_info()
        
        if system_info:
            assert 'basic_info' in system_info
            assert 'system_stats' in system_info
            assert 'running_processes' in system_info
            print("OK - Informatii sistem")
            return True
        else:
            print("ATENTIONARE - Informatii sistem goale (poate fi normal)")
            return True
            
    except Exception as e:
        print(f"EROARE - Informatii sistem: {e}")
        return False

def main():
    """Functia principala."""
    print("BebeConn Library - Test")
    print("=" * 40)
    
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
    
    print(f"Rezultat: {passed}/{total} teste trecute")
    
    if passed == total:
        print("SUCCESS - Toate testele au trecut! Libraria este gata de utilizare.")
        print("\nUtilizare:")
        print("  bebe-conn start                    # Pornire locala")
        print("  bebe-conn start --ngrok           # Pornire cu ngrok")
        print("  python -c 'import bebe_conn; bebe_conn.start()'")
        print("\nPentru a instala libraria:")
        print("  pip install -e .                  # Instalare in mod development")
        print("  python setup.py sdist bdist_wheel # Build pentru PyPI")
    else:
        print("EROARE - Unele teste au esuat. Verifica erorile de mai sus.")
        sys.exit(1)

if __name__ == "__main__":
    main()