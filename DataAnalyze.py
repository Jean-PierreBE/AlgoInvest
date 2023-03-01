from prettytable import PrettyTable
import pandas as pd

DATA_FILES = {"File_01": "files_optimized/ActionData1.csv",
              "File_02": "files_optimized/ActionData2.csv"}
DATA_DELIMETER = ","
COL_RESULTS = ["Libelles"]
COL_LINE = ["lignes"]
COL_COL = ["colonnes"]
COL_NULL = ["% cellules non nulles"]
COL_NBACT = ["Nbre d'actions"]
COL_NBACTPOS = ["Nbre d'actions prix > 0"]
COL_NBACTNUL = ["Nbre d'actions prix = 0"]
COL_NBACTNEG = ["Nbre d'actions prix < 0"]
COL_NBPROFPOS = ["Nbre d'actions profit > 0"]
COL_NBPROFNUL = ["Nbre d'actions profit = 0"]
COL_NBPROFNEG = ["Nbre d'actions profit < 0"]

def calc_filled_cells (df):
    nb_not_null = df.notnull().sum().sum()
    percent_not_null = (nb_not_null /(df.shape[1]*df.shape[0])*100)
    return(round(percent_not_null,2))


"""read file"""
for key, value in DATA_FILES.items():
    df_data = pd.read_csv(value, delimiter=DATA_DELIMETER,
                          encoding='unicode_escape')
    COL_RESULTS.append(key)
    COL_LINE.append(df_data.shape[0])
    COL_COL.append(df_data.shape[1])
    COL_NULL.append(str(calc_filled_cells(df_data)) + " %")
    COL_NBACT.append(df_data["name"].drop_duplicates().count())
    COL_NBACTPOS.append(df_data['price'].loc[df_data['price'] > 0].count())
    COL_NBACTNUL.append(df_data['price'].loc[df_data['price'] == 0].count())
    COL_NBACTNEG.append(df_data['price'].loc[df_data['price'] < 0].count())
    COL_NBPROFPOS.append(df_data['profit'].loc[df_data['profit'] > 0].count())
    COL_NBPROFNUL.append(df_data['profit'].loc[df_data['profit'] == 0].count())
    COL_NBPROFNEG.append(df_data['profit'].loc[df_data['profit'] < 0].count())

    print("Le dataframe contient {} lignes et {} colonnes".format(df_data.shape[0],df_data.shape[1]))

    print("Pourcentage de cellules non nulles : " + str(calc_filled_cells(df_data)) + " %")
    print("Nbre d'actions : " + str(df_data["name"].drop_duplicates().count()))

    print("Nbre d'actions prix > 0: " + str(df_data['price'].loc[df_data['price'] > 0].count()))
    print("Nbre d'actions prix = 0: " + str(df_data['price'].loc[df_data['price'] == 0].count()))
    print("Nbre d'actions prix < 0: " + str(df_data['price'].loc[df_data['price'] < 0].count()))

    print("Nbre d'actions profit > 0: " + str(df_data['profit'].loc[df_data['profit'] > 0].count()))
    print("Nbre d'actions profit = 0: " + str(df_data['profit'].loc[df_data['profit'] == 0].count()))
    print("Nbre d'actions profit < 0: " + str(df_data['profit'].loc[df_data['profit'] < 0].count()))


table_result = PrettyTable()
table_result.title = "Résultats par fichier"
table_result.field_names = COL_RESULTS
table_result.add_row([COL_LINE[0],COL_LINE[1],COL_LINE[2]])
table_result.add_row([COL_COL[0],COL_COL[1],COL_COL[2]])
table_result.add_row([COL_NULL[0],COL_NULL[1],COL_NULL[2]])
table_result.add_row([COL_NBACT[0],COL_NBACT[1],COL_NBACT[2]])
table_result.add_row([COL_NBACTPOS[0],COL_NBACTPOS[1],COL_NBACTPOS[2]])
table_result.add_row([COL_NBACTNUL[0],COL_NBACTNUL[1],COL_NBACTNUL[2]])
table_result.add_row([COL_NBACTNEG[0],COL_NBACTNEG[1],COL_NBACTNEG[2]])
table_result.add_row([COL_NBPROFPOS[0],COL_NBPROFPOS[1],COL_NBPROFPOS[2]])
table_result.add_row([COL_NBPROFNUL[0],COL_NBPROFNUL[1],COL_NBPROFNUL[2]])
table_result.add_row([COL_NBPROFNEG[0],COL_NBPROFNEG[1],COL_NBPROFNEG[2]])

print(table_result)