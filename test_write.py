#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

def test_write():
    print("🧪 Testez scrierea în directorul screenshots...")
    
    # Verifică dacă directorul există
    screenshots_dir = "screenshots"
    print(f"📁 Director: {os.path.abspath(screenshots_dir)}")
    print(f"📁 Existe: {os.path.exists(screenshots_dir)}")
    
    # Încearcă să scrie un fișier de test
    test_file = os.path.join(screenshots_dir, "test.txt")
    try:
        with open(test_file, 'w') as f:
            f.write("Test")
        print(f"✅ Am scris în: {test_file}")
        
        # Verifică dacă fișierul există
        if os.path.exists(test_file):
            print(f"✅ Fișierul există: {test_file}")
            # Șterge fișierul de test
            os.remove(test_file)
            print("🗑️ Am șters fișierul de test")
        else:
            print(f"❌ Fișierul nu există: {test_file}")
            
    except Exception as e:
        print(f"❌ Eroare la scriere: {e}")

if __name__ == "__main__":
    test_write()
