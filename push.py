import os
import glob
import requests
import time

# --- CONFIGURATION ---
API_KEY = "your-api-key"
HANDSHAKE_DIR = "/home/pi/handshakes/" # update your handshakes directory
TRACKING_FILE = os.path.join(HANDSHAKE_DIR, "uploaded_list.txt")
URL = "https://wpa-sec.stanev.org"
# ---------------------

def load_sent_list():
    if not os.path.exists(TRACKING_FILE):
        return set()
    with open(TRACKING_FILE, 'r') as f:
        return set(line.strip() for line in f)

def update_sent_list(filename):
    with open(TRACKING_FILE, 'a') as f:
        f.write(filename + "\n")

def main():
    print(f"--- jizzzzzzzing uploads ---")
    print(f"Mode: Cookie-based Auth + .22000 Verification")

    sent_files = load_sent_list()
    
    # Fast Validation: Only look at files that have a matching .22000
    # This proves they are valid without needing Scapy.
    hash_files = glob.glob(os.path.join(HANDSHAKE_DIR, "*.22000"))
    
    print(f"Found {len(hash_files)} verified handshakes. Processing...")

    uploaded_count = 0
    
    for hash_path in hash_files:
        base_name = os.path.splitext(os.path.basename(hash_path))[0]
        pcap_filename = base_name + ".pcap"
        pcap_path = os.path.join(HANDSHAKE_DIR, pcap_filename)

        if pcap_filename in sent_files:
            continue
            
        if not os.path.exists(pcap_path):
            continue

        print(f"Uploading {pcap_filename}...", end=" ", flush=True)

        try:
            with open(pcap_path, 'rb') as f:
                # MIMIC GOTCHIPUSH: Send key as a cookie, not in URL
                cookies = {'key': API_KEY}
                files = {'file': f}
                
                r = requests.post(URL, cookies=cookies, files=files, timeout=30)

                if r.status_code == 200:
                    # MIMIC GOTCHIPUSH: Simple success check
                    if "already submitted" in r.text:
                        print("⏭️  Already in uploaded")
                    else:
                        print("✅ UPLOADED")
                    
                    # Always mark as handled so we don't spam
                    update_sent_list(pcap_filename)
                    uploaded_count += 1
                    time.sleep(0.5)
                else:
                    print(f"❌ HTTP {r.status_code}")

        except Exception as e:
            print(f"❌ Error: {e}")

    print(f"\nDone. jizzed {uploaded_count} files.")

if __name__ == "__main__":
    main()
