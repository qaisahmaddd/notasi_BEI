import streamlit as st

def load_content():
    glossary = {
        'Notasi Khusus': 'Sistem penomoran unik yang digunakan di Bursa Efek Indonesia (BEI) untuk mengidentifikasi saham-saham tertentu.',
        'Emiten': 'Perusahaan yang telah mendaftar dan sahamnya terdaftar untuk diperdagangkan di Bursa Efek Indonesia (BEI).',
        'Investor': 'Seseorang atau lembaga yang membeli saham atau investasi lainnya dengan tujuan untuk mendapatkan keuntungan jangka panjang.',
        'Trader': 'Seseorang yang melakukan perdagangan saham atau investasi lainnya dengan tujuan untuk mendapatkan keuntungan jangka pendek dari perubahan harga pasar.',
        'Bursa Efek Indonesia (BEI)': 'Lembaga yang menyediakan fasilitas untuk perdagangan saham dan instrumen keuangan lainnya di Indonesia.',
        'Aplikasi OLT': 'Online Trading adalah platform elektronik yang memungkinkan investor untuk melakukan perdagangan saham secara online.',
        'Fundamental': 'Analisis yang mengidentifikasi saham-saham dengan menganalisis laporan keuangan, kinerja perusahaan, dan faktor ekonomi lainnya.',
        'Ekuitas Negatif': 'Kondisi di mana liabilitas suatu perusahaan melebihi nilainya aset.',
        'IPO': 'Penawaran saham perdana, yaitu proses di mana perusahaan pertama kali menjual sahamnya kepada publik.'
    }

    # Menampilkan ekspander di sidebar
    with st.sidebar.expander('Glossary Kata'):
        pilihan_kata = list(glossary.keys())
        kata_dipilih = st.selectbox('Pilih kata yang tidak dimengerti:', pilihan_kata, key="glossary_selectbox")
        if st.button('Cari Definisi!', key="glossary_button"):
            st.write(glossary[kata_dipilih])



    with st.sidebar.expander('Deskripsi Notasi Khusus'):
        st.markdown("""
            <div style="text-align: center;">
            <h2>Deskripsi Notasi Khusus</h2>
            <h4><a href="https://www.idx.co.id/id/perusahaan-tercatat/notasi-khusus/" target="_blank" rel="noopener noreferrer">Sumber: BEI Website</a></h4>
            </div>
            </div>
            <div style="display: flex; justify-content: center;">
            <table class="editorDemoTable" style="width: 300px;">
                <thead>
                    <tr>
                        <th style="width: 10px; text-align: center;">Huruf</th>
                        <th style="width: 290px; text-align: center;">Deskripsi</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td style="text-align: center;"><strong>A</strong></td>
                        <td style="text-align: left;">Adanya Opini Tidak Wajar (Adverse) dari Akuntan Publik</td>
                    </tr>
                    <tr>
                        <td style="text-align: center;"><strong>B</strong></td>
                        <td style="text-align: left;">Adanya permohonan Pernyataan Pailit, permohonan pembatalan perdamaian, atau dalam kondisi pailit</td>
                    </tr>
                    <tr>
                        <td style="text-align: center;"><strong>C</strong></td>
                        <td style="text-align: left;">Kejadian perkara hukum terhadap Perusahaan Tercatat, Anak Perusahaan Tercatat dan/atau anggota Direksi dan anggota Dewan Komisaris Perusahaan Tercatat yang berdampak Material</td>
                    </tr>
                    <tr>
                        <td style="text-align: center;"><strong>D</strong></td>
                        <td style="text-align: left;">Adanya Opini "Tidak Menyatakan Pendapat (Disclaimer)" dari Akuntan Publik</td>
                    </tr>
                    <tr>
                        <td style="text-align: center;"><strong>E</strong></td>
                        <td style="text-align: left;">Laporan keuangan terakhir menunjukkan ekuitas negatif</td>
                    </tr>
                    <tr>
                        <td style="text-align: center;"><strong>F</strong></td>
                        <td style="text-align: left;">Sanksi administratif dan/atau perintah tertulis dari Otoritas Jasa Keuangan yang dikenakan terhadap Perusahaan Tercatat karena pelanggaran peraturan di bidang Pasar Modal dengan kategori pelanggaran ringan</td>
                    </tr>
                    <tr>
                        <td style="text-align: center;"><strong>G</strong></td>
                        <td style="text-align: left;">Sanksi administratif dan/atau perintah tertulis dari Otoritas Jasa Keuangan yang dikenakan terhadap Perusahaan Tercatat karena pelanggaran peraturan di bidang Pasar Modal dengan kategori pelanggaran sedang</td>
                    </tr>
                    <tr>
                        <td style="text-align: center;"><strong>I</strong></td>
                        <td style="text-align: left;">Perusahaan Tercatat yang tidak menerapkan Saham Dengan Hak Suara Multipel dan tercatat di Papan Ekonomi Baru</td>
                    </tr>
                    <tr>
                        <td style="text-align: center;"><strong>K</strong></td>
                        <td style="text-align: left;">Perusahaan Tercatat yang menerapkan Saham Dengan Hak Suara Multipel dan tercatat di Papan Ekonomi Baru</td>
                    </tr>
                    <tr>
                        <td style="text-align: center;"><strong>L</strong></td>
                        <td style="text-align: left;">Perusahaan Tercatat belum menyampaikan laporan keuangan</td>
                    </tr>
                    <tr>
                        <td style="text-align: center;"><strong>M</strong></td>
                        <td style="text-align: left;">Adanya permohonan Penundaan Kewajiban Pembayaran Utang (PKPU)</td>
                    </tr>
                    <tr>
                        <td style="text-align: center;"><strong>N</strong></td>
                        <td style="text-align: left;">Perusahaan Tercatat yang menerapkan Saham Dengan Hak Suara Multipel dan tercatat di Papan Utama atau Papan Pengembangan</td>
                    </tr>
                    <tr>
                        <td style="text-align: center;"><strong>Q</strong></td>
                        <td style="text-align: left;">Pembatasan kegiatan usaha Perusahaan Tercatat dan/atau anak Perusahaan Tercatat oleh regulator</td>
                    </tr>
                    <tr>
                        <td style="text-align: center;"><strong>S</strong></td>
                        <td style="text-align: left;">Laporan keuangan terakhir menunjukkan tidak ada pendapatan usaha</td>
                    </tr>
                    <tr>
                        <td style="text-align: center;"><strong>V</strong></td>
                        <td style="text-align: left;">Sanksi administratif dan/atau perintah tertulis dari Otoritas Jasa Keuangan yang dikenakan terhadap Perusahaan Tercatat karena pelanggaran peraturan di bidang Pasar Modal dengan kategori pelanggaran berat</td>
                    </tr>
                    <tr>
                        <td style="text-align: center;"><strong>X</strong></td>
                        <td style="text-align: left;">Perusahaan Tercatat dicatatkan di Papan Pemantauan Khusus</td>
                    </tr>
                    <tr>
                        <td style="text-align: center;"><strong>Y</strong></td>
                        <td style="text-align: left;">Perusahaan Tercatat yang belum menyelenggarakan Rapat Umum Pemegang Saham Tahunan (RUPST) sampai dengan 6 (enam) bulan setelah tahun buku berakhir</td>
                    </tr>
                    <!-- Tambahkan baris lainnya sesuai kebutuhan -->
                </tbody>
            </table>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("""
    <div style="display: flex; justify-content: center; align-items: center; flex-direction: column;">
        <h1 style="text-align: center;">DASHBOARD NOTASI KHUSUS</h1>
        <h2 style="text-align: center;">Emiten Bursa Efek Indonesia</h2>
        <h4 style="text-align: center;">✍🏻 Qais Ahmad ✍🏻</h4>
        <div style="display: flex; justify-content: center;">
            <a href="https://github.com/qaisahmaddd" target="_blank"><img alt="Github" src="https://img.shields.io/badge/GitHub-%2312100E.svg?&style=for-the-badge&logo=Github&logoColor=white" /></a>
            <a href="https://www.linkedin.com/in/qais-ahmad-45b36280/" target="_blank"><img alt="LinkedIn" src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" /></a>
            <a href="https://huggingface.co/qaisahmad" target="_blank"><img alt="HuggingFace" src="https://img.shields.io/badge/huggingface-%2312100E.svg?&style=for-the-badge&logo=huggingface&logoColor=white" /></a>
        </div>
        <hr style="width: 50%; margin-top: 20px; margin-bottom: 20px;">
    </div>
""", unsafe_allow_html=True)

    # Notasi Khusus BEI
    with st.expander("Disclaimer"):
        st.markdown("""
            <div style="display: flex; justify-content: center; align-items: center;">
                <div style="text-align: center;">
                    <img src="https://cdn.pixabay.com/animation/2023/04/28/18/34/18-34-10-554_512.gif" alt="animated" width="100"/>
                    <h3>|| ======  DISCLAIMER  ====== ||</h3>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        * Tidak ada maksud untuk menyebarkan isu negatif dalam artikel ini.
        * Notasi Khusus tidak bersifat permanen, bahkan dalam hitungan minggu, stempel ini sudah tidak melekat lagi pada emiten.  
        * Jika dibandingkan pada saat anda membaca, mungkin data emiten sudah tidak sama lagi.
        * Artikel ini disusun untuk tujuan edukasi saham untuk investor pemula dan latihan analisis bagi penulis.
        * Emiten yang tidak ada di dalam artikel ini, tidak secara kontan adalah emiten terbaik.  
        * Segala keputusan berinvestasi merupakan tanggung jawab individu masing-masing.  
    
        Untuk pengalaman yang lebih baik, jika Anda menggunakan smartphone, putarlah smartphone Anda.
        """)
        
        st.markdown(
            """
            <style>
            .centered-image {
                display: flex;
                justify-content: center;
                align-items: center;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
        '<div class="centered-image"><img src="https://assets-v2.lottiefiles.com/a/685770f2-1168-11ee-8e72-c72882ce9865/CQuMaUaImx.gif" alt="Rotate Phone" width="250px" height="250px"></div>',
        unsafe_allow_html=True,
        )
    
    with st.expander("Pendahuluan"):
        intro_html = """
        <div style="text-align: justify;">
        <p>Saya termasuk investor (maksud saya trader) generasi Covid-19. Walaupun sering mendapatkan momentum pasar <i>turn-around</i>, namun tidak jarang pula saya <i>cut-loss</i> karena terbujuk isu-isu yang dibesar-besarkan oleh influencer saham. Saya bahkan tidak menyadari bahwa beberapa dari perusahaan-perusahaan tersebut memiliki risiko tinggi yang jelas-jelas terlihat. Beruntung, profil risiko saya tidak agresif, sehingga saya selalu was-was ketika nilai investasi saya turun atau tidak menghasilkan dalam waktu tertentu.</p>
        <p>Sebenarnya Bursa Efek Indonesia telah melakukan upaya untuk mencegah investor pemula agar lebih berhati-hati dalam berinvestasi saham dengan memberikan petunjuk berupa notasi pada beberapa emiten perusahaan, namun masih banyak investor pemula yang belum memahami sepenuhnya pentingnya notasi tersebut. Notasi-notasi tersebut layaknya sebatas hiasan saja di aplikasi OLT, padahal sebagian besar (tidak semua notasi) bersifat negatif, menunjukkan risiko tinggi dalam investasi. Penting untuk diketahui bahwa notasi-notasi tersebut sangat berguna sebagai tanda atau peringatan bagi investor pemula ketika mereka ingin membeli saham.</p>
        <p>Diluar notasi khusus yang ada pada artikel ini, bukan berarti seluruh saham-saham tersebut secara kontan adalah saham yang baik atau bagus fundamentalnya. Masih ada banyak faktor di luar ini, notasi khusus merupakan <b>salah satu</b> bukan satu-satunya cara mencari saham yang baik. Hal ini seharusnya menjadi rem khususnya para investor pemula untuk lebih berhati-hati dengan mendalami kondisi perusahaan tersebut.</p>
        </div>
        """
        st.write(intro_html, unsafe_allow_html=True)

        st.image("https://syariahsaham.id/wp-content/uploads/2023/11/New-Peter-Lynch.webp", caption="Peter Lynch")
        st.write("""
        <div style="text-align: center;">
        <blockquote>
        <p>"behind every stock is a company. find out what it’s doing"</p>
        <footer>- Peter Lynch</footer>
        </blockquote>
        </div>""", unsafe_allow_html=True)
        
        intro_html2 = """
        <div style="text-align: justify;">
        <p>Dalam artikel ini, saya akan menganalisis beberapa notasi khusus Bursa Efek Indonesia untuk beberapa emiten yang ada di pasar saham Indonesia saat ini.</p>
        <p>Di samping kiri, jika anda menggunakan smartphone, silahkan tap arrow sehingga sidebar terbuka. Saya telah menyiapkan keterangan dari setiap notasi yang sumbernya langsung dari website Bursa Efek Indonesia.</p>
        <p>Untuk memudahkan analisa, saya mengelompokkan notasi-notasi tersebut berdasarkan lingkup masalahnya sebagai berikut:</p>
                """
        intro_html3 = """
        <div style="display: flex; justify-content: center;">
        <table class="editorDemoTable" style="width: 500px; height: 334px;">
        <thead>
        <tr>
        <td style="width: 500px; text-align: left;" colspan="2"><strong>Keuangan</strong></td>
        </tr>
        <tr style="height: 18px;">
        <td style="width: 23.1016px; height: 18px; text-align: center;"><strong>B</strong></td>
        <td style="width: 299.898px; height: 18px;">Pernyataan Pailit, pembatalan perdamaian, atau kondisi pailit</td>
        </tr>
        </thead>
        <tbody>
        <tr style="height: 18px;">
        <td style="width: 23.1016px; height: 18px; text-align: center;"><strong>D</strong></td>
        <td style="width: 299.898px; height: 18px;">Opini 'Tidak Menyatakan Pendapat (Disclaimer)' dari Akuntan Publik</td>
        </tr>
        <tr style="height: 22px;">
        <td style="width: 23.1016px; height: 22px; text-align: center;"><strong>E</strong></td>
        <td style="width: 299.898px; height: 22px;">Laporan keuangan menunjukkan ekuitas negatif</td>
        </tr>
        <tr style="height: 22px;">
        <td style="width: 23.1016px; height: 22px; text-align: center;"><strong>A</strong></td>
        <td style="width: 299.898px; height: 22px;">Opini Tidak Wajar (Adverse) dari Akuntan Publik</td>
        </tr>
        <tr style="height: 18px;">
        <td style="width: 23.1016px; height: 18px; text-align: center;"><strong>M</strong></td>
        <td style="width: 299.898px; height: 18px;">Adanya permohonan Penundaan Kewajiban Pembayaran Utang (PKPU)</td>
        </tr>
        <tr>
        <td style="width: 500px; text-align: left;" colspan="2"><strong>Sanksi</strong></td>
        </tr>
        <tr style="height: 18px;">
        <td style="width: 23.1016px; height: 18px; text-align: center;"><strong>Q</strong></td>
        <td style="width: 299.898px; height: 18px;">Pembatasan kegiatan usaha oleh regulator</td>
        </tr>
        <tr style="height: 18px;">
        <td style="width: 23.1016px; height: 18px; text-align: center;"><strong>F</strong></td>
        <td style="width: 299.898px; height: 18px;">Sanksi administratif dari Otoritas Jasa Keuangan (ringan)</td>
        </tr>
        <tr style="height: 22px;">
        <td style="width: 23.1016px; height: 22px; text-align: center;"><strong>G</strong></td>
        <td style="width: 299.898px; height: 22px;">Sanksi administratif dari Otoritas Jasa Keuangan (sedang)</td>
        </tr>
        <tr style="height: 22px;">
        <td style="width: 23.1016px; height: 22px; text-align: center;"><strong>V</strong></td>
        <td style="width: 299.898px; height: 22px;">Sanksi administratif dari Otoritas Jasa Keuangan (berat)</td>
        </tr>
        <tr>
        <td style="width: 500px; text-align: left;" colspan="2"><strong>Administrasi</strong></td>
        </tr>
        <tr style="height: 18px;">
        <td style="width: 23.1016px; height: 18px; text-align: center;"><strong>L</strong></td>
        <td style="width: 299.898px; height: 18px;">Belum menyampaikan laporan keuangan</td>
        </tr>
        <tr style="height: 18px;">
        <td style="width: 23.1016px; height: 18px; text-align: center;"><strong>S</strong></td>
        <td style="width: 299.898px; height: 18px;">Laporan keuangan tanpa pendapatan usaha</td>
        </tr>
        <tr style="height: 22px;">
        <td style="width: 23.1016px; height: 22px; text-align: center;"><strong>Y</strong></td>
        <td style="width: 299.898px; height: 22px;">Belum menyelenggarakan Rapat Umum Pemegang Saham Tahunan (RUPST) tepat waktu</td>
        </tr>
        <tr>
        <td style="width: 500px; text-align: left;" colspan="2"><strong>Struktur</strong></td>
        </tr>
        <tr style="height: 18px;">
        <td style="width: 23.1016px; height: 18px; text-align: center;"><strong>N</strong></td>
        <td style="width: 299.898px; height: 18px;">Saham dengan Hak Suara Multipel (Papan Utama atau Papan Pengembangan)</td>
        </tr>
        <tr style="height: 18px;">
        <td style="width: 23.1016px; height: 18px; text-align: center;"><strong>K</strong></td>
        <td style="width: 299.898px; height: 18px;">Saham dengan Hak Suara Multipel (Papan Ekonomi Baru)</td>
        </tr>
        <tr style="height: 22px;">
        <td style="width: 23.1016px; height: 22px; text-align: center;"><strong>I</strong></td>
        <td style="width: 299.898px; height: 22px;">Saham tanpa Hak Suara Multipel (Papan Ekonomi Baru)</td>
        </tr>
        <tr>
        <td style="width: 500px; text-align: left;" colspan="2"><strong>Hukum</strong></td>
        </tr>
        <tr style="height: 18px;">
        <td style="width: 23.1016px; height: 18px; text-align: center;"><strong>C</strong></td>
        <td style="width: 299.898px;">Perkara hukum yang signifikan</td>
        </tr>
        <tr>
        <td style="width: 500px; text-align: left;" colspan="2"><strong>Pemantauan Khusus</strong></td>
        </tr>
        <tr style="height: 18px;">
        <td style="width: 23.1016px; height: 18px; text-align: center;"><strong>X</strong></td>
        <td style="width: 299.898px; height: 18px;">Dicatatkan di Papan Pemantauan Khusus</td>
        </tr>
        </tbody>
        </table>
        </div>
            """
        st.write(intro_html2, unsafe_allow_html=True)
        st.write(intro_html3, unsafe_allow_html=True)


    with st.expander("Tentang Web App ini"):
        st.markdown("""
            <h3>Tentang Data</h3>
            <ul>
                <li>Data dari aplikasi ini diperoleh dari website resmi Bursa Efek Indonesia (BEI) <a href="https://www.idx.co.id/">IDX</a>.</li>
                <li>Metode pengumpulan data bukan dari hasil web scraping.</li>
                <li>Data yang digunakan didownload pada awal bulan April 2024.</li>
                <li>Data transaksi yang digunakan adalah data bulan Maret 2024, selama satu bulan penuh.</li>
                <li>Semua data yang telah dikumpulkan dan digabungkan (file-file terlampir dalam direktori).</li>
            </ul>

            <h3>Tentang Fitur</h3>
            <ul>
                <li>Fitur 1 | <strong>Eksplorasi Jumlah Emiten berdasarkan Tahun IPO</strong><br>
                Menampilkan jumlah emiten berdasarkan tahun Initial Public Offering (IPO) dengan notasi khusus yang dipilih.</li>
                <li>Fitur 2 | <strong>Eksplorasi Sektor dengan Notasi Khusus</strong><br>
                Menampilkan sektor apa saja yang memiliki notasi khusus berdasarkan tahun IPO yang dipilih.</li>
                <li>Fitur 3 | <strong>Eksplorasi Detail Perusahaan dengan Notasi Khusus</strong><br>
                Menampilkan detail perusahaan yang masuk ke dalam notasi atau kasus yang dipilih dalam bentuk tabel.</li>
                <li>Fitur 4 | <strong>Eksplorasi Trend Emiten selama Bulan Maret 2024</strong><br>
                Menampilkan tren emiten yang dipilih selama bulan Maret 2024.</li>
            </ul>
            """, unsafe_allow_html=True)
