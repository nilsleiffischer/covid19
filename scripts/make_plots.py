import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import locale
import matplotlib.dates as mdates
import logging
import yaml
from .load_data import load_jhu_data
from .plot import *


if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, '')
    if 'de_' not in locale.getlocale()[0]:
        try:
            locale.setlocale(locale.LC_ALL, "de_DE")
            logging.debug("Set LC_ALL to 'de_DE'.")
        except locale.Error:
            logging.warning("Unable to set locale")
    logging.debug("Using locale: LC_ALL={}, LC_TIME={}".format(
        locale.getlocale(locale.LC_ALL), locale.getlocale(locale.LC_TIME)))

    import os
    os.makedirs('plots', exist_ok=True)
    plot_daily_new_cases('plots/daily_new_cases.svg')
    # plot_timeshifts('plots/germany_total.svg')
    # plot_timeshifts('plots/germany_total_log.svg', log=True)
    # plot_german_states('plots/states.svg')
    # plot_german_states('plots/states_log.svg', log=True)

    # data_cds = load_cds_data()['cases']
    # for country in yaml.safe_load(open('data/fits.yaml')):
    #     plot_prediction(
    #         data_cds.loc[country['Dataset']],
    #         label=country['Name'],
    #         save_to='plots/prediction_{}.svg'.format(country['Slug']))
