from sri.parser.cranfield import get_data, get_txt_data,\
                                get_qry_data, get_cran_rel, get_cran_rel_numpy
import json
PATH_TO_CRAN_TXT = "db/cran/cran.all.1400"
PATH_TO_CRAN_QRY = "db/cran/cran.qry"
PATH_TO_CRAN_REL = "db/cran/cranqrel"

txt_list = get_data(PATH_TO_CRAN_TXT)
# qry_list = get_data(PATH_TO_CRAN_QRY)
# print(txt_list)
# print(qry_list)

txt_data = get_txt_data(txt_list)
# qry_data = get_qry_data(qry_list)
print(txt_data)
# print(qry_data)
with open('cranfield.json','w') as f:
    json.dump(txt_data, f, indent=4)

# cran_rel = get_cran_rel(PATH_TO_CRAN_REL)
# cran_rel_numpy = get_cran_rel_numpy(PATH_TO_CRAN_REL)
# print(cran_rel_numpy)