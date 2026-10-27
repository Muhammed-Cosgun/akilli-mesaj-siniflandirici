import streamlit as st
from main import mesaji_siniflandir

st.set_page_config(
    page_title="Akıllı Sorun Sınıflandırıcı",
    page_icon="🤖",
    layout="centered"
)

BIRIMLER = {
    "fatura": "Fatura ve Ödeme Birimi",
    "teknik_destek": "Teknik Destek Birimi",
    "genel_talep": "Genel Talepler Birimi"
}

st.title("🤖 Akıllı Sorun Sınıflandırıcı")

st.write(
    "Sorununuzu açıklayın. Yapay zekâ, "
    "sorununuzu uygun kategoriye sınıflandırsın."
)

mesaj = st.text_area(
    "Sorun açıklaması",
    placeholder="Örneğin: Kartımdan iki kez ücret alındı...",
    height=150
)

if st.button("Sorunu Sınıflandır", type="primary"):
    if not mesaj.strip():
        st.warning("Lütfen önce sorun açıklaması girin.")
    else:
        with st.spinner("Sorun sınıflandırılıyor..."):
            try:
                kategori = mesaji_siniflandir(mesaj.strip())
                birim = BIRIMLER[kategori]

                st.success("Sınıflandırma tamamlandı!")

                st.subheader("Sınıflandırma Sonucu")

                KATEGORI_ISIMLERI = {
                    "fatura": "Fatura ve Ödeme",
                    "teknik_destek": "Teknik Destek",
                    "genel_talep": "Genel Talep"
                }

                st.write("**Kategori:**", KATEGORI_ISIMLERI[kategori])
                st.write("**İlgili birim:**", birim)

                st.info(
                    f"Sorununuz {birim} birimine "
                    "iletilmek üzere sınıflandırıldı."
                )

                st.caption(
                    "Not: Bu uygulama henüz gerçek birim "
                    "iletimi yapmamaktadır."
                )

            except Exception as hata:
                st.error(f"Sınıflandırma sırasında hata oluştu: {hata}")
