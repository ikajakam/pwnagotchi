# Turbo Push for Pwnagotchi

High-speed, lightweight Python script to upload valid handshake capture (`.pcap`) to 
[wpa-sec.stanev.org](https://wpa-sec.stanev.org)

## Prerequisites
-  **`ohcapi` Plugin Enabled:** This script relies on `ohcapi` to create `.22000` files for valid handshakes check. 
- **If you don't have `.22000` files, this script will assume you have no valid handshakes.**

## Usage

- **Download the script** in your handshakes directory
  ```bash
   wget https://raw.githubusercontent.com/ikajakam/pwnagotchi/main/push.py -O /home/pi/handshakes/push.py
   ```

- **Configure API Key**
    ```bash
    API_KEY = "your-api-key"
    ```

- **Make Executable (Optional)** 
    ```bash
    chmod +x /home/pi/handshakes/turbo_push.py
    ```

#### Run the script manually whenever you want to sync your handshakes

```bash
python3 push.py
```

```bash
python3 /home/pi/handshakes/push.py
```

```bash
echo "alias push='python3 /home/pi/handshakes/push.py'" >> ~/.bashrc && source ~/.bashrc
```


<img width="1600" height="881" alt="image" src="https://github.com/user-attachments/assets/b6e68e1f-4915-40ba-8f35-36fe1eb0b1b4" />
