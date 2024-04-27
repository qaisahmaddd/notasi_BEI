import streamlit as st
import pandas as pd
import VizNotation
import pendahuluan
from VizNotation import color_codes as color_codes
from streamlit_option_menu import option_menu

# import mplcursors
df_harian_aktif_NK= pd.read_csv('clean_data/transaksi_NK.csv')
st.set_page_config(layout='wide')

st.markdown(
    """
    <style>
    .reportview-container .main .block-container {
        max-width: 95%;
        padding-top: 2rem;
        padding-right: 2rem;
        padding-left: 2rem;
        padding-bottom: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

pendahuluan.load_content()
with st.expander("Perbandingan Komposisi Emiten"):
    # Title
    st.write(f"<div style='text-align: center;'><h3 style='font-weight: bold; '>{'Dengan VS Tanpa Notasi Khusus'}</h3></div>", unsafe_allow_html=True)
    VizNotation.pie1()

    st.markdown("""
        <div style="text-align: justify;">
        <p>
        Kita bisa lihat <strong>lebih dari seperempat</strong> perusahaan yang ada di Bursa Saham atau sekitar 27.5% berstempel Notasi Khusus. 
        Tentunya angka tersebut tidak semua aktif diperdagangkan. Banyak di antara emiten tersebut yang sedang tertidur di harga Rp. 50 per lembar sahamnya, atau bahkan lebih rendah dari itu.
        </p>
        <p>
        Selanjutnya kita bisa eksplor perbandingan emiten Notasi Khusus yang aktif diperdagangkan sahamnya dengan yang tidak aktif diperdagangkan.
        </p>
        </div>
    """, unsafe_allow_html=True)


    # Title
    st.write(f"<div style='text-align: center;'><h3 style='font-weight: bold; '>{'Aktif VS Tidak Aktif'}</h3></div>", unsafe_allow_html=True)
    VizNotation.total_emiten()
    st.markdown("""
        <div style="text-align: justify;">
        <p>
        Bicara perbandingan seberapa besar persentase perusahaan berstempel Notasi Khusus yang aktif dan tidak aktif diperdagangkan menjadi sangat krusial dan penting untuk ditampilkan. Bisa dibayangkan jika mayoritas perusahaan yang paling bermasalah, paling ramai diperdagangkan.
        </p>
        Kembali mengingatkan, di sisi kiri ada kolom keterangan Notasi yang bisa diinterpretasikan sendiri seberapa besar perusahaan yang bermasalah, <strong>NAMUN BANYAK PEMINATNYA</strong>.
        </p>
        <p>
        Mari kita lanjutkan ke chart di bawah ini.
        </p>
        </div>
    """, unsafe_allow_html=True)
    VizNotation.total_emiten_1()
    st.markdown("""
        <div style="text-align: justify;">
        <p>
        Jika sebelumnya kita membahas dari segi Notasinya, kali ini kita akan lirik dari sisi kelompok kasus yang saya susun di atas. 
        </p>
        <ol>
        <li>Emiten dengan kategori Pemantauan Khusus didominasi oleh emiten yang tidak aktif diperdagangkan. Namun jika dilihat dari angka absolutnya, emiten yang aktif terbilang cukup banyak yaitu 76 perusahaan dalam pemantauan khusus. Ini seharusnya menjadi WARNING untuk investor jika tidak mau modalnya habis sia-sia.</li>
        <li>Emiten dengan kategori Keuangan juga didominasi oleh yang tidak aktif diperdagangkan. Hanya ada 13 perusahaan di kategori ini. </li>
        <li>Beruntung tidak ada emiten yang distempeli Kategori Hukum. Entah beruntung atau malah kita justru lebih waspada. Semua tegantung penilaian masing-masing pihak. </li>
        <li>Saya tidak akan mebahas kasus Administrasi dan Sanksi pada artike ini.</li>
        </ol>
        <p>Di bawah saya sudah siapkan fitur 3. Fitur untuk explorasi emiten berdasarkan notasi atau kategori kasusnya jika anda penasaran emtien apa saja yang termasuk kategori di atas.
        Karena keterbatasan waktu, Saya cukupkan analisa saya ini. Saya akan sempatkan update database Notasi Khusus bulan April ini. Silahkan explore tools ini, dan semoga bermanfaat.
        </p>
        </div>
        <div style="display: flex; justify-content: center; align-items: center; flex-direction: column;">
        <h1><img src="https://slackmojis.com/emojis/56793-thanks/download" width="30"/> Thanks!</h1>
        <hr style="width: 50%; margin-top: 20px; margin-bottom: 20px;">
        </div>
    """, unsafe_allow_html=True)

    
with st.expander("Fitur 1"):
# Title
    st.write('### Eksplorasi Sektor dengan Notasi Khusus')
    VizNotation.emiten_by_year()

with st.expander("Fitur 2"):
# Title
    st.write('### Eksplorasi Sektor dengan Notasi Khusus')
    VizNotation.emiten_by_year2()

with st.expander("Fitur 3"):
    st.write('### Eksplorasi Detail Perusahaan dengan Notasi Khusus')
    first_filter= st.radio('Pilih berdasarkan:', ['Notasi', 'Kategori Kasus'])
    if first_filter == 'Notasi':
        pilihan_notasi = ['A', 'B', 'D', 'E', 'F', 'I', 'K', 'L', 'M', 'S', 'X']
        arg = st.selectbox('Pilih Notasi:', pilihan_notasi)
        status_perdagangan = st.radio("Pilih Status Perdagangan:", ["Aktif Diperdagangkan", "Semua Emiten"])
        if status_perdagangan == 'Aktif Diperdagangkan':
            if st.button('Tampilkan!'):
                VizNotation.notasi_aktif(arg)
        else:
            if st.button('Tampilkan!'):
                VizNotation.notasi_all(arg)
    else:
        pilihan_kasus = ['Keuangan', 'Administrasi', 'Hukum', 'Sanksi', 'Struktur_Saham', 'Pemantauan_Khusus']
        arg = st.selectbox('Pilih Kategori Kasus:', pilihan_kasus)
        status_perdagangan = st.radio("Pilih Status Perdagangan:", ["Aktif Diperdagangkan", "Semua Emiten"])
        if status_perdagangan == 'Aktif Diperdagangkan':
            if st.button('Tampilkan!'):
                VizNotation.kategori_aktif(arg)
        else:
            if st.button('Tampilkan!'):
                VizNotation.kategori_all(arg)

with st.expander("Fitur 4"):
    st.write('### Eksplorasi Trend Emiten selama Bulan Maret 2024')
    a= df_harian_aktif_NK.copy()
    a['Kode_Emiten'] = a['Kode'] + ' - ' + a['Emiten']
    b= a['Kode_Emiten'].unique()
    kode_dipilih = st.selectbox("Pilih Emiten", b)
    if st.button('Cek Trend!'):
        st.write(f'Berikut adalah trend emiten:')
        st.write(f'{kode_dipilih}bulan Maret')
        st.write('Bulan Maret 2024')
        VizNotation.analisa_trend(kode_dipilih[:4])

# # 2. horizontal menu
# selected2 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
#     icons=['house', 'cloud-upload', "list-task", 'gear'], 
#     menu_icon="cast", default_index=0, orientation="horizontal")
# selected2

# # 3. CSS style definitions
# fitur = option_menu(None, ["Fitur 1", "Fitur 2",  "Fitur 3", 'Fitur 4'], 
#     icons=['1-circle', '1-circle', "1-circle", 'gear'], 
#     menu_icon="cast", default_index=0, orientation="horizontal",
#     styles={
#         "container": {"padding": "0!important", "background-color": "#0000000"},
#         "icon": {"color": "orange", "font-size": "17px"}, 
#         "nav-link": {"font-size": "17px", "text-align": "left", "margin":"0px", "--hover-color": color_codes[3]},
#         "nav-link-selected": {"background-color": color_codes[3]},
#     }
# )

# if st.button('Tampilkan Fitur!'):
#     if fitur== 'Fitur 1':
#         st.write('### Eksplorasi Jumlah Emiten berdasarkan Tahun IPO')
#         notasi = ['A', 'B', 'D', 'E', 'F', 'I', 'K', 'L', 'M', 'S', 'X']
#         # Multi-select untuk memilih opsi
#         selected_options_2 = st.selectbox('Pilihan Notasi:', notasi)
#         VizNotation.emiten_by_year(selected_options_2)

# fitur = option_menu(None, ["Fitur 1", "Fitur 2",  "Fitur 3", 'Fitur 4'], 
#     icons=['1-circle', '1-circle', "1-circle", 'gear'], 
#     menu_icon="cast", default_index=0, orientation="horizontal",
#     styles={
#         "container": {"padding": "0!important", "background-color": "#0000000"},
#         "icon": {"color": "orange", "font-size": "17px"}, 
#         "nav-link": {"font-size": "17px", "text-align": "left", "margin":"0px", "--hover-color": color_codes[3]},
#         "nav-link-selected": {"background-color": color_codes[3]},
#     }
# )

# if st.button('Tampilkan Fitur!'):









# 4. Manual item selection
if st.session_state.get('switch_button', False):
    st.session_state['menu_option'] = (st.session_state.get('menu_option', 1) + 1) % 4
    manual_select = st.session_state['menu_option']
else:
    manual_select = None


# selected4 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
#     icons=['house', 'cloud-upload', "list-task", 'gear'], 
#     orientation="horizontal", manual_select=manual_select, key='menu_4')
# st.button(f"Move to Next {st.session_state.get('menu_option', 1)}", key='switch_button')
# selected4

# # 5. Add on_change callback
# def on_change(key):
#     selection = st.session_state[key]
#     st.write(f"Selection changed to {selection}")
    
# selected5 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'],
#                         icons=['house', 'cloud-upload', "list-task", 'gear'],
#                         on_change=on_change, key='menu_5', orientation="horizontal")
# selected5
    

# st.write(color_codes)