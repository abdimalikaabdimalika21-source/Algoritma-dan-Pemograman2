import os, time, random, sys

# --- BAGIAN 1: FUNGSI TAMPILAN (yuda) ---
def bersih_layar():
    """Fungsi 1: Menghapus teks di terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def styling(teks, warna_kode):
    """Fungsi 2: Memberi warna ANSI (91: Merah, 92: Hijau, 93: Kuning, 95: Magenta, 96: Cyan)."""
    return f"\033[{warna_kode}m{teks}\033[0m"

def ketik(teks, delay=0.03):
    """Fungsi 3: Efek animasi mengetik untuk narasi."""
    for char in teks:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# --- BAGIAN 2: STATUS & ITEM (nadya) ---
class Ksatria:
    """Fungsi 4: Inisialisasi data pemain (Constructor)."""
    def __init__(self, nama):
        self.nama = nama
        self.level = 5
        self.hp = 200
        self.hp_max = 200
        self.atk = 30
        self.emas = 100
        self.item = ["Ramuan Kecil"]

def tampilkan_status(p):
    """Fungsi 5: Dashboard status pemain."""
    print(styling(f"\n--- ⚔️  {p.nama} (Lv.{p.level}) ---", "96"))
    print(f"❤️  HP: {p.hp}/{p.hp_max} | ⚔️  ATK: {p.atk} | 🪙  Emas: {p.emas}")
    print(f"🎒 Tas: {', '.join(p.item) if p.item else 'Kosong'}")
    print(styling("-" * 35, "90"))

def buka_toko(p):
    """Fungsi 6: Logika belanja di pedagang keliling."""
    bersih_layar()
    print(styling("=== 🏪 PEDAGANG KELILING ELRA ===", "93"))
    print(f"Emasmu: {p.emas}")
    print("1. Ramuan Ajaib (60 Emas) | 0. Keluar")
    pilih = input("\nBeli sesuatu? ")
    if pilih == "1" and p.emas >= 60:
        p.emas -= 60
        p.item.append("Ramuan Ajaib")
        print(styling("✅ Kamu membeli Ramuan Ajaib!", "92"))
    else:
        print(styling("Melanjutkan perjalanan...", "90"))
    time.sleep(1.2)

# --- BAGIAN 3: SISTEM TEMPUR (Abdi) ---
def hitung_aksi(atk, pertahanan):
    """Fungsi 7: Kalkulasi damage dengan angka acak."""
    variasi = random.randint(-5, 10)
    total = (atk - (pertahanan // 2)) + variasi
    return max(10, total)

def gunakan_item(p):
    """Fungsi 8: Memakai ramuan untuk pulihkan HP."""
    if p.item:
        p.item.pop()
        p.hp = min(p.hp_max, p.hp + 100)
        print(styling(f"💊 Ramuan diminum! HP {p.nama} pulih.", "92"))
    else:
        print(styling("⚠️ Kamu tidak punya ramuan!", "91"))
    time.sleep(1)

def pertempuran(p, m):
    """Fungsi 9: Turn-based combat loop."""
    m_hp = m['hp']
    while m_hp > 0 and p.hp > 0:
        bersih_layar()
        print(styling(f"🔥 PERTEMPURAN: {m['nama'].upper()} 🔥", "91"))
        print(f"HP Musuh: {m_hp} / {m['hp']}")
        tampilkan_status(p)
        
        aksi = input("Pilih: (1) Serang (2) Ramuan (3) Lari: ")
        if aksi == "1":
            dmg = hitung_aksi(p.atk, m['def'])
            m_hp -= dmg
            print(styling(f"💥 Tebasanmu mengenai {m['nama']}! ({dmg} dmg)", "92"))
        elif aksi == "2":
            gunakan_item(p)
        elif aksi == "3":
            if random.random() < 0.4: return "lari"
            print("Gagal kabur! Musuh menutup jalanmu!")

        if m_hp > 0:
            m_dmg = hitung_aksi(m['atk'], 10)
            p.hp -= m_dmg
            print(styling(f"👹 {m['nama']} menyerang balik! ({m_dmg} dmg)", "91"))
            time.sleep(1.5)
    return "menang" if p.hp > 0 else "kalah"

# --- BAGIAN 4: PROGRESS & NARASI (Anggota 4) ---
def naik_level(p):
    """Fungsi 10: Upgrade status pemain."""
    p.level += 1
    p.hp_max += 75
    p.hp = p.hp_max
    p.atk += 25
    print(styling(f"\n🌟 LEVEL UP! Level naik ke {p.level}!", "93"))
    time.sleep(2)

def prolog(nama):
    """Fungsi 11: Pembukaan cerita (Prolog)."""
    bersih_layar()
    print(styling("=== ⚔️  PROLOG: KERANGKA TAKDIR ===", "95"))
    ketik(f"Di Kerajaan Elra, hiduplah ksatria muda bernama {styling(nama, '93')}.")
    ketik("Suatu malam, Naga Malachar menculik Putri Elara ke Menara Abadi.")
    ketik(f"Dengan pedang di tangan, {nama} bersumpah untuk membawanya pulang.")
    input(styling("\n[ Tekan Enter untuk Memulai Perjalanan... ]", "90"))

def main():
    """Fungsi 12: Manajer Alur Utama Game & Epilog."""
    bersih_layar()
    print(styling("=== ⚔️  KSATRIA DAN SANG NAGA AGUNG 🐉 ===", "95"))
    nama_p = input("Siapa namamu, Ksatria? ")
    p1 = Ksatria(nama_p if nama_p else "Aldric")
    
    prolog(p1.nama) # Panggil Prolog

    cerita_musuh = [
        {"nama": "Serigala Hutan", "hp": 100, "atk": 20, "def": 5, "duit": 80, "msg": "🌲Menjelajahi Hutan Bayangan🌲"},
        {"nama": "Monster Lava", "hp": 200, "atk": 40, "def": 15, "duit": 100, "msg": "🌋Gunung Merapi🌋"},
        {"nama": "Black Wizard David", "hp": 300, "atk": 50, "def": 20, "duit": 200, "msg": "😎Menara Penyihir!😎"},
        {"nama": "Naga Malachar", "hp": 500, "atk": 60, "def": 25, "duit": 0, "msg": "🐉PUNCAK MENARA ABADI!🐉"}

    ]

    for m in cerita_musuh:
        while True:
            bersih_layar()
            print(f"📍 {styling(m['msg'], '95')}")
            tampilkan_status(p1)
            siap = input(f"Hadapi {m['nama']}? (y) Maju (t) Toko: ").lower()
            if siap == 'y': break
            elif siap == 't': buka_toko(p1)

        if pertempuran(p1, m) == "menang":
            p1.emas += m['duit']
            naik_level(p1)
        else:
            # Epilog Kekalahan
            bersih_layar()
            ketik(styling(f"💀 {p1.nama} gugur. Elra selamanya dalam kegelapan.", "91"))
            return

    # Epilog Kemenangan
    bersih_layar()
    print(styling("=== ✨ EPILOG: KEJAYAAN ELRA ✨ ===", "93"))
    ketik(f"Malachar runtuh! {p1.nama} berhasil menyelamatkan Putri Elara.")
    ketik("Seluruh kerajaan bersorak. Namamu terukir abadi dalam sejarah.")
    print(styling("\n--- TAMAT ---", "96"))

if __name__ == "__main__":
    main()