import pandas as pd

def check_to_do_list():
    path = 'G:/Mi unidad/02_trabajo/01_unidad_de_innovacion_hcsc/notas_ui.xlsx'
    df_to_do_list = pd.read_excel(path)

    print(df_to_do_list)
    return pd.DataFrame()
