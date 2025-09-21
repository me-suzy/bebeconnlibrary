#!/usr/bin/env python3
"""
Script pentru build și upload la PyPI
"""

import os
import sys
import subprocess
import shutil

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

def clean_build():
    """Șterge folderele de build."""
    print("🧹 Curățare foldere de build...")
    folders_to_clean = ['build', 'dist', 'bebe_conn.egg-info']
    for folder in folders_to_clean:
        if os.path.exists(folder):
            shutil.rmtree(folder)
            print(f"✅ Șters {folder}")

def build_package():
    """Construiește pachetul."""
    return run_command("python -m build", "Build pachet")

def upload_to_testpypi():
    """Upload la TestPyPI."""
    return run_command("python -m twine upload --repository testpypi dist/*", "Upload la TestPyPI")

def upload_to_pypi():
    """Upload la PyPI."""
    return run_command("python -m twine upload dist/*", "Upload la PyPI")

def install_test():
    """Testează instalarea."""
    return run_command("pip install bebe-conn", "Test instalare")

def main():
    """Funcția principală."""
    print("🚀 BebeConn - Build și Upload la PyPI")
    print("=" * 50)
    
    # Verifică dacă suntem în directorul corect
    if not os.path.exists("setup.py"):
        print("❌ Nu sunt în directorul corect. Rulează din directorul bebe-conn/")
        sys.exit(1)
    
    # Curățare
    clean_build()
    
    # Build
    if not build_package():
        print("❌ Build eșuat")
        sys.exit(1)
    
    # Alege destinația
    print("\n📦 Alege destinația:")
    print("1. TestPyPI (pentru testare)")
    print("2. PyPI (pentru producție)")
    print("3. Doar build (fără upload)")
    
    choice = input("Alege (1/2/3): ").strip()
    
    if choice == "1":
        if upload_to_testpypi():
            print("✅ Upload la TestPyPI completat!")
            print("🔗 Testează cu: pip install --index-url https://test.pypi.org/simple/ bebe-conn")
        else:
            print("❌ Upload la TestPyPI eșuat")
    
    elif choice == "2":
        confirm = input("⚠️  Ești sigur că vrei să uploadezi la PyPI? (y/N): ").strip().lower()
        if confirm == 'y':
            if upload_to_pypi():
                print("✅ Upload la PyPI completat!")
                print("🔗 Instalează cu: pip install bebe-conn")
            else:
                print("❌ Upload la PyPI eșuat")
        else:
            print("❌ Upload anulat")
    
    elif choice == "3":
        print("✅ Build completat! Pachetul este în folderul dist/")
    
    else:
        print("❌ Alegere invalidă")
        sys.exit(1)
    
    print("\n🎉 Proces completat!")

if __name__ == "__main__":
    main()
