import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import stats
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
plt.style.use('./matplotlibrc')

sminMap = {
    'smin15': 23, 'smin1525': 22, 'smin155': 21, 'smin1575': 20, 'smin16': 19,
    'smin1625': 18, 'smin165': 17, 'smin1675': 16, 'smin17': 15, 'smin175': 14,
    'smin18': 13, 'smin185': 12, 'smin19': 11, 'smin195': 10, 'smin20': 9,
    'smin21': 8, 'smin22': 7, 'smin23': 6, 'smin24': 5, 'smin26': 4, 'smin28': 3
}
def addAx(axarr, i, cols, data, title='', ylabel='', ylim=(None, None), exErr=[]):
    axarr[i].set_title(title)
    axarr[i].set_ylabel(ylabel)
    if(ylim != (None, None)):
        axarr[i].set_ylim(ylim)
    s0s = list(map(lambda smin: sminMap[smin], data.index))
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
    df.index = list(sminMap.keys())[:len(df)]
    if len(exclude) != 0:
        df.drop(exclude, inplace=True)
    # exclude not converged fits
    df = df[df['status']==0]
    return df
