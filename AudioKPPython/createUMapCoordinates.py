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
    names = []

    for file in dataFolder:
        dataPoint = []
        names.append(file.stem)

        jsonFile = open(file, "r")
        jsonFileContent = jsonFile.read()
        jsonData = json.loads(jsonFileContent)

        dataPoint.append(jsonData["lowlevel"]["average_loudness"])
        dataPoint.append(jsonData["lowlevel"]["zerocrossingrate"]["mean"])
        dataPoint.append(jsonData["lowlevel"]["spectral_centroid"]["mean"])
        dataPoint.append(jsonData["lowlevel"]["pitch_salience"]["mean"])
        dataPoint.append(jsonData["lowlevel"]["dissonance"]["mean"])

        data.append(dataPoint)

    reducer = umap.UMAP(min_dist=4.99, n_neighbors=200, spread=5.0)
    data = np.array(data)

    scaledData = StandardScaler().fit_transform(data)

    embedding = reducer.fit_transform(scaledData)
    print(embedding.shape)

    plot_data("coordUmap", embedding[:, 0], embedding[:, 1])

    completeDict = []
    if len(data) == len(embedding) and len(names) == embedding.shape[0]:
        for i in range(len(embedding)):
            singleEntry = {'name': names[i],
                           'x': float(embedding[i][0]),
                           'y': float(embedding[i][1]),
                           'loudness': float(data[i][0]),
                           'raspiness': float(data[i][1]),
                           'color': float(data[i][2]),
                           'stability': float(data[i][3]),
                           'tonality': float(data[i][4])}
            completeDict.append(singleEntry)

            # write single entry files
            # filename = "coord/{}_coo.json".format(names[i])
            # json.dump(singleEntry, open(filename, 'w', encoding='utf-8'), indent=4)

        json.dump(completeDict, open("coord/completeDict.json", 'w', encoding='utf-8'), indent=4)



