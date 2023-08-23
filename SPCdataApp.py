import pandas as pd
from xlwings import view
import PyPDF2
import re



sukl_codes = pd.read_csv("../SPC/dlp_lecivepripravky.csv", sep = ";", encoding= "ISO-8859-1", header=0)

sukl_codes.columns.values
sukl_codes.head(1)
sukl_codes.reset_index()
cipher = sukl_codes[['NAZEV', 'KOD_SUKL', "FORMA", "DOPLNEK"]]
cipher.head()

for each in cipher.FORMA.unique():
    print(each)
    

roztoky = ["AUR GTT SOL",
   "AUR GTT SOL MDC",
   "AUR/OPH GTT SOL",
       "DRM PLQ SOL",
       "DRM PLV SOL",
       "DRM PTC SOL",
           "DRM SOL",
       "DRM SPR SOL",
           "GNG SOL",
           "HFL SOL",
   "HFL/HMD/HDF SOL",
       "HMD/HFL SOL",
       "INF CNC SOL",
       "INF PCS SOL",
       "INF PLV SOL",
           "INF SOL",
       "INF SOL APS",
       "INF/POR SOL",
           "INH SOL",
       "INH SOL PSS",
       "INJ CNC SOL",
   "INJ PLQ SOL ISP",
       "INJ PLV SOL",
"INJ PLV SOL/SOL NEB",
       "INJ PSL SOL",
           "INJ SOL",
       "INJ SOL ISP",
       "INJ SOL PEP",
       "INJ SOL PFI",
       "INJ SOL PRO",
       "INJ SOL VIA",
       "INJ SOL ZVL",
"INJ SOL/INF CNC SOL",
   "INJ SOL/SOL NEB",
   "INJ/INF CNC SOL",
   "INJ/INF PLV SOL",
"INF PLV SOL/SOL NEB",
       "INJ/INF SOL",
   "INJ/INF SOL ISP",
"INJ/INF/IVS PLV SOL",
       "IVS PLQ SOL",
           "IVS SOL",
       "NAS GTT SOL",
       "NAS SPR SOL",
   "NAS SPR SOL MDC",
       "OPH GTT SOL",
   "OPH GTT SOL MDC",
"GTT SOL+NAS SPR SOL",
           "ORM SOL",
       "ORM SPR SOL",
       "PLQ SOL NEB",
       "POR CNC SOL",
       "POR GRA SOL",
   "POR GRA SOL SCC",
       "POR GTT SOL",
       "POR PLQ SOL",
       "POR PLV SOL",
   "POR PLV SOL SCC",
           "POR SOL",
       "POR SOL MDC",
   "POR SOL/DRM SOL",
   "POR SOL/INH SOL",
   "POR/ORM/DRM SOL",
       "POR/RCT SOL",
           "PRN SOL",
       "RAD PRE SOL",
           "RCT SOL",
           "SLG SOL",
       "SLG SPR SOL",
           "SOL GKU",
       "SOL MOD SNF",
           "SOL NEB",
       "SOL PRO VLN",
           "TBL SOL",
       "TDR SPR SOL",
       "VAG GRA SOL",
           "VAG SOL"]

roztoky = ["AUR GTT SOL",
   "AUR GTT SOL MDC",
   "AUR/OPH GTT SOL",
    #    "DRM PLQ SOL",
    #    "DRM PLV SOL",
    #    "DRM PTC SOL",
        #    "DRM SOL",
    #    "DRM SPR SOL",
           "GNG SOL",
        #    "HFL SOL",
#    "HFL/HMD/HDF SOL",
    #    "HMD/HFL SOL",
    #    "INF CNC SOL",
    #    "INF PCS SOL",
    #    "INF PLV SOL",
        #    "INF SOL",
    #    "INF SOL APS",
    #    "INF/POR SOL",
        #    "INH SOL",
    #    "INH SOL PSS",
    #    "INJ CNC SOL",
#    "INJ PLQ SOL ISP",
#        "INJ PLV SOL",
# "INJ PLV SOL/SOL NEB",
#        "INJ PSL SOL",
#            "INJ SOL",
#        "INJ SOL ISP",
#        "INJ SOL PEP",
#        "INJ SOL PFI",
#        "INJ SOL PRO",
#        "INJ SOL VIA",
#        "INJ SOL ZVL",
# "INJ SOL/INF CNC SOL",
#    "INJ SOL/SOL NEB",
#    "INJ/INF CNC SOL",
#    "INJ/INF PLV SOL",
# "INF PLV SOL/SOL NEB",
#        "INJ/INF SOL",
#    "INJ/INF SOL ISP",
# "INJ/INF/IVS PLV SOL",
#        "IVS PLQ SOL",
#            "IVS SOL",
       "NAS GTT SOL",
       "NAS SPR SOL",
   "NAS SPR SOL MDC",
       "OPH GTT SOL",
   "OPH GTT SOL MDC",
"GTT SOL+NAS SPR SOL",
           "ORM SOL",
       "ORM SPR SOL",
    #    "PLQ SOL NEB",
       "POR CNC SOL",
       "POR GRA SOL",
#    "POR GRA SOL SCC",
       "POR GTT SOL",
    #    "POR PLQ SOL",
       "POR PLV SOL",
   "POR PLV SOL SCC",
           "POR SOL",
       "POR SOL MDC",
   "POR SOL/DRM SOL",
   "POR SOL/INH SOL",
#    "POR/ORM/DRM SOL",
    #    "POR/RCT SOL",
        #    "PRN SOL",
    #    "RAD PRE SOL",
           "RCT SOL",
           "SLG SOL",
       "SLG SPR SOL",
        #    "SOL GKU",
    #    "SOL MOD SNF",
           "SOL NEB",
    #    "SOL PRO VLN",
        #    "TBL SOL",
    #    "TDR SPR SOL",
       "VAG GRA SOL",
           "VAG SOL"]

preklad = pd.read_csv("./dlp_formy.csv", header = 0, sep = ";", encoding= "ISO-8859-1")[["FORMA", "NAZEV"]].query('FORMA in @roztoky')



with pd.option_context('display.max_rows', None): print(preklad)

selectn = cipher.query('FORMA in @roztoky')

kody = selectn["KOD_SUKL"].values.tolist()
rozhrani = pd.read_csv("./dlp_nazvydokumentu.csv", header = 0, sep = ";", encoding= "ISO-8859-1")[['KOD_SUKL', 'SPC']].query('KOD_SUKL in @kody')


selectn["uchov"] = [""]*len(selectn)
selectn["poo"] = [""]*len(selectn)

for i in range(len(selectn)):
    print(selectn["NAZEV"].iloc[i])
    kod = selectn["KOD_SUKL"].iloc[i]
    nazevpdf = str(rozhrani.query('KOD_SUKL == @kod')["SPC"].values[0])
    if len(nazevpdf) > 3:
        pdfko = f"../SPC/{nazevpdf}"
        # pdfko
        text = ""
        with open(pdfko, "rb") as pdf_file:
            read_pdf = PyPDF2.PdfReader(pdf_file)
            for each in read_pdf.pages:
                text += each.extract_text()
                
        ind1 = text.find("Doba použitelnosti")
        ind2 = text.find("Zvláštní opatření pro uchovávání")
        ind3 = text.find("Druh obalu a velikost balení")

        selectn["poo"].iloc[i] = text[ind1+20:ind2-5].strip().replace(" \n \n", "\n")
        selectn["uchov"].iloc[i] = text[ind2+34:ind3-5].strip().replace(" \n \n", "\n")

selectn.to_csv("./scraped.csv", mode="w+", index=True, header=True, sep = ";")
