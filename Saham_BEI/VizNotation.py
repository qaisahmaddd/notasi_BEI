import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import os
import plotly.express as px
import plotly.graph_objects as go

color_codes = ['#5b507a','#ff715b','#b59da4','#219ebc','#ffb703','#6d3d14','#d9bbf9','#aa9fb1']
st.set_option('deprecation.showPyplotGlobalUse', False)

df_all_emiten= pd.read_csv('clean_data/emiten.csv')
df_emiten_NK= pd.read_csv('clean_data/emiten_NK.csv')
df_emiten_NK_actv= pd.read_csv('clean_data/emiten_NK_aktif.csv')
df_harian_aktif_NK= pd.read_csv('clean_data/transaksi_NK.csv')
count_emiten_NK= len(df_emiten_NK)
count_emiten_non_NK= len(df_all_emiten) - count_emiten_NK

def pie1():
    sizes = [count_emiten_NK, count_emiten_non_NK]
    labels = ['Dengan Notasi', 'Tanpa Notasi']
    data = {'Emiten': labels, 'Jumlah': sizes}
    df = pd.DataFrame(data)

    fig = px.pie(df, values='Jumlah', names='Emiten',
                 color_discrete_sequence=[color_codes[2], color_codes[3]],  # Menggunakan warna dari list color_codes
                 hover_data={'Jumlah': ':.0f'},
                 labels={'Jumlah': 'Jumlah Emiten'})

    # Atur legenda menjadi di tengah bawah dalam satu baris
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.2,
        xanchor="center",
        x=0.5
    ))

    # Atur ukuran plot menjadi 500px x 500px
    st.write('<style>div.Widget.row-widget.stRadio div[role="radiogroup"] div:nth-child(2) label{flex: 0 1 auto !important;}</style>', unsafe_allow_html=True)
    st.plotly_chart(fig, use_container_width=True)

def total_emiten():
    notasi = sorted(list(df_emiten_NK.columns[6:17]))
    NK_all = [df_emiten_NK[col].sum() for col in df_emiten_NK.columns[6:17]]
    NK_aktif = [df_emiten_NK_actv[col].sum() for col in df_emiten_NK_actv.columns[8:19]]

    # Membuat DataFrame
    df_compare_NK = pd.DataFrame({
        'Notasi': notasi,
        'NK All': NK_all,
        'NK Aktif': NK_aktif
    })
    df_compare_NK.set_index('Notasi', inplace=True)

    # Menghitung kolom "Tidak Aktif"
    df_compare_NK['Tidak Aktif'] = df_compare_NK['NK All'] - df_compare_NK['NK Aktif']
    df_compare_NK['Tidak Aktif'] = df_compare_NK['NK All'] - df_compare_NK['NK Aktif']
    # Menghitung persentase
    df_compare_NK_prcnt = df_compare_NK[['NK Aktif', 'Tidak Aktif']].div(df_compare_NK['NK All'], axis=0)
    df_compare_NK_prcnt = df_compare_NK_prcnt.round(2)
    df_compare_NK= df_compare_NK.iloc[:, 1:]
    df_compare_NK= df_compare_NK.sort_values(by='NK Aktif')
    df_compare_NK_prcnt= df_compare_NK_prcnt.sort_values(by='NK Aktif')

    # Menampilkan plot
    fig, ax = plt.subplots(figsize=(10, 6))  # Create figure and axis
    df_compare_NK_prcnt.plot(kind='barh', stacked=True, color=[color_codes[3], color_codes[4]], ax=ax)

    # Menampilkan label pada plot
    plt.legend(loc='lower center', bbox_to_anchor=(0, 1))
    plt.xlabel('Perbandingan Emiten')
    plt.ylabel('Notasi')
    plt.title('Berdasarkan Huruf Notasinya')
    plt.xticks([])
    plt.xticks(rotation=0)

    # Menampilkan label pada bar plot
    for n, x in enumerate([*df_compare_NK_prcnt.index.values]):
        for (proportion, count, y_loc) in zip(df_compare_NK_prcnt.loc[x],
                                            df_compare_NK.loc[x],
                                            df_compare_NK_prcnt.loc[x].cumsum()):
            
            plt.text(x=(y_loc - proportion) + (proportion / 2),
                    y=n - 0.11,
                    s=f'{count} ({np.round(proportion * 100, 1)}%)', 
                    color="black",
                    fontsize=8,
                    fontweight="bold")
    st.pyplot(fig)   
    
def total_emiten_1():
    temp_dict= {
        'Kasus': [],
        'Emiten Aktif': [],
        'Emiten Tidak Aktif': [],
        'Emiten Keseluruhan': []
    }
    cols= df_emiten_NK.columns[18:24].to_list()
    for col in cols:
        a= len(df_emiten_NK_actv[df_emiten_NK_actv[col]== 'Ya'])
        c= len(df_emiten_NK[df_emiten_NK[col]== 'Ya'])
        b= c - a
        col= col.replace("_", " ")
        temp_dict['Kasus'].append(col)
        temp_dict['Emiten Aktif'].append(a)
        temp_dict['Emiten Tidak Aktif'].append(b)
        temp_dict['Emiten Keseluruhan'].append(c)
    temp_df= pd.DataFrame(temp_dict).set_index('Kasus')
    temp_df= temp_df[temp_df['Emiten Keseluruhan']>0]
    temp_df_prcnt= round(temp_df[['Emiten Aktif', 'Emiten Tidak Aktif']].div(temp_df['Emiten Keseluruhan'], axis=0), 2)
    temp_df_prcnt= temp_df_prcnt.fillna(0)
    temp_df_prcnt= temp_df_prcnt.iloc[:, :2]
    temp_df= temp_df.iloc[:, :2]
    print(temp_df)

    fig, ax = plt.subplots(figsize=(10, 6))  # Create figure and axis
    temp_df_prcnt.plot(kind='barh', stacked=True, color=[color_codes[3], color_codes[4]], ax=ax)

    plt.legend(loc='lower center', bbox_to_anchor=(-0.1, 1))
    plt.xlabel('Perbandingan Emiten')
    plt.ylabel('Kasus')
    plt.title('Berdasarkan Kategori Kasus')
    plt.xticks([])
    plt.xticks(rotation=0)

    for n, x in enumerate([*temp_df.index.values]):
        for (proportion, count, y_loc) in zip(temp_df_prcnt.loc[x],
                                            temp_df.loc[x],
                                            temp_df_prcnt.loc[x].cumsum()):
            
            plt.text(x=(y_loc - proportion) + (proportion / 2),
                    y=n - 0.11,
                    s=f'{count} ({np.round(proportion * 100, 1)}%)', 
                    color="black",
                    fontsize=8,
                    fontweight="bold")
    # Return the figure
    st.pyplot(fig)

def emiten_by_year(notasi):
    st.write(f"<h3 style='text-align: center;'>Jumlah Notasi ( {notasi} ) Berdasarkan Tahun IPO</h3>", unsafe_allow_html=True)
    temp_df = df_emiten_NK.groupby('Tahun_IPO')['Total_Notasi'].sum().reset_index()

    # Memfilter data
    temp_df = temp_df[temp_df['Tahun_IPO'].notna()]

    total = df_emiten_NK.groupby('Tahun_IPO')[notasi].sum().reset_index()

    # Membuat plot menggunakan Plotly
    fig = go.Figure()

    # Tambahkan trace untuk Total Notasi
    fig.add_trace(go.Bar(
        x=temp_df['Tahun_IPO'],
        y=temp_df['Total_Notasi'],
        name='Total Notasi',
        marker_color=color_codes[3],
        hovertemplate='<b>Tahun IPO</b>:%{x}<br><b>%{y} <b>Emiten</b>',
    ))

    # Tambahkan trace untuk Total Notasi spesifik (notasi yang dipilih)
    fig.add_trace(go.Scatter(
        x=total['Tahun_IPO'],
        y=total[notasi],
        mode='lines+markers',
        name=f'Total Notasi {notasi}',
        marker=dict(color=color_codes[4], size=8),
        line=dict(color=color_codes[4], width=3),
        hovertemplate='<b>Tahun IPO</b>:%{x}<br><b>%{y} <b>Emiten</b>',
        stackgroup=True
    ))

    # Atur layout grafik
    fig.update_layout(
        xaxis=dict(title='Tahun IPO', tickmode='linear', tickvals=temp_df['Tahun_IPO'], tickangle=90),
        yaxis=dict(title='Jumlah Notasi Keseluruhan'),
        legend=dict(x=0, y=1.0, bgcolor='rgba(255, 255, 255, 0)', bordercolor='rgba(255, 255, 255, 0)'),
        plot_bgcolor='rgba(0, 0, 0, 0)',
        width=670
    )

    # Menampilkan grafik di Streamlit
    st.plotly_chart(fig)


def emiten_by_year2():
    year= sorted(df_emiten_NK['Tahun_IPO'].unique(), reverse=True)
    tahun_dipilih = st.selectbox("Pilih Tahun IPO", year)
    temp_df2 = df_emiten_NK[df_emiten_NK['Tahun_IPO']== tahun_dipilih]
    temp_df2 = temp_df2.groupby('Sektor')['Total_Notasi'].sum().reset_index()
    if st.button('Cek Tahun ini!'):
        st.write(f"<h3 style='text-align: center;'>Emiten Notasi Khusus Tahun IPO {tahun_dipilih}</h3>", unsafe_allow_html=True)
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=temp_df2['Sektor'],
            y=temp_df2['Total_Notasi'],
            name='Total Notasi',
                marker_color=color_codes[3]
        ))
        # Menampilkan grafik di Streamlit
        st.plotly_chart(fig)


def pilih_emiten(kode):
    a= df_harian_aktif_NK[df_harian_aktif_NK['Kode']== kode]
    b= a['Nilai'].sum()/1000000000 #Total_Nilai_Transaksi_Milyar
    c= a['Volume'].sum()/1000000
    d= a['Foreign_Sell'].sum()/1000000
    e= a['Foreign_Buy'].sum()/1000000
    a1= a/18 
    b1= b/18 
    c1= c/18 
    d1= d/18
    temp_dict= {
        'Keterangan': ['Transaksi', 'Volume', 'Foreign_Sell', 'Foreign_Buys'],
        'Total': [a, b, c, d],
        'Rata-Rata': [a1, b1, c1, d1]
    }
    temp_df= pd.DataFrame(temp_dict)

def kategori_aktif(kasus):
    a= df_emiten_NK_actv[df_emiten_NK_actv[kasus] == 'Ya'].reset_index(drop=True)
    a.index= a.index+1
    a= a[['Kode', 'Emiten', 'Sektor', 'Tahun_IPO', 'Papan_Pencatatan']]
    if len(a) > 0:
        st.write(f'Ditemukan sebanyak: {len(a)} Emiten (Perusahaan)')
        st.write('Berikut adalah tabel emitennya:')
        st.write(a)
    else:
        st.write(f'Emiten yang aktif diperdagangkan tidak ditemukan pada Kategori Kasus {kasus}')
def kategori_all(kasus):
    a= df_emiten_NK[df_emiten_NK[kasus] == 'Ya'].reset_index(drop=True)
    a.index= a.index+1
    a= a[['Kode', 'Emiten', 'Sektor', 'Tahun_IPO', 'Papan_Pencatatan']]
    if len(a) > 0:
        st.write(f'Ditemukan sebanyak: {len(a)} Emiten (Perusahaan)')
        st.write('Berikut adalah tabel emitennya:')

        st.write(a)
    else:
        st.write(f'Emiten tidak ditemukan pada Kategori Kasus {kasus}')
def notasi_aktif(notasi):
    a= df_emiten_NK_actv[df_emiten_NK_actv[notasi] == 1].reset_index(drop=True)
    a.index= a.index+1
    a= a[['Kode', 'Emiten', 'Sektor', 'Tahun_IPO', 'Papan_Pencatatan']]
    if len(a) > 0:
        st.write(f'Ditemukan sebanyak: {len(a)} Emiten (Perusahaan)')
        st.write('Berikut adalah tabel emitennya:')
        st.write(a)
    else:
        st.write(f'Emiten yang aktif diperdagangkan tidak ditemukan pada Notasi {notasi}')
def notasi_all(notasi):
    a= df_emiten_NK[df_emiten_NK[notasi] == 1].reset_index(drop=True)
    a.index= a.index+1
    a= a[['Kode', 'Emiten', 'Sektor', 'Tahun_IPO', 'Papan_Pencatatan']]
    if len(a) > 0:
        st.write(f'Ditemukan sebanyak: {len(a)} Emiten (Perusahaan)')
        st.write('Berikut adalah tabel emitennya:')
        st.write(a)
    else:
        st.write(f'Emiten tidak ditemukan pada Notasi {notasi}')

def analisa_trend(kode):
    emiten = df_harian_aktif_NK[df_harian_aktif_NK['Kode'] == kode]
    emiten= emiten.rename(columns={
        'Penutupan': 'Harga Saham',
        'Volume': 'Total Volume Transaksi',
        'Nilai': 'Total Nilai Transaksi'
    })

    a = emiten['Tanggal'].unique()
    cols = ['Harga Saham', 'Total Nilai Transaksi', 'Total Volume Transaksi']
    
    for i, col in enumerate(cols):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=a, y=emiten[col], mode='lines', name=col, line=dict(color=color_codes[i+1])))
        fig.update_layout(title=f'Chart Harian {col} {kode}',
                          xaxis_title='Tanggal',
                          yaxis_title=col,
                          hovermode='x',
                          template='plotly_dark')
        st.plotly_chart(fig)
