import umap
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np
import json
import pathlib as pl


def plot_data(title, x, y):
    fig = plt.figure(title)
    plt.title(title)
    plt.ylabel("???y")
    plt.xlabel("???x")
    plt.xlim([x.min(), x.max()])
    plt.ylim([y.min(), y.max()])
    plt.plot(x, y, '.', label=title)
    plt.savefig("coord/{}.svg".format(title))
    plt.show()


if __name__ == "__main__":

    dataFolder = pl.Path("../../EXTRACT_FSDKaggle2018.audio_train").rglob("*.json")

    data = []

    for file in dataFolder:
        dataPoint = []

        jsonFile = open(file, "r")
        jsonFileContent = jsonFile.read()
        jsonData = json.loads(jsonFileContent)

        dataPoint.append(jsonData["lowlevel"]["average_loudness"])
        dataPoint.append(jsonData["lowlevel"]["zerocrossingrate"]["mean"])
        dataPoint.append(jsonData["lowlevel"]["hfc"]["mean"])
        dataPoint.append(jsonData["lowlevel"]["spectral_centroid"]["mean"])
        dataPoint.append(jsonData["lowlevel"]["pitch_salience"]["mean"])
        dataPoint.append(jsonData["lowlevel"]["dissonance"]["mean"])

        data.append(dataPoint)

    reducer = umap.UMAP()
    data = np.array(data)

    scaledData = StandardScaler().fit_transform(data)

    embedding = reducer.fit_transform(scaledData)
    print(embedding.shape)

    plot_data("coordUmap", embedding[:, 0], embedding[:, 1])
    coordFile = "coordinates.json"



