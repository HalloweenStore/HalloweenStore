# Fitness Plan — iPhone Shortcuts

Kişiselleştirilmiş 8 haftalık spor planı ve iPhone Kestirmeleri.

## Profil

- **Boy:** 178 cm
- **Kilo:** 80 kg (hafif fazla kilo, BMI ~25,2)
- **Özel durum:** Nefes kesilmesi → düşük yoğunluklu program
- **Takviye:** Kreatin 3–5 g/gün

## Dosyalar

| Dosya | Açıklama |
|-------|----------|
| `SPOR-PLANI.md` | Detaylı 8 haftalık program |
| `index.html` | iPhone'dan indirme sayfası |
| `shortcuts/Spor-Planim.shortcut` | Ana menü kestirmesi |
| `shortcuts/Bugunku-Antrenman.shortcut` | Otomatik günlük program |
| `shortcuts/Gun-Sec-Antrenman.shortcut` | Manuel gün seçimi |
| `shortcuts/Kreatin-Hatirlatici.shortcut` | Kreatin hatırlatıcı |

## iPhone'a Kurulum

1. `index.html` dosyasını Safari'de açın (veya GitHub Pages üzerinden)
2. **Spor Planım İndir** butonuna dokunun
3. İndirilen `.shortcut` dosyasına dokunun → **Ekle**

## Kestirmeleri Yeniden Oluşturma

```bash
python3 generate_shortcuts.py
```
