#!/usr/bin/env python3
"""
Script pentru instalare și test rapid al librăriei BebeConn
"""

import subprocess
import sys
import os

def run_command(cmd, description):
    """Rulează o comandă și afișează rezultatul."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completat")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Eroare la {description}: {e}")
        if e.stderr:
            print(f"Stderr: {e.stderr}")
        return False

def install_dependencies():
    """Instalează dependențele."""
    return run_command("pip install -r requirements.txt", "Instalare dependențe")

def install_library():
    """Instalează librăria în mod development."""
    return run_command("pip install -e .", "Instalare librărie în mod development")

def test_library():
    """Testează librăria."""
    return run_command("python test_library.py", "Test librărie")

def main():
    """Funcția principală."""
    print("🚀 BebeConn Library - Instalare și Test")
    print("=" * 50)
    
    # Verifică dacă suntem în directorul corect
    if not os.path.exists("setup.py"):
        print("❌ Nu sunt în directorul corect. Rulează din directorul bebe-conn-library/")
        sys.exit(1)
    
    # Instalare dependențe
    if not install_dependencies():
        print("❌ Instalarea dependențelor a eșuat")
        sys.exit(1)
    
    # Instalare librărie
    if not install_library():
        print("❌ Instalarea librăriei a eșuat")
        sys.exit(1)
    
    # Test librărie
    if not test_library():
        print("❌ Testul librăriei a eșuat")
        sys.exit(1)
    
    print("\n🎉 Instalare și test completate cu succes!")
    print("\n📖 Acum poți folosi:")
    print("  bebe-conn start                    # Pornire locală")
    print("  bebe-conn start --ngrok           # Pornire cu ngrok")
    print("  python -c 'import bebe_conn; bebe_conn.start()'")
    
    # Întrebă dacă vrea să pornească sistemul
    choice = input("\n❓ Vrei să pornești sistemul acum? (y/N): ").strip().lower()
    if choice == 'y':
        print("\n🚀 Pornesc sistemul...")
        try:
            from bebe_conn import start
            start()
        except KeyboardInterrupt:
            print("\n⏹️  Sistem oprit de utilizator")
        except Exception as e:
            print(f"❌ Eroare la pornirea sistemului: {e}")

if __name__ == "__main__":
    main()
