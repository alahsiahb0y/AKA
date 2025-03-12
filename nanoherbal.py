import numpy as np
import streamlit as st
import base64
import pandas as pd
import altair as alt

st.set_page_config(page_title="NanoHerbal", page_icon="🌿")

if "page" not in st.session_state:
    st.session_state.page = "home"

def navigate_to(page_name):
    st.session_state.page = page_name

st.markdown(
    f"""
    <style>
    .background {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: #FF8F00CC; //alternative #FF8F00CC
        z-index: 0; /* Letakkan di belakang konten lainnya */
    }}
    </style>
    <div class="background"></div>
    """,
    unsafe_allow_html=True
)

def set_background():
    page_bg = f'''
    <style>
        .stApp {{
            background: url('https://media-exp1.licdn.com/dms/image/C561BAQF6MpHgMOgscg/company-background_10000/0/1614409458530?e=2147483647&v=beta&t=Qe02VpPEKqQwFYJm5LoQF8oOmyh8PRbNI0brFg9l5sg') no-repeat center center fixed;
            background-size: cover;
        }}

        .container {{
            position: relative;
            z-index: 0;
            text-align: center;
        }}
    </style>
    <div class="overlay"></div>
    '''
    st.markdown(page_bg, unsafe_allow_html=True)

set_background()

with st.container():
    col1, col2 = st.columns([14, 2])  # Membagi halaman menjadi dua kolom (5:1)

    with col1:
        # Teks di kiri
        st.write("""
        <div style="font-family: 'Minion Pro', monospaces monospace; margin-top: -20px; text-align: right;">
            <p style="font-weight: bold; margin: 0px; font-size: 24px; line-height: 1;">Politeknik AKA Bogor</p>
            <p style="margin: 0px; font-size: 22px; line-height: 1; margin-top: 10px; color: #ffff; ">D-IV Nanoteknologi Pangan</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        # Fungsi untuk mengonversi gambar menjadi base64
        def image_to_base64(image_path):
            with open(image_path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode("utf-8")

        # Konversi gambar lokal
        image_base64 = image_to_base64("aka1.png")

        # Gunakan base64 di dalam HTML
        st.markdown(
            f"""
            <div style="text-align: right; margin-top: -35px;">
                <img src="data:image/png;base64,{image_base64}"
                    alt="Logo Politeknik AKA Bogor" style="width: 500px !important; height: auto">
            </div>
            """,
            unsafe_allow_html=True,
        )

image_url = "https://indonesiacollege.co.id/blog/wp-content/uploads/2022/10/jurusan-politeknik-aka-bogor.jpg"

st.markdown(
    """
    <style>
                                    /*Button sebelum hover*/
    .stButton > button {
        background-color: transparent !important; /* Warna latar belakang default */
        color: #ffffff !important;             /* Warna teks default */
        border: 2px #FFFF solid;
        font-weight: bold ;
        font-size: 10px ;
        cursor: pointer;
        height: 60px ;
        padding: 20px ;
        transition: background-color 0.2s, color 0.2s; /* Efek transisi */
    }

                                    /* Gaya tombol saat hover */
    .stButton > button:hover {
        background-color: #ffffff !important;  /* Warna latar belakang saat hover */
        color: #FF8F00 !important;          /* Warna teks saat hover */
        border: 3px solid #FF8F00 !important;
        height: 60px !important;
        }
    """, unsafe_allow_html=True)

def Home():
    st.markdown("<h1 style='text-align: center; font-family: times new roman;'><br><br>Lets Get Started<br></h1>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("% Rendemen", use_container_width=True):
            navigate_to("rendemen")

    with col2:
        if st.button("Kadar Air", use_container_width=True):
            navigate_to("kadarair")
    
    with col3:
        if st.button("Kadar Abu", use_container_width=True):
            navigate_to("kadarabu")

    with col4:
        if st.button("Total Fenolik", use_container_width=True):
            navigate_to("totalfenol")


st.markdown("""
    <style>
        /* Mengubah warna latar belakang input box saja */
        div[data-testid="stNumberInput"] input, 
        div[data-testid="stTextInput"] input {
            background-color: #FFB347 !important;
            color: black !important;
            border: transparent !important; /* Menghilangkan border hitam */
            border-radius: 5px; /* Membuat sudut lebih halus */
            padding: 10px;
        }

        /* Menghilangkan border hitam tombol +/- tanpa mengubah warna */
        div[data-testid="stNumberInput"] button {
            background: #FFB347 !important;
            border: none !important;
        }
    </style>
""", unsafe_allow_html=True)

def rendemenn():
    st.markdown("<h1 style='text-align: center; font-family: times new roman;'><br>% Rendemen<br></h1>", unsafe_allow_html=True)    
    nardm = st.text_input("Nama sampel ekstrak (gram)")
    ckrdm = st.number_input("Massa cawan kosong (gram)")
    mardm = st.number_input("Massa awal sebelum esktraksi (gram)")
    makrdm = st.number_input("Massa akhir setelah ekstraksi")

    if mardm > 0:
        rsltrdm = (makrdm-ckrdm)*100/mardm

    else:
        st.warning("Pastikan massa awal sebelum ekstraksi telah terisi dengan nilai > 0")
        rsltrdm = None


    if st.button("Hitung %Rendemen", use_container_width=True):
        if ckrdm <= makrdm <= ckrdm + mardm and rsltrdm is not None:
            st.markdown(f"""
                <div style="
                    background-color: #FB4F14;
                    padding: 15px;
                    border: 2px #FFFF solid;
                    border-radius: 10px;
                    text-align: center;">
                    <h1 style="text-align: center; font-family: 'Times New Roman', Times, serif; font-size: 30px;">
                        %Rendemen {nardm} sebesar {rsltrdm:.2f} %
                    </h1>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.error("Pastikan data yang anda input telah benar !")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Back", use_container_width=True):
        navigate_to("home")


def kadar_air():
    st.markdown("<h1 style='text-align: center; font-family: times new roman;'><br>Kadar Air<br></h1>", unsafe_allow_html=True)

    matname = st.text_input("Masukkan Nama Bahan")
    mc = st.number_input("Massa Cawan Kosong (gram)", format="%.4f")
    befheat = st.number_input("Massa Bahan (gram)", format="%.4f")
    aftheat = st.number_input("Massa Keseluruhan Setelah Pemanasan (gram)", format="%.4f")

    if st.button("Hitung Kadar Air", use_container_width=True):
        if mc <= aftheat <= mc + befheat and befheat > 0:
            rslt_kadarair = (mc+befheat-aftheat)*100/befheat
            st.markdown(f"""
                <div style="
                    background-color: #FB4F14;
                    padding: 15px;
                    border: 2px #FFFF solid;
                    border-radius: 10px;
                    text-align: center;">
                    <h1 style="text-align: center; font-family: 'Times New Roman', Times, serif; font-size: 30px;">
                        Kadar air {matname} sebesar {rslt_kadarair:.2f} %
                    </h1>
                </div>
            """, unsafe_allow_html=True)

    else:
        st.error("Pastikan data yang anda input telah benar !")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Back", use_container_width=True):
        navigate_to("home")

def kadar_abu():
    st.markdown("<h1 style='text-align: center; font-family: times new roman;'><br>Kadar Abu<br></h1>", unsafe_allow_html=True)
    
    mattname = st.text_input("Masukkan Nama Bahan")
    cakos = st.number_input("Massa Cawan Kosong (gram)", format="%.4f")
    matbef = st.number_input("Massa Bahan (gram)", format="%.4f")
    mataft = st.number_input("Massa Keseluruhan Setelah Pemanasan (gram)", format="%.4f")

    if st.button("Hitung Kadar Abu", use_container_width=True):
        if cakos <= mataft <= cakos + matbef:
            rslt_kadarabu = (mataft-cakos)*100/matbef
            st.markdown(f"""
                <div style="
                    background-color: #FB4F14;
                    padding: 15px;
                    border: 2px #FFFF solid;
                    border-radius: 10px;
                    text-align: center;">
                    <h1 style="text-align: center; font-family: 'Times New Roman', Times, serif; font-size: 30px;">
                        Kadar abu {mattname} sebesar {rslt_kadarabu:.2f} %
                    </h1>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.error("Pastikan data yang anda input telah benar !")
    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("Back", use_container_width=True):
        navigate_to("home")

def total_fenol():

    st.markdown("<h1 style='text-align: center; font-family: times new roman;'><br>Total Fenolik<br></h1>", unsafe_allow_html=True)

    namspl = st.text_input("Masukkan Nama Sampel")
    st.markdown("<br>", unsafe_allow_html=True)
    st.header("`Larutan Induk Asam Galat`")
    gasg = st.number_input("Massa Asam Galat (gram)", format="%.4f")
    vltasg = st.number_input("Volumer Labu Takar (mL)", format="%.0f")

    if vltasg == 0:
        st.error("Volume pengenceran tidak bisa 0 !!!")
        ppmasg = None
    else:
        mgasg = gasg*1000
        ppmasg = mgasg*1000/vltasg
    
    if st.checkbox("Lihat Konsentrasi Asam Galat (ppm)"):
        if ppmasg is not None:
            st.success(f"Asam galat {ppmasg:.4f} ppm sebagai C1")

    st.header("`Deret Standar`")

    # Misal, ppmasg sudah didefinisikan (contoh saja)
    ppmasg = 50.0

    jml = int(st.number_input("Masukkan Jumlah Deret", format="%.0f"))
    if jml > 2:
        st.write("Masukkan data untuk setiap sampel:")

        # Buat 4 kolom untuk input
        cols = st.columns(4)

        # List untuk menyimpan nilai input
        pipetvol_list = []
        ltvol_list = []
        absr_list = []
        concrslt_list = []

        for i in range(jml):
            with cols[0]:
                pipetvol = st.number_input(f"Volume Pipet ({i+1}) (mL)", format="%.2f", key=f"pipet_{i}")
            with cols[1]:
                ltvol = st.number_input(f"Volume Labu Takar ({i+1}) (mL)", format="%.2f", key=f"labu_{i}")
            with cols[2]:
                if ltvol > 0:
                    concrslt = ppmasg * pipetvol / ltvol
                    st.markdown("")
                    st.success(f"{concrslt:.2f} ppm")
                else:
                    concrslt = 0  # Jika ltvol <= 0, beri nilai default agar tidak None
                    st.markdown("")
            with cols[3]:
                absr = st.number_input(f"Absorbansi Deret ke-{i+1}", format="%.4f", key=f"abs_{i}")
            
            # Simpan ke list
            pipetvol_list.append(pipetvol)
            ltvol_list.append(ltvol)
            absr_list.append(absr)
            concrslt_list.append(concrslt)

        # Satu checkbox untuk memeriksa kesalahan input
        if st.checkbox("Lihat Kesalahan"):
            any_error = False
            for i in range(jml):
                if ltvol_list[i] <= 0:
                    st.error(f"Volume Labu Takar deret ke-{i+1} Tidak Boleh 0 !!!")
                    any_error = True
            if not any_error:
                st.success("Tidak ada kesalahan input!")



        # Konversi ke dictionary dan DataFrame
        datum = {
            "Konsentrasi Asam Galat (ppm)": concrslt_list,  # Sumbu X
            "Absorbansi": absr_list  # Sumbu Y
        }
        dataa = pd.DataFrame(datum)

        # Tampilkan DataFrame data input

        st.dataframe(dataa, use_container_width=True)

        if st.button("Hitung Regresi Deret", use_container_width=True):

            # Pastikan ada setidaknya 2 data untuk regresi
            if len(dataa) < 2:
                st.error("Data tidak cukup untuk analisis regresi!")
            else:
                # Hitung parameter regresi menggunakan NumPy
                x = dataa["Konsentrasi Asam Galat (ppm)"].values
                y = dataa["Absorbansi"].values
                slope, intersep = np.polyfit(x, y, 1)  # y = a*x + b
                
                # Hitung nilai prediksi dan koefisien determinasi (R²)
                y_pred = slope * x + intersep
                ss_res = np.sum((y - y_pred) ** 2)
                ss_tot = np.sum((y - np.mean(y)) ** 2)
                r2 = 1 - ss_res / ss_tot

                eq_text = f"y = {slope:.4f} x {'+' if intersep >= 0 else '-'} {abs(intersep):.4f}"

                determm = f"R² = {r2:.4f}"

                # Buat grafik dengan garis regresi dan titik data
                base = alt.Chart(dataa).encode(
                    x=alt.X("Konsentrasi Asam Galat (ppm):Q", title="Konsentrasi Asam Galat (ppm)"),
                    y=alt.Y("Absorbansi:Q", title="Absorbansi")
                )
                
                # Garis regresi menggunakan transform_regression (untuk visualisasi)
                regression_line = base.transform_regression(
                    "Konsentrasi Asam Galat (ppm)", "Absorbansi", method="linear"
                ).mark_line(color="green")
                
                # Titik data asli
                points = base.mark_point()

                # Buat DataFrame untuk anotasi teks
                # Posisi teks: misalnya di pojok kiri atas grafik
                annotation_df = pd.DataFrame({
                    "x": [dataa["Konsentrasi Asam Galat (ppm)"].min()],
                    "y": [dataa["Absorbansi"].max()],
                    "text": [eq_text]
                })

                # Buat anotasi teks menggunakan mark_text
                text_annotation = alt.Chart(annotation_df).mark_text(
                    align='left',
                    baseline='top',
                    dx=5,
                    dy=5,
                    fontSize=12,
                    color='black'
                ).encode(
                    x='x:Q',
                    y='y:Q',
                    text='text:N'
                )

                # Gabungkan grafik titik, garis regresi, dan anotasi teks
                chart = regression_line + points + text_annotation

                st.altair_chart(chart, use_container_width=True)
    
                st.write(
                    f"""
                    <div style="text-align: center; font-size: 50px;">
                        <code>{eq_text}</code>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )

                st.write(
                    f"""
                    <div style="text-align: center; font-size: 50px;">
                        <code>
                            {determm}
                        </code>
                    </div>
                    """,
                    unsafe_allow_html=True
                )    
    
    else:
        st.error("Jumlah deret standard harus lebih dari 2")

    st.header(f"`Penetapan Total Fenol Sampel {namspl}`")
    col1, col2 = st.columns(2)
    with col1:
        pipetspl = st.number_input("Volume sampel yang dipipet (mL)")
    with col2:
        vollt = st.number_input("Volume labu takar (mL)")
    
    if pipetspl <= 0:
        st.error("Nilai volume sampel yang dipipet tidak boleh 0")
        fakpen = None
    else:
        fakpen = vollt/pipetspl
        
    

    spl = int(st.number_input("Masukkan Jumlah Sampel", format="%.0f"))
    
    cterukur_list = []
    ke_list = []
    ctkalifp_list = []
    fenoltot_list = []

    for i in range(spl):
        # Hitung parameter regresi menggunakan NumPy
        x = dataa["Konsentrasi Asam Galat (ppm)"].values
        y = dataa["Absorbansi"].values
        slope, intersep = np.polyfit(x, y, 1)  # y = a*x + b        

        ke = i+1
        absspl = st.number_input(f"Absorbansi Sampel {namspl} ({ke})", format="%.4f", key=f"absorbansii_{i}")
        cterukur = (absspl-intersep)/slope
        ctkalifp = cterukur*fakpen
        fenoltot = (ctkalifp/1000)/vollt

        cterukur_list.append(cterukur)
        ke_list.append(ke)
        ctkalifp_list.append(ctkalifp)
        fenoltot_list.append(fenoltot)

    if fenoltot_list:
        meanfentot = np.mean(fenoltot_list)
    else:
        st.error("Input data pada box yang tersedia !!!")
        meanfentot = None

    if st.button(f"Hitung total fenol sampel {namspl}", use_container_width=True):
        if jml > 2:
            datac = {
                "Sampel ke -": ke_list,  # Sumbu X
                "C terukur (ppm)": cterukur_list,  # Sumbu Y
                "Konsentrasi Larutan (ppm)": ctkalifp_list,
                "Total Fenol (mg.GAE/g)": fenoltot_list
            }
            dataac = pd.DataFrame(datac).round(
                {
                "C terukur (ppm)": 4,  # Sumbu Y
                "Konsentrasi Larutan (ppm)": 4,
                "Total Fenol (mg.GAE/g)": 4
                }
            )

            # Tampilkan DataFrame data input
            st.dataframe(dataac, use_container_width=True)
            if meanfentot is not None:
                st.markdown(f"""
                    <div style="
                        background-color: #FB4F14;
                        padding: 15px;
                        border: 2px #FFFF solid;
                        border-radius: 10px;
                        text-align: center;">
                        <h1 style="text-align: center; font-family: 'Times New Roman', Times, serif; font-size: 20px;">
                            Rata-rata total fenol sampel {namspl} sebesar {meanfentot:.4f} mg.GAE/g
                        </h1>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.error("Input data deret terlebih dahulu")
        st.markdown("<br>", unsafe_allow_html=True)

    if st.button("Back", use_container_width=True):
        navigate_to("home")















if st.session_state.page == "home":
    Home()

elif st.session_state.page == "rendemen":
    rendemenn()

elif st.session_state.page == "kadarabu":
    kadar_abu()

elif st.session_state.page == "kadarair":
    kadar_air()

elif st.session_state.page == "totalfenol":
    total_fenol()