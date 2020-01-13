import pandas as pd
import json
from pandas.io.json import json_normalize


def wifi_df(wifi_database_path: str) -> pd.DataFrame:
    with open(wifi_database_path, encoding="utf8") as data_file:
        data = json.load(data_file)

    df_wifi: pd.DataFrame = json_normalize(data, 'results',
                                           ['success', 'totalResults', 'first', 'last', 'search_after',
                                            'searchAfter'], )
    df_wifi = df_wifi[['trilat', 'trilong', 'ssid', 'housenumber', 'road']]
    df_wifi = df_wifi.rename(columns={'trilat': 'szerokosc', 'trilong': 'wysokosc', 'ssid': 'SSID'})
    df_wifi = df_wifi.set_index('SSID')
    return df_wifi


def wireshark_df(wireshark_path: str) -> pd.DataFrame:
    df_wireshark: pd.DataFrame = pd.read_csv(wireshark_path)
    df_wireshark["Info"] = df_wireshark.apply(lambda x: to_ssid(x["Info"]), axis=1)
    df_wireshark['Time'] = df_wireshark.apply(lambda x: int(x['Time']), axis=1)
    df_wireshark = df_wireshark.rename(columns={'Info': 'SSID'})
    df_wireshark = df_wireshark[['Time', 'SSID']]
    df_wireshark = df_wireshark.set_index('SSID')
    return df_wireshark


def to_ssid(x):
    ret = x.split(",")[-1][6:]
    return ret


def street(df, road_name):
    ret = df.loc[df['_road'] == road_name]
    return ret
