import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def normalize(df: pd.DataFrame) -> pd.DataFrame:
    ret: pd.DataFrame = df.sort_values(by=['Time'])
    s_max = df['szerokosc'].max()
    s_min = df['szerokosc'].min()
    w_max = df['wysokosc'].max()
    w_min = df['wysokosc'].min()
    print(f's min {s_min}, s max {s_max}, w min {w_min}, w max {w_max}')

    ret['szerokosc'] = ret.apply(lambda x: to_11(s_max, s_min, x['szerokosc']), axis=1)
    ret['wysokosc'] = ret.apply(lambda x: to_11(w_max, w_min, x['wysokosc']), axis=1)

    return ret


def to_11(maxi: float, mini: float, curr: float) -> float:  # covert numbers from data to (-1,1)
    ret: float = (curr-mini)/(maxi-mini)
    return 2*ret-1.


def plotter(df_input: pd.DataFrame):
    img = plt.imread("data/google_map.png")
    fig, ax = plt.subplots()
    plt.ion()
    time_max = int(df_input['Time'].max() / 60)

    for ii in range(time_max+1):
        df = get_data(df_input, ii)
        # x = df[df.columns[1]] # stare slabe
        # y = df[df.columns[2]]
        y = df[df.columns[1]]
        x = df[df.columns[2]]
        s = df[df.columns[3]]

        plt.axis('off')
        plt.ylim(-1, 1)
        plt.xlim(-1, 1)
        ax.set_title(f'Sygnały w czasie na godzinę {6 + int(((17 + ii) - (17 + ii)%60)/60)}:{((17 + ii)%60):02d}')
        ax.imshow(img, extent=[-1, 1, -1, 1])
        ax.scatter(x, y, s, color='firebrick')
        plt.draw()
        plt.pause(0.5)
        if ii != time_max:
            plt.cla()
    plt.pause(100)


def tester(df_input: pd.DataFrame):
    img = plt.imread("data/google_map.png")
    fig, ax = plt.subplots()
    plt.ion()
    time_max = int(df_input['Time'].max() / 60)
    df = df_input[['Time', 'szerokosc', 'wysokosc']]
    y = df[df.columns[1]]
    x = df[df.columns[2]]
    plt.axis('off')
    plt.ylim(-1, 1)
    plt.xlim(-1, 1)
    ax.set_title(f'test mapy')
    ax.imshow(img, extent=[-1, 1, -1, 1])
    ax.scatter(x, y, color='firebrick')
    plt.draw()
    plt.pause(25)
    print('xD')


def get_data(df: pd.DataFrame, dt: int) -> pd.DataFrame:
    ret: pd.DataFrame = df[['Time', 'szerokosc', 'wysokosc']].copy()
    ret[ret.columns[0]] = ret[ret.columns[0]] / 60
    ret[ret.columns[0]] = ret[ret.columns[0]].apply(np.int64)
    ret = ret[(ret['Time'] >= dt - 2) & (ret['Time'] <= dt + 0)]

    #aproksymacja f. kwadratowej tak, ze max dla f(dt)=r^2 oraz f(dt-1)=(r-1)^2
    # r = 8
    # a = 1-2*r
    # b = -2 * a * dt
    # c = r*r - a * dt * dt - b * dt
    # print((r - abs(dt)) * ())
    ret['size'] = (8 - 2*abs(ret['Time'] - dt))**2
    return ret


