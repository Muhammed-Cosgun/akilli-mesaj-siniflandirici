import json
from ollama import chat

MODEL = "qwen2.5:7b"


def mesaji_siniflandir(musteri_mesaji):
    prompt = f"""
Sen bir sorun sınıflandırma asistanısın.

Görevin, kullanıcının bildirdiği sorunu aşağıdaki
kategorilerden yalnızca birine sınıflandırmaktır.

Kategoriler:
- fatura: Fatura, ödeme, ücret, para iadesi ve
  ödeme işlemleriyle ilgili sorunlar.
- teknik_destek: Uygulama, giriş, yazılım ve teknik sorunlar.
- genel_talep: Genel şikâyetler, öneriler, üyelik talepleri
  ve bilgi talepleri.

Kurallar:
- Kullanıcının mesajını dikkatlice değerlendir.
- Mesaja en uygun kategoriyi seç.
- Genel hizmet şikâyetlerini, fatura veya teknik sorunlarla
  açıkça ilgili değillerse genel_talep olarak sınıflandır.
- Fatura veya ödeme sorunu içeren şikâyetleri fatura olarak sınıflandır.
- Uygulama, giriş veya yazılım sorunu içeren şikâyetleri
  teknik_destek olarak sınıflandır.
- Bir mesaj birden fazla sorun içeriyorsa, açıkça belirtilen
  sorunlardan en belirgin olanına göre kategori seç.
- Yalnızca kategori bilgisini döndür.
- Açıklama, özet veya yanıt yazma.

Kullanıcı mesajı:
{musteri_mesaji}
"""

    response = chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        format={
            "type": "object",
            "properties": {
                "kategori": {
                    "type": "string",
                    "enum": [
                        "fatura",
                        "teknik_destek",
                        "genel_talep"
                    ]
                }
            },
            "required": ["kategori"]
        },
        options={"temperature": 0}
    )

    sonuc = json.loads(response.message.content)
    return sonuc["kategori"]


def main():
    birimler = {
        "fatura": "Fatura ve Ödeme Birimi",
        "teknik_destek": "Teknik Destek Birimi",
        "genel_talep": "Genel Talepler Birimi"
    }

    print("=== Akıllı Sorun Sınıflandırıcı ===")
    print("Çıkmak için q yaz.\n")

    while True:
        mesaj = input("Sorununuzu yazın: ").strip()

        if mesaj.lower() == "q":
            print("Program kapatıldı.")
            break

        if not mesaj:
            print("Lütfen bir sorun açıklaması girin.\n")
            continue

        try:
            kategori = mesaji_siniflandir(mesaj)
            birim = birimler[kategori]

            print("\n--- Sınıflandırma Sonucu ---")
            print(f"Kategori: {kategori}")
            print(f"İlgili birim: {birim}")
            print(
                f"Sorununuz {birim} birimine "
                "iletilmek üzere sınıflandırıldı."
            )
            print(
                "(Bilgi: Bu uygulama henüz gerçek birim "
                "iletimi yapmaz.)"
            )
            print()

        except json.JSONDecodeError:
            print("Hata: Model geçerli JSON üretmedi.\n")

        except Exception as hata:
            print(f"Hata oluştu: {hata}\n")


if __name__ == "__main__":
    main()
