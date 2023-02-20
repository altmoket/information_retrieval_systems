from sri.parser import cisi
import json

PATH_TO_CISI_TXT = "db/cisi/CISI.ALL"
PATH_TO_CISI_QRY = "db/cisi/CISI.QRY"
PATH_TO_CISI_BLN = "db/cisi/CISI.BLN"
PATH_TO_CISI_REL = "db/cisi/CISI.REL"





txt_list = cisi.get_data(PATH_TO_CISI_TXT)
# qry_list = get_data(PATH_TO_CRAN_QRY)
# print(txt_list)
# print(qry_list)

txt_data = cisi.get_txt_data(txt_list)
# qry_data = get_qry_data(qry_list)
# print(txt_data)
# print(qry_data)
with open('cisi.json','w') as f:
    json.dump(txt_data, f, indent=4)

# cran_rel = get_cran_rel(PATH_TO_CRAN_REL)
# cran_rel_numpy = get_cran_rel_numpy(PATH_TO_CRAN_REL)
# print(cran_rel_numpy)