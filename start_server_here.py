#!/usr/bin/env python3
"""
Start Server Here - Pornește serverul din directorul curent
"""

import os
import sys

# Schimbă directorul curent la directorul scriptului
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

print(f"📁 Director curent: {os.getcwd()}")
print("🚀 Pornesc serverul din directorul corect...")

try:
    import bebe_conn
    bebe_conn.start()
except Exception as e:
    print(f"❌ Eroare: {e}")
    sys.exit(1)
