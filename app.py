from datetime import datetime
from pathlib import Path

import streamlit as st


BASE_DIR = Path(__file__).resolve().parent
PICT_DIR = BASE_DIR / "pict"
ANNIVERSARY_DATE = datetime(2026, 4, 3, 0, 0, 0)

PHOTO_FILES = [
    "WhatsApp Image 2026-04-02 at 22.02.07.jpeg",
    "WhatsApp Image 2026-04-02 at 22.01.38.jpeg",
    "WhatsApp Image 2026-04-02 at 22.00.49.jpeg",
    "WhatsApp Image 2026-04-02 at 22.00.48.jpeg",
    "WhatsApp Image 2026-04-02 at 22.00.48 (2).jpeg",
    "WhatsApp Image 2026-04-02 at 22.00.48 (1).jpeg",
]


st.set_page_config(
    page_title="1st Anniversary - Caca & Aku",
    page_icon="H",
    layout="wide",
)


def load_photo(filename: str) -> Path:
    return PICT_DIR / filename


def countdown_text() -> str:
    now = datetime.now()
    diff = ANNIVERSARY_DATE - now
    total_seconds = int(diff.total_seconds())
    if total_seconds <= 0:
        return "Hari ini hari anniversary kalian."

    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{hours} jam {minutes} menit {seconds} detik lagi menuju 3 April 2026"


st.markdown(
    """
    <style>
      .stApp {
        background:
          radial-gradient(circle at top left, rgba(255, 204, 191, 0.9), transparent 30%),
          radial-gradient(circle at top right, rgba(232, 146, 157, 0.45), transparent 25%),
          linear-gradient(180deg, #fff9f4 0%, #fff1e7 50%, #ffe6dd 100%);
        color: #3b1f24;
      }
      .block-container {
        max-width: 1180px;
        padding-top: 2rem;
        padding-bottom: 4rem;
      }
      .hero-card,
      .story-card,
      .letter-card,
      .countdown-card {
        background: rgba(255, 251, 248, 0.76);
        border: 1px solid rgba(141, 45, 67, 0.12);
        border-radius: 28px;
        box-shadow: 0 18px 60px rgba(114, 43, 57, 0.14);
        backdrop-filter: blur(12px);
      }
      .hero-card {
        padding: 2.2rem;
      }
      .eyebrow {
        letter-spacing: 0.22em;
        text-transform: uppercase;
        color: #8d2d43;
        font-size: 0.78rem;
        margin-bottom: 0.6rem;
      }
      .title {
        font-family: Georgia, serif;
        font-size: clamp(2.8rem, 5vw, 5rem);
        line-height: 1.02;
        margin: 0;
      }
      .lead {
        color: #7b5962;
        font-size: 1.06rem;
        line-height: 1.8;
        margin-top: 1.1rem;
      }
      .countdown-card {
        margin-top: 1.4rem;
        padding: 1rem 1.2rem;
      }
      .countdown-text {
        color: #8d2d43;
        font-weight: 700;
        font-size: 1.25rem;
      }
      .section-title {
        font-family: Georgia, serif;
        font-size: clamp(2rem, 4vw, 3.3rem);
        line-height: 1.08;
        margin: 0.1rem 0 1.2rem;
      }
      .story-card, .letter-card {
        padding: 1.4rem;
        height: 100%;
      }
      .body-copy {
        color: #7b5962;
        line-height: 1.8;
        font-size: 1rem;
        margin: 0;
      }
      .signature {
        color: #3b1f24;
        font-weight: 700;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

hero_left, hero_right = st.columns([1.08, 0.92], gap="large")

with hero_left:
    st.markdown(
        """
        <div class="hero-card">
          <div class="eyebrow">3 April 2026</div>
          <h1 class="title">Happy 1st Anniversary, Caca.</h1>
          <p class="lead">
            Besok tepat satu tahun perjalanan kalian. Halaman ini dibuat untuk
            mengingat semua momen kecil, lucu, hangat, dan berharga yang sudah dilewati bareng.
          </p>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        f"""
        <div class="countdown-card">
          <div style="color:#7b5962; font-size:0.95rem; margin-bottom:0.45rem;">Menuju hari anniversary</div>
          <div class="countdown-text">{countdown_text()}</div>
        </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with hero_right:
    left_photo, right_photo = st.columns(2, gap="small")
    with left_photo:
        st.image(str(load_photo(PHOTO_FILES[0])), use_container_width=True)
    with right_photo:
        st.image(str(load_photo(PHOTO_FILES[1])), use_container_width=True)

st.markdown('<div style="height: 2.5rem;"></div>', unsafe_allow_html=True)
st.markdown('<div class="eyebrow">Tentang Kita</div>', unsafe_allow_html=True)
st.markdown(
    '<h2 class="section-title">Satu tahun yang terasa cepat, tapi isinya banyak banget.</h2>',
    unsafe_allow_html=True,
)

story_columns = st.columns(3, gap="medium")
story_content = [
    (
        "Selalu ada cerita",
        "Dari obrolan random, candaan receh, sampai momen yang bikin hati tenang, semuanya pelan-pelan jadi rumah.",
    ),
    (
        "Tumbuh bareng",
        "Setahun ini bukan cuma tentang foto yang bagus, tapi tentang gimana kalian tetap saling pilih, saling dengar, dan saling jaga.",
    ),
    (
        "Untuk Caca",
        "Terima kasih karena sudah jadi perempuan yang ngasih warna, perhatian, dan rasa nyaman yang susah dijelasin pakai kata-kata.",
    ),
]

for column, (title, body) in zip(story_columns, story_content):
    with column:
        st.markdown(
            f"""
            <div class="story-card">
              <h3 style="font-family: Georgia, serif; margin-top:0; margin-bottom:0.8rem;">{title}</h3>
              <p class="body-copy">{body}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown('<div style="height: 2.8rem;"></div>', unsafe_allow_html=True)
st.markdown('<div class="eyebrow">Galeri Kenangan</div>', unsafe_allow_html=True)
st.markdown(
    '<h2 class="section-title">Potongan momen yang pengin disimpan lama.</h2>',
    unsafe_allow_html=True,
)

gallery_rows = [
    PHOTO_FILES[:3],
    PHOTO_FILES[3:],
]

for row in gallery_rows:
    cols = st.columns(3, gap="small")
    for col, photo in zip(cols, row):
        with col:
            st.image(str(load_photo(photo)), use_container_width=True)

st.markdown('<div style="height: 2.8rem;"></div>', unsafe_allow_html=True)
st.markdown('<div class="eyebrow">Untuk Kamu</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="letter-card">
      <h2 class="section-title" style="max-width:none;">Selamat 1st anniversary, sayang.</h2>
      <p class="body-copy">
        Caca, terima kasih sudah nemenin satu tahun ini dengan sabar, hangat, dan tulus.
        Hubungan bukan soal hari-hari yang selalu sempurna, tapi soal dua orang yang tetap mau
        jalanin semuanya bareng. Dan hal paling indah adalah, orang itu adalah kamu.
      </p>
      <p class="body-copy" style="margin-top:1rem;">
        Semoga setelah 3 April 2026 ini, masih ada banyak tanggal indah lain yang bisa dirayakan.
        Semoga kalian tetap bikin banyak kenangan baru, sedikit demi sedikit, selama mungkin.
      </p>
      <p class="signature" style="margin-top:1.2rem;">Dengan penuh sayang,<br>Pacarmu</p>
    </div>
    """,
    unsafe_allow_html=True,
)
