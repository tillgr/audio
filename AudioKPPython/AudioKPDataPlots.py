import matplotlib.pyplot as plt
import numpy as np
import json
import pathlib as pl
import collections as coll


def make_hist(title, xlabel, data, numbins=20):
    figure = plt.figure("{} histogram".format(title))
    plt.title(title)
    plt.ylabel("number of audio files")
    plt.xlabel(xlabel)
    plt.xlim([data.min(), data.max()])
    n, bins, _ = plt.hist(data, numbins)
    bins = (bins[:-1] + bins[1:]) / 2.
    plt.errorbar(bins, n, yerr=np.sqrt(n), linestyle="none", capsize=2)
    plt.savefig("plots/{}_hist.svg".format(title))
    plt.show()


def plot_data(title, ylabel, data, errpl=False, err=None):
    fig = plt.figure(title)
    sampleaxis = range(len(data))
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel("audio files")
    plt.xlim([0, len(data)])
    plt.ylim([data.min(), data.max()])
    if errpl:
        plt.errorbar(sampleaxis, data, xerr=0.5, yerr=err/2., label=title, fmt='none', elinewidth=0.25, capsize=2, capthick=0.25)
    else:
        plt.plot(sampleaxis, data, '+', label=title)
    plt.savefig("plots/{}_data.svg".format(title))
    plt.show()


if __name__ == "__main__":

    jsonFolder = pl.Path("../../EXTRACT_FSDKaggle2018.audio_train").rglob("*.json")

    average_loudness = []

    spectral_centroid = []
    spectral_centroid_stdev = []

    spectral_flux = []
    spectral_flux_stdev = []

    dissonance = []
    dissonance_stdev = []

    dynamic_complexity = []

    zerocrossingrate = []
    zerocrossingrate_stdev = []

    hfc = []
    hfc_stdev = []

    spectral_skewness = []
    spectral_skewness_stdev = []

    key_krumhansl = []
    strength_krumhansl = []

    pitch_salience = []
    pitch_salience_stdev = []

    for file in jsonFolder:
        # print("\n\n spectral_centroid:  \n")
        # print(spectral_centroid)
        jsonFile = open(file, "r")
        jsonFileContent = jsonFile.read()
        jsonData = json.loads(jsonFileContent)

        average_loudness.append(jsonData["lowlevel"]["average_loudness"])

        spectral_centroid.append(jsonData["lowlevel"]["spectral_centroid"]["mean"])
        spectral_centroid_stdev.append(jsonData["lowlevel"]["spectral_centroid"]["stdev"])

        spectral_flux.append(jsonData["lowlevel"]["spectral_flux"]["mean"])
        spectral_flux_stdev.append(jsonData["lowlevel"]["spectral_flux"]["stdev"])

        dissonance.append(jsonData["lowlevel"]["dissonance"]["mean"])
        dissonance_stdev.append(jsonData["lowlevel"]["dissonance"]["stdev"])

        dynamic_complexity.append(jsonData["lowlevel"]["dynamic_complexity"])

        zerocrossingrate.append(jsonData["lowlevel"]["zerocrossingrate"]["mean"])
        zerocrossingrate_stdev.append(jsonData["lowlevel"]["zerocrossingrate"]["stdev"])

        hfc.append(jsonData["lowlevel"]["hfc"]["mean"])
        hfc_stdev.append(jsonData["lowlevel"]["hfc"]["stdev"])

        spectral_skewness.append(jsonData["lowlevel"]["spectral_skewness"]["mean"])
        spectral_skewness_stdev.append(jsonData["lowlevel"]["spectral_skewness"]["stdev"])

        key_krumhansl.append(jsonData["tonal"]["key_krumhansl"]["key"])
        strength_krumhansl.append(jsonData["tonal"]["key_krumhansl"]["strength"])

        pitch_salience.append(jsonData["lowlevel"]["pitch_salience"]["mean"])
        pitch_salience_stdev.append(jsonData["lowlevel"]["pitch_salience"]["stdev"])

        jsonFile.close()

    # average_loudness
    np_average_loudness = np.array(average_loudness)
    plot_data("average loudness", "loudness", np_average_loudness)
    make_hist("average loudness", "loudness", np_average_loudness)

    # spectral centroid
    np_spectral_centroid = np.array(spectral_centroid)
    np_spectral_centroid_stdev = np.array(spectral_centroid_stdev)
    plot_data("spectral centroid", "frequency", np_spectral_centroid, errpl=True, err=np_spectral_centroid_stdev)
    make_hist("spectral centroid", "frequency", np_spectral_centroid)

    # spectral flux
    np_spectral_flux = np.array(spectral_flux)
    np_spectral_flux_stdev = np.array(spectral_flux_stdev)
    plot_data("spectral flux", "power", np_spectral_flux, errpl=True, err=np_spectral_flux_stdev)
    make_hist("spectral flux", "power", np.sqrt(np_spectral_flux), numbins=30)

    # dissonance
    np_dissonance = np.array(dissonance)
    np_dissonance_stdev = np.array(dissonance_stdev)
    plot_data("dissonance", "dissonance", np_dissonance, errpl=True, err=np_dissonance_stdev)
    make_hist("dissonance", "dissonance", np_dissonance, numbins=30)

    # dynamic_complexity
    np_dynamic_complexity = np.array(dynamic_complexity)
    plot_data("dynamic complexity", "dynamic complexity", np_dynamic_complexity)
    make_hist("dynamic complexity", "dynamic complexity", np_dynamic_complexity)

    # zero crossing rate
    np_zerocrossingrate = np.array(zerocrossingrate)
    np_zerocrossingrate_stdev = np.array(zerocrossingrate_stdev)
    plot_data("zero crossing rate", "rate", np_zerocrossingrate, errpl=True, err=np_zerocrossingrate_stdev)
    make_hist("zero crossing rate", "rate", np_zerocrossingrate)

    # hfc
    np_hfc = np.array(hfc)
    np_hfc_stdev = np.array(hfc_stdev)
    plot_data("high frequency content", "high-frequency coefficient [unknown]", np_hfc, errpl=True, err=np_hfc_stdev)
    make_hist("high frequency content", "high-frequency coefficient [unknown]", np_hfc)

    # spectral_skewness
    np_spectral_skewness = np.array(spectral_skewness)
    np_spectral_skewness_stdev = np.array(spectral_skewness_stdev)
    plot_data("spectral skewness", "skewness", np_spectral_skewness, errpl=True, err=np_spectral_skewness_stdev)
    make_hist("spectral skewness", "skewness", np_spectral_skewness)

    # key_krumhansl
    letter_counter = coll.Counter(key_krumhansl)
    fig = plt.figure("key krumhansl")
    plt.title("key (krumhansl)")
    plt.xlabel("pitch class / key")
    plt.ylabel("number of audio files")
    ax = fig.add_subplot(111)
    ax.xaxis.set_major_locator(plt.FixedLocator(range(len(letter_counter))))
    ax.xaxis.set_major_formatter(plt.FixedFormatter(list(letter_counter.keys())))
    ax.bar(range(len(letter_counter)), letter_counter.values(), align="center")
    plt.savefig("plots/key krumhansel.svg")
    plt.show()

    # pitch_salience
    np_pitch_salience = np.array(pitch_salience)
    np_pitch_salience_stdev = np.array(pitch_salience_stdev)
    plot_data("pitch salience", "salience", np_pitch_salience, errpl=True, err=np_pitch_salience_stdev)
    make_hist("pitch salience", "salience", np_pitch_salience)

    # correlation example
    fig = plt.figure("plot")
    plt.title("normalised spectral centroid and dynamic complexity")
    plt.xlabel("audio files")
    plt.xlim([0, len(np_spectral_centroid)])
    plt.ylim([0, 1])

    norm_centroid = np_spectral_centroid / np_spectral_centroid.max()
    norm_dyncomplexity = np_dynamic_complexity/ np_dynamic_complexity.max()

    plt.plot(range(len(np_dynamic_complexity)), norm_dyncomplexity, '+', label="dyn compl")
    plt.plot(range(len(np_spectral_centroid)), norm_centroid, '+', label="spec centr")
    plt.legend()
    plt.savefig("plots/spec_cen_dyn_comp.svg")
    plt.show()

    fig = plt.figure("plot")
    plt.title("normalised dynamic complexity over normalised spectral centroid")
    plt.xlabel("spectral centroid")
    plt.ylabel("dynamic complexity")
    plt.plot(norm_centroid, norm_dyncomplexity, '+')
    # plt.plot(range(len(np_spectral_centroid)), norm_centroid, '+', label="spec centr")
    # plt.legend()
    plt.savefig("plots/dyn_comp_over_spec_cen.svg")
    plt.show()

    # no correlation example
    ind = np.argsort(norm_centroid)
    sorted_norm_centroid = np.sort(norm_centroid)
    sorted_norm_dyncomplexity = norm_dyncomplexity[ind]

    fig = plt.figure("plot")
    plt.title("normalised spectral centroid and dynamic complexity - sorted")
    plt.xlabel("audio files")
    plt.xlim([0, len(np_spectral_centroid)])
    plt.ylim([0, 1])

    plt.plot(range(len(np_dynamic_complexity)), sorted_norm_dyncomplexity, '+', label="dyn compl")
    plt.plot(range(len(np_spectral_centroid)), sorted_norm_centroid, '+', label="spec centr")
    plt.legend()
    plt.savefig("plots/spec_cen_dyn_comp_sorted.svg")
    plt.show()
