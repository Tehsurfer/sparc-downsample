import os
import sys
import platform
import progressbar
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from scipy import signal
import json
import numpy as np




def run():
    max_lines = 100000
    resample_factors = [10]
    file_name = sys.argv[1]
    if len(sys.argv) == 3:
        resample_factors[0] = int(sys.argv[2])

    # Get data
    try:
        data = np.loadtxt(file_name, skiprows=1, delimiter=",", max_rows=max_lines)
        sys.stdout.write('\rLoading file: %s' % file_name)
    except MemoryError:
        sys.stdout.write('\rRan out of memory loading: %s! :( Check file size fits in memory' % file_name)
    except FileNotFoundError:
        sys.stdout.write('\rFile not found: %s!' % file_name)
    
    sys.stdout.write('\rFile loaded successfully. Beginning processing')

    # Switch to numpy array 
    data_array = data.view()
    data_array = data_array.transpose()
    data_array = np.nan_to_num(data_array)
    if len(data_array[0]) > max_lines:
        max_lines = len(data_array[0])

    # Create figure
    fig = go.Figure()

    # Resample data
    data_resampled = []
    for i, _ in enumerate(data_array):
        data_resampled.append([])
        fig.add_trace(
            go.Scattergl(
                x=np.linspace(0, len(data_array[i]), len(data_array[i])),
                y=data_array[i],
                name='original-trace' + str(i),
                mode='lines',

            )
        )
        for j, resample_factor in enumerate(resample_factors):
            resampled_trace = signal.resample(data_array[i], int(max_lines/resample_factor))
            data_resampled[i].append(resampled_trace)
            fig.add_trace(
                go.Scattergl(
                    x=np.linspace(0, len(data_array[1]), len(resampled_trace)),
                    y=resampled_trace,
                    mode='lines',
                    name='resampled-trace' + str(i) + '-' + str(resample_factors[j]) + 'x',
                )
            )

    # with open(file_name.split[0] + '-downsampled.json', 'w') as f:
    #     json.dump({'data':data_resampled.tolist()}, f)



    plot(fig)

