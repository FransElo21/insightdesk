from openai import OpenAI

from app.core.config import MAIA_API_KEY, MAIA_BASE_URL


class AIService:
    def __init__(self):
        self.client = OpenAI(
            api_key=MAIA_API_KEY,
            base_url=MAIA_BASE_URL,
        )
        self.model = "maia/gemini-3.1-flash-lite-preview"

    def classify(self, text: str) -> str:
        prompt = f"""
Anda adalah sistem klasifikasi pengaduan.

Kategori yang tersedia:

* Jaringan
* Akademik
* Fasilitas
* Keuangan
* Administrasi

Aturan:

* Jawab hanya nama kategori.
* Jangan berikan penjelasan.

Pengaduan:
{text}
"""

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=0,
            messages=[{"role": "user", "content": prompt}],
        )

        return response.choices[0].message.content.strip()

    def sentiment(self, text: str) -> str:
        prompt = f"""
Tentukan sentimen pengaduan berikut.

Pilihan:

* Positif
* Netral
* Negatif

Aturan:

* Jawab hanya satu kata.
* Jangan berikan penjelasan.

Pengaduan:
{text}
"""

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=0,
            messages=[{"role": "user", "content": prompt}],
        )

        return response.choices[0].message.content.strip()

    def generate_insight(self, complaints: list[str]) -> str:
        prompt = f"""
Anda adalah analis pengaduan profesional.

Berikut adalah kumpulan pengaduan:

{chr(10).join(complaints)}

Analisis seluruh data tersebut.

Buat output dengan format berikut:

Ringkasan:
(Jelaskan kondisi umum pengaduan)

Masalah Utama:
(Sebutkan masalah yang paling dominan)

Trend:
(Jelaskan pola atau tren yang terlihat)

Rekomendasi:
(Berikan rekomendasi tindakan)

Gunakan bahasa Indonesia yang profesional,
ringkas, dan mudah dipahami.
"""

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=0.3,
            messages=[{"role": "user", "content": prompt}],
        )

        return response.choices[0].message.content.strip()
