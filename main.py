import pandas as pd
import loader
from analysis import normalize, plotter, tester

if __name__ == '__main__':
    wifi_database_path = 'data/querry'
    df_wifi = loader.wifi_df(wifi_database_path)

    wireshark_path = 'data/wireshark_data.csv'
    df_wireshark: pd.DataFrame = loader.wireshark_df(wireshark_path)
    df_wireshark = pd.merge(df_wireshark, df_wifi, how='inner', right_index=True, left_index=True)

    df_wireshark = normalize(df_wireshark)
    # tester(df_wireshark)
    plotter(df_wireshark)

