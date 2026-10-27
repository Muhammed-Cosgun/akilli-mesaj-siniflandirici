# Akıllı Sorun Sınıflandırıcı

Python, Ollama ve Streamlit kullanılarak geliştirilen, kullanıcı mesajlarını yapay zekâ yardımıyla sınıflandıran basit bir web uygulaması.

## Proje Hakkında

Bu uygulama, kullanıcı tarafından girilen sorun veya talep metnini analiz eder ve aşağıdaki kategorilerden birine atar. Ardından ilgili birimi kullanıcıya gösterir.

| Kategori | İlgili Birim |
|---|---|
| `fatura` | Fatura ve Ödeme Birimi |
| `teknik_destek` | Teknik Destek Birimi |
| `genel_talep` | Genel Talepler Birimi |

## Kullanılan Teknolojiler

- Python
- Ollama
- Qwen 2.5 7B (`qwen2.5:7b`)
- Streamlit

## Özellikler

- Kullanıcıdan metin girişi alma
- Yerel dil modeliyle mesaj sınıflandırma
- JSON formatında yapılandırılmış model çıktısı
- Kategoriye göre ilgili birimi belirleme
- Web arayüzü üzerinden sonuçları görüntüleme

## Kurulum

### 1. Depoyu klonlayın

```bash
git clone https://github.com/Muhammed-Cosgun/akilli-mesaj-siniflandirici.git
cd akilli-mesaj-siniflandirici
```

### 2. Sanal ortam oluşturun

```bash
python -m venv .venv
```

Windows PowerShell üzerinde sanal ortamı etkinleştirin:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Gerekli paketleri yükleyin

```bash
python -m pip install ollama streamlit
```

### 4. Ollama ve modeli hazırlayın

Ollama uygulamasının kurulu ve çalışıyor olduğundan emin olun.

```bash
ollama pull qwen2.5:7b
```

Modeli çalıştırmak ve Ollama bağlantısını test etmek için:

```bash
ollama run qwen2.5:7b
```

Bu komut modelin indirilmesini ve yerel olarak çalıştırılmasını sağlar. Model hazır olduğunda uygulamayı çalıştırmadan önce Ollama'nın erişilebilir durumda olduğundan emin olun.

### 5. Uygulamayı başlatın

Proje klasöründe aşağıdaki komutu çalıştırın:

```bash
python -m streamlit run app.py
```

Streamlit uygulaması tarayıcıda açılacaktır.

## Proje Sınırları

Bu proje, mesajları sınıflandırıp ilgili birimi belirleyen bir prototiptir. Mesajlar gerçek bir birime gönderilmez ve otomatik yönlendirme işlemi gerçekleştirilmez.

## Geliştirici

Muhammed Coşgun — Bilgisayar Mühendisi