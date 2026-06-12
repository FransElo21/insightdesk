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

    def generate_insight( self, complaints: list[str], days: int ) -> str:
        prompt = f"""
    Anda adalah analis pengaduan profesional.

    Data berikut berasal dari
    {days} hari terakhir.

    Jumlah pengaduan:
    {len(complaints)}

    Daftar pengaduan:

    {chr(10).join(complaints)}

    Analisis data tersebut dan buat output dengan format berikut:

    Ringkasan:
    ...

    Masalah Utama:
    ...

    Trend:
    ...

    Rekomendasi:
    ...

    Gunakan bahasa Indonesia yang profesional,
    ringkas, dan mudah dipahami.

    Fokus pada pola keluhan yang paling sering muncul.
    """

        response = (
            self.client.chat.completions.create(
                model=self.model,
                temperature=0.3,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
        )

        return (
            response
            .choices[0]
            .message
            .content
            .strip()
        )