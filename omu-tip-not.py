
# omu not hesaplama v0.1

import tkinter as tk
from tkinter import messagebox

def about():
    messagebox.showinfo(title="Hakkında", message="S.Emre Özer tarafından geliştirilmiş tamamen"+
                        "ücretsiz bir programdır.\nGeliştirilme Tarihi: Nisan 2022\nversiyon: v0.1")
def yardim():
    messagebox.showinfo(title="Yardım", message="boş bıraktıkların \"0\" olarak kabul edilecek ")
    
def hesapla():
    buyumegelisme  = 0
    beyinveduyular = 0
    etik           = 0
    zedelenme      = 0
    kan            = 0
    savunma        = 0
    secmeli        = 0
    biyolojiketmen = 0
    mdunot         = 0
    pdonot         = 0
    gelisim        = 0
    final          = 0
    
    liste = [buyumegelisme, beyinveduyular, etik,
             zedelenme, kan, savunma, secmeli,
             biyolojiketmen, mdunot, pdonot,
             gelisim, final]
    try:
        buyumegelisme  = float(["0" if buyumegelismeNot.get()=="" else buyumegelismeNot.get().replace(",",".")][0])*7
        beyinveduyular = float(["0" if beyinveduyularNot.get()=="" else beyinveduyularNot.get().replace(",",".")][0])*10
        etik           = float(["0" if etikNot.get()=="" else etikNot.get().replace(",",".")][0])*7
        zedelenme      = float(["0" if zedelenmeNot.get()=="" else zedelenmeNot.get().replace(",",".")][0])*5
        kan            = float(["0" if kanNot.get()=="" else kanNot.get().replace(",",".")][0])*7
        savunma        = float(["0" if savunmaNot.get()=="" else savunmaNot.get().replace(",",".")][0])*7
        secmeli        = float(["0" if secmeliNot.get()=="" else secmeliNot.get().replace(",",".")][0])*4
        biyolojiketmen = float(["0" if biyolojiketmenlerNot.get()=="" else biyolojiketmenlerNot.get().replace(",",".")][0])*7
        mdunot         = float(["0" if mduNot.get()=="" else mduNot.get().replace(",",".")][0])*10
        pdonot         = float(["0" if pdoNot.get()=="" else pdoNot.get().replace(",",".")][0])*10
        gelisim        = float(["0" if gelisimNot.get()=="" else gelisimNot.get().replace(",",".")][0])*5
        final          = float(["0" if finalNot.get()=="" else finalNot.get().replace(",",".")][0])
        # final barajı 59.5
        hesap = ((((
            buyumegelisme+
            beyinveduyular+
            etik+
            zedelenme+
            kan+
            savunma+
            secmeli+
            biyolojiketmen
            )/54)*50)+
            mdunot+
            pdonot+
            gelisim+
            final*25)/100
        
        hesap = round(hesap, 2)

        if hesap >= 69.5 and final>=59.5:
        
            sonuc.config(text=str(hesap)+" | Geçtin!")
            barajLabel.config(text="")

        elif hesap >= 69.5 and final<59.5:
            sonuc.config(text=str(hesap)+" | Kaldın :( ")
            barajLabel.config(text="Final barajı 59.5!")
            
        else:

            sonuc.config(text=str(hesap)+" | Kaldın :(")
            barajLabel.config(text="")

       
    except ValueError:     
        messagebox.showerror(title="Hata", message="sadece sayı girin")


# window options
window = tk.Tk()
window.resizable(False, False)
window.title("Omü Tıp 2 Not Hesaplama")
window.geometry("325x500+80+80") # +80+80 program açıldığında ekranın sol üst köşesinden ne kadar uzak olacağını ayarlıyor
# window.overrideredirect(True) # pencerenin sağ üst köşesindeki
                              # küçült, büyült, kapat tuşlarını kaldırıyor ve
                              # pencereyi taşıyabileceğimiz üzt kenarı kaldırıyor

# button = Button(parent, text = 'Click me !!', bg='red', activebackground = 'yellow', height = 5, width = 10)
# butona basıldığında buton rengi değiştirilebilir yukarı satıra bak

# configure the grid
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

label1 = tk.Label(window, text = "Büyüme Gelişme:")
label1.grid(column=0, row=0, sticky=tk.E, padx=5, pady=5)

buyumegelismeNot = tk.Entry(width=5)
buyumegelismeNot.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)

label2 = tk.Label(window, text = "Beyin ve Duyular:")
label2.grid(column=0, row=1, sticky=tk.E, padx=5, pady=5)

beyinveduyularNot = tk.Entry(width=5)
beyinveduyularNot.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)

label3 = tk.Label(window, text = "Etik ve Tıbbi araş.:")
label3.grid(column=0, row=2, sticky=tk.E, padx=5, pady=5)

etikNot = tk.Entry(width=5)
etikNot.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)

label4 = tk.Label(window, text = "zedelenme:")
label4.grid(column=0, row=3, sticky=tk.E, padx=5, pady=5)

zedelenmeNot = tk.Entry(width=5)
zedelenmeNot.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)

label5 = tk.Label(window, text = "kan:")
label5.grid(column=0, row=4, sticky=tk.E, padx=5, pady=5)

kanNot = tk.Entry(width=5)
kanNot.grid(column=1, row=4, sticky=tk.W, padx=5, pady=5)

label6 = tk.Label(window, text="savunma:")
label6.grid(column=0, row=5, sticky=tk.E, padx=5, pady=5)

savunmaNot = tk.Entry(width=5)
savunmaNot.grid(column=1, row=5, sticky=tk.W, padx=5, pady=5)

label7 = tk.Label(window, text="seçmeli:")
label7.grid(column=0, row=6, sticky=tk.E, padx=5, pady=5)

secmeliNot = tk.Entry(width=5)
secmeliNot.grid(column=1, row=6, sticky=tk.W, padx=5, pady=5)

label8 = tk.Label(window, text="biyolojik etmenler:")
label8.grid(column=0, row=7, sticky=tk.E, padx=5, pady=5)

biyolojiketmenlerNot = tk.Entry(width=5)
biyolojiketmenlerNot.grid(column=1, row=7, sticky=tk.W, padx=5, pady=5)

label9 = tk.Label(window, text="mdu notu:")
label9.grid(column=0, row=8, sticky=tk.E, padx=5, pady=5)

mduNot = tk.Entry(width=5)
mduNot.grid(column=1, row=8, sticky=tk.W, padx=5, pady=5)

label10 = tk.Label(window, text="pdo notu:")
label10.grid(column=0, row=9, sticky=tk.E, padx=5, pady=5)

pdoNot = tk.Entry(width=5)
pdoNot.grid(column=1, row=9, sticky=tk.W, padx=5, pady=5)

label11 = tk.Label(window, text="gelişim notu:")
label11.grid(column=0, row=10, sticky=tk.E, padx=5, pady=5)

gelisimNot = tk.Entry(width=5)
gelisimNot.grid(column=1, row=10, sticky=tk.W, padx=5, pady=5)

label12 = tk.Label(window, text="final notu:")
label12.grid(column=0, row=11, sticky=tk.E, padx=5, pady=5)

finalNot = tk.Entry(width=5)
finalNot.grid(column=1, row=11, sticky=tk.W, padx=5, pady=5)


button = tk.Button(window, text="hesapla", command = hesapla)
button.grid(column=1, row=12, padx=5, pady=5)

helpButton = tk.Button(window, text="yardım", command=yardim)
helpButton.grid(column=1, row=13, padx=5, pady=5)

aboutButton = tk.Button(window, text="hakkında", command=about)
aboutButton.grid(column=0, row=12)

sonuc = tk.Label(window, text="")
sonuc.grid(column=0, row=13, sticky=tk.E, padx=5, pady=0)

barajLabel = tk.Label(window, text="")
barajLabel.grid(column=0, row=14, sticky=tk.E)

window.mainloop()

