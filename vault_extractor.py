#!/usr/bin/env python3
"""
NEXUS DYNAMICS // VAULT EXTRACTOR UTILITY
Perimeter Security Telemetry - Gate B Relay
Author: FOSS GECT Security Tools Cell
"""

import zipfile
import sys
import os

VAULT_FILE = "stage2_vault.zip"

def main():
    print("=" * 65)
    print(" NEXUS DYNAMICS // PERIMETER VAULT DECRYPTION UTILITY")
    print(" Target: stage2_vault.zip")
    print("=" * 65)
    
    if not os.path.exists(VAULT_FILE):
        print(f"[-] Error: {VAULT_FILE} not found in current directory.")
        return

    pwd = input("Enter vehicle license plate password: ").strip().upper().replace(" ", "")
    
    try:
        with zipfile.ZipFile(VAULT_FILE, 'r') as zf:
            zf.extractall(path="extracted_vault", pwd=pwd.encode('utf-8'))
            print("\n\033[92m[+] SUCCESS: stage2_vault.zip decrypted!\033[0m")
            print("[+] Contents extracted to folder: extracted_vault/")
            print("-" * 65)
            for item in zf.namelist():
                print(f"  -> {item}")
            print("-" * 65)
            print("\n[!] Next Step: Analyze chime_transmission.wav and read stage3_dossier.txt.")
            print("[!] Off-campus Safehouse Node: https://github.com/anjo2007/aether-safehouse-node")
    except RuntimeError:
        print("\n\033[91m[-] ACCESS DENIED: Bad password.\033[0m")
        print("[-] Check camera_04_gate_b.log or cam04_frame.png for the vehicle license plate.")

if __name__ == "__main__":
    main()
