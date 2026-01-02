#!/usr/bin/env python3   # Python 3 ile çalıştırılacağını belirtir

import socket            # Ağ bağlantıları ve port taraması için
import os                # Terminal temizleme için
from datetime import datetime   # Tarama zamanı için

def clear():
    os.system("clear")   # Terminal ekranını temizler (Kali/Linux)

def banner():
    # Program açıldığında üstte görünen menü/bilgi ekranı
    print("="*60)
    print("               🔥  RANGE NOVA – Port Scanner  🔥")
    print("="*60)
    print("KULLANIM:")
    print(" 1) Tek port tarama:             scan <ip> <port>")
    print(" 2) Port aralığı tarama:         scan <ip> <start>-<end>")
    print(" 3) Tüm portları tarama:         scan <ip> all")
    print(" 4) Çıkış:                        exit")
    print("="*60)

def scan_port(ip, port):
    # Tek bir portun açık mı kapalı mı olduğunu kontrol eder
    try:
        sock = socket.socket()    # Soket oluştur
        sock.settimeout(0.5)      # 0.5 saniyelik timeout
        sock.connect((ip, port))  # Porta bağlanmayı dene
        sock.close()              # Bağlantı başarılı → port açıktır
        return True
    except:
        return False              # Bağlantı hatası → port kapalı

def range_nova_scan(ip, start, end):
    # Belirli port aralığını tarar
    print(f"\n🔎 Tarama Başladı → {ip} ({start}-{end})")
    print("-"*60)

    for p in range(start, end+1):   # Başlangıçtan bitiş portuna kadar
        if scan_port(ip, p):        # Port açıksa ekrana yazdır
            print(f"[AÇIK] Port {p}")

    print("-"*60)
    print("✔️ Tarama Bitti:", datetime.now().strftime("%H:%M:%S"))

def main():
    clear()          # Ekranı temizle
    banner()         # Banner menüsünü göster

    while True:      # Sonsuz döngü, kullanıcı komut bekliyor
        cmd = input("\nRANGE NOVA > ").strip()   # Kullanıcı komutunu al

        if cmd == "exit":         # Çıkış komutu
            print("Çıkılıyor...")
            break

        if cmd.startswith("scan"):   # Kullanıcı tarama komutu girdiyse
            try:
                parts = cmd.split()  # Komutu boşluklara göre ayır

                ip = parts[1]        # Hedef IP
                port_part = parts[2] # Port / aralık / all

                # Tüm portları tarama işlemi
                if port_part == "all":
                    range_nova_scan(ip, 1, 65535)

                # Port aralığı tarama işlemi (örn: 1-1000)
                elif "-" in port_part:
                    start, end = port_part.split("-")
                    range_nova_scan(ip, int(start), int(end))

                # Tek port tarama işlemi
                else:
                    port = int(port_part)
                    print(f"\n🔎 {ip} üzerinde {port} portu kontrol ediliyor...")
                    if scan_port(ip, port):
                        print(f"[AÇIK] Port {port}")
                    else:
                        print(f"[KAPALI] Port {port}")

            except:
                # Kullanıcı hatalı yazarsa uyarı verir
                print("❌ Kullanım hatası! Format: scan <ip> <port/port-range/all>")

        else:
            # Bilinmeyen komut girilirse uyarı verir
            print("❌ Geçersiz komut! 'scan' ya da 'exit' kullan.")

if __name__ == "__main__":
    main()   # Programın ana fonksiyonunu başlatır
