import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import stats
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
plt.style.use('./matplotlibrc')

sbins = [0.0375, 0.1, 0.1375, 0.1625, 0.1875, 0.2125, 0.2375, 0.2625, 0.2875, 0.3125, 0.3375, 0.3625, 0.3875, 0.4125, 0.4375, 0.4625, 0.4875, 0.5125, 0.5375, 0.5625, 0.5875, 0.6125, 0.6375, 0.6625, 0.6875, 0.7125, 0.7375, 0.7625, 0.7875, 0.8125, 0.8375, 0.8625, 0.8875, 0.9125, 0.9375, 0.9625, 0.9875, 1.0125, 1.0375, 1.0625, 1.0875, 1.1125, 1.1375, 1.1625, 1.1875, 1.2125, 1.2375, 1.2625, 1.2875, 1.3125, 1.3375, 1.3625, 1.3875, 1.4125, 1.4375, 1.4625, 1.4875, 1.5125, 1.5375, 1.5625, 1.5875, 1.6125, 1.6375, 1.6625, 1.6875, 1.725, 1.775, 1.825, 1.875, 1.925, 1.975, 2.05, 2.15, 2.25, 2.35, 2.5, 2.7, 2.9, 3.0875, 3.3375]
sMinMap = {
    'smin15': 23, 'smin1525': 22, 'smin1550': 21, 'smin1575': 20, 'smin1600': 19,
    'smin1625': 18, 'smin1650': 17, 'smin1675': 16, 'smin1700': 15, 'smin1750': 14,
    'smin1800': 13, 'smin1850': 12, 'smin1900': 11, 'smin1950': 10, 'smin2000': 9,
    'smin2100': 8, 'smin2200': 7, 'smin2300': 6, 'smin2400': 5, 'smin2600': 4, 'smin2800': 3, 'smin3000': 2
}
def addAx(axarr, i, cols, data, title='', ylabel='', xlabel='', ylim=(None, None), exErr=[]):
    axarr[i].set_title(title)
    axarr[i].set_ylabel(ylabel)
    axarr[i].set_xlabel(xlabel)
    if(ylim != (None, None)):
        axarr[i].set_ylim(ylim)
    s0s = list(map(lambda smin: sMinMap[smin], data.index))
    for index, col in enumerate(cols):
        lines, eBars, third = axarr[i].errorbar(
            s0s,
            data[col],
            barsabove=True,
            yerr=None if col in exErr else data[col+'Err'],
            fmt='.',
            marker='o',
            label=r'$\alpha_s(m_\tau)$' if col == 'alpha' else col,
        )
        # if mfcs:
        #     if isinstance(lines, list):
        #         for idx, line  in lines:
        #             line.set_color(mfcs[idx])
        #     else:
        #         lines.set_color(mfcs[0])

    ax_r = axarr[i].twinx()
    ax_r.plot(s0s, data['chiDof'], color='lightgrey', label=r'$\chi^2/dof$')
    ax_r.set_ylabel('test')
    ax_r.grid(False)

    # put axarr[i] in front of ax_r
    axarr[i].set_zorder(ax_r.get_zorder()+1)
    # hide the 'canvas'
    axarr[i].patch.set_visible(False)

    axarr[i].xaxis.set_major_locator(MaxNLocator(integer=True))

    # legend
    axarr[i].legend(loc="lower right")


def read_csv(path, exclude=[]):
    df = pd.read_csv(path, header=1)
    
    df.index = list(sMinMap.keys())[:len(df)]
    if len(exclude) != 0:
        df.drop(exclude, inplace=True)
    # exclude not converged fits
    df = df[df['status']==0]
    return df

def testOPESeriesForConvergence(df, minDiff=1e-1, upToDim=8):
    def compare(x):
        return x < minDiff
    c6c8 = (abs(df['del^(6)']) - abs(df['del^(8)'])).apply(compare)

    if upToDim == 8:
        return c6c8
    if upToDim == 10:
        c8c10 = (abs(df['del^(8)']) - abs(df['del^(10)'])).apply(compare)
        return c6c8 & c8c10
    if upToDim == 12:
        c8c10 = (abs(df['del^(8)']) - abs(df['del^(10)'])).apply(compare)
        c10c12 = (abs(df['del^(10)']) - abs(df['del^(12)'])).apply(compare)
        return c6c8 & c8c10 & c10c12

def getBestRow(df):
    return df.loc[df['chiDof'].idxmin()]
