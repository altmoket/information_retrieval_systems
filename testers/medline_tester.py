from sri.searchengine.parser.medline import get_data, get_txt_data, get_qry_data, get_rel, get_rel_numpy
import json

PATH_TO_MED_TXT = "db/med/MED.ALL"
PATH_TO_MED_QRY = "db/med/MED.QRY"
PATH_TO_MED_REL = "db/med/MED.REL"

# txt_list = get_data(PATH_TO_MED_TXT)
# qry_list = get_data(PATH_TO_MED_QRY)
# print(txt_list)
# print(qry_list)

# txt_data = get_txt_data(txt_list)
# # qry_data = get_qry_data(qry_list)
# print(txt_data)
# # print(qry_data)
# with open('medline.json','w') as f:
#     json.dump(txt_data, f, indent=4)
    
med_rel = get_rel(PATH_TO_MED_REL)
med_rel_numpy = get_rel_numpy(PATH_TO_MED_REL)
print(med_rel)
print(med_rel_numpy)
