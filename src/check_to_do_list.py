import pandas as pd
from datetime import datetime

def check_time_passed(df_to_do_list,status,max_days):
    df_to_do_list = df_to_do_list[df_to_do_list['ESTADO']==status]

    return df_to_do_list[
        (
            (df_to_do_list['ESTADO'].values == status)
            &
            (df_to_do_list['DAYS_PASSED'].values >= max_days)
        )
        ]

def check_to_do_list():
    path = 'G:/Mi unidad/02_trabajo/01_unidad_de_innovacion_hcsc/notas_ui.xlsx'
    df_to_do_list = pd.read_excel(path)

    df_to_do_list['FECHA'] = pd.to_datetime(
        df_to_do_list['FECHA'],
        format='%Y-%m-%d'
        )

    today = datetime.today()

    df_to_do_list['DAYS_PASSED'] = (today - df_to_do_list['FECHA']).dt.days

    list_tasks_to_remind = []
    list_tasks_to_remind.append(check_time_passed(df_to_do_list,status="Iniciado",max_days=7))
    list_tasks_to_remind.append(check_time_passed(df_to_do_list,status="No iniciado",max_days=3))
    list_tasks_to_remind.append(check_time_passed(df_to_do_list,status="Bloqueado",max_days=7))

    return pd.concat(list_tasks_to_remind, axis=0)
