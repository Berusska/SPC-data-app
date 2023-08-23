import pandas as pd

sloupce = "KOD_SUKL;H;NAZEV;SILA;FORMA;BALENI;CESTA;DOPLNEK;OBAL;DRZ;ZEMDRZ;AKT_DRZ;AKT_ZEM;REG;V_PLATDO;NEOMEZ;UVADENIDO;IS_;ATC_WHO;RC;SDOV;SDOV_DOV;SDOV_ZEM;REG_PROC;DDDAMNT_WHO;DDDUN_WHO;DDDP_WHO;ZDROJ_WHO;LL;VYDEJ;ZAV;DOPING;NARVLA;DODAVKY;EAN;BRAILLOVO_PISMO;EXP;EXP_T;NAZEV_REG;MRP_CISLO;PRAVNI_ZAKLAD_REGISTRACE;OCHRANNY_PRVEK".split(";")

sukl_codes = pd.read_csv("./DLP20230731/dlp_lecivepripravky.csv", sep = ";", encoding= "ISO-8859-1", header=0)

sukl_codes.columns.values
sukl_codes.head(1)
sukl_codes.reset_index()
cipher = sukl_codes[['NAZEV', 'KOD_SUKL', "FORMA", "DOPLNEK"]]
len(cipher)