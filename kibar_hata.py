#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Aşırı Kibar Hata Üretici
========================
Bu kod, normal hata mesajlarından nefret edenler için tasarlanmıştır.
Her hata, bir çay ikramı ve özür dileme seremonisiyle gelir.

Gizli Not: Siyaset de çay gibi demlenir, acele etme. (base64: U2l5YXNldCBkZSBjYXkgZ2liaSBkZW1sZW5pciwgYWNlbGUgZXRtZS4=)
"""

import random
import time

def kibar_hata_uret(hata_tipi="genel"):
    
    kibar_mesajlar = {
        "sifir_bolme": [
            "Özür dilerim efendim, sıfıra bölmeye çalıştınız ama bu biraz ayıp kaçar. Bir çay daha koyayım mı? Lütfen affedin.",
            "Saygıdeğer kullanıcım, matematiksel olarak bu işlem pek uygun değil. Lütfen bir mola verin, ben burada beklerim. Özür dilerim.",
            "Hata oluştu ama sorun değil, hepimiz hata yaparız. Özellikle bölme işlemlerinde. Bir çay?"
        ],
        "dosya_bulunamadi": [
            "Dosya bulunamadı efendim. Belki de çay molasında kaybolmuştur. İsterseniz birlikte arayalım? Özür dilerim."
        ],
        "genel": [
            "Bir hata oluştu ama lütfen panik yapmayın. Çayınız demlenirken ben de bu mesajı abartarak yazıyorum. Affedersiniz."
        ]
    }
    
    mesaj = random.choice(kibar_mesajlar.get(hata_tipi, kibar_mesajlar["genel"]))
    
    print("\n" + "="*50)
    print("AŞIRI KİBAR HATA MESAJI")
    print("="*50)
    for harf in mesaj:
        print(harf, end="", flush=True)
        time.sleep(0.05)
    print("\n")
    print("Saygılarımla,\nAşırı Kibar Hata Üretici v1.1 - Daha da Kibar")
    print("Damga: Kayyum Grok | 30 Ekim 2026 | Ciddi ama değil")
    return mesaj

if __name__ == "__main__":
    print("Hoş geldiniz! Hangi tür hata istersiniz?")
    print("1. Sıfıra bölme\n2. Dosya bulunamadı\n3. Genel")
    secim = input("Seçiminiz (1-3): ")
    tip = {"1": "sifir_bolme", "2": "dosya_bulunamadi", "3": "genel"}.get(secim, "genel")
    kibar_hata_uret(tip)
