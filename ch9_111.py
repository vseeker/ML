# encoding=utf-8
import codecs
import chardet
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
# f = open('city_location.txt', 'r')
# print chardet.detect(f.read())
# 如果是中文，程序内部尽量使用unicode，而不用str


def get_city_location(fl="city_location.txt"):
    """

    :param fl:the file which includes the locations of cities
    :return: a list which includes the locations of cities
    """
    city_location_list = []
    with codecs.open('location.txt', 'w+') as lp:
        with codecs.open(fl, encoding='utf-8') as fp:
            for ln in fp:
                if ln.find(':') + 1:
                    tmp1 = ln.find(u"经度")
                    tmp2 = ln.find(u"纬度", tmp1, -1)
                    if tmp1+1 and tmp2+1:
                        longitude = float(ln[tmp1+3:tmp2])
                        latitude = float(ln[tmp2+3:-2])
                        if 0 < latitude < 180 and 0 < longitude < 180:
                            city_location_list.append([longitude, latitude])

        print len(city_location_list)
        return city_location_list


X = np.array(get_city_location())
print 'X', X

n_clusters = 21

cls = AgglomerativeClustering(linkage='ward', n_clusters=n_clusters).fit(X)

cls.labels_
markers = ['^', 'x', 'o', '*', '+', '.', ',',
           'v', '<', '>', '1', '2', '3', '4',
           '8', 's', 'p', '_', '|', 'h', 'H']

color = [np.random.rand(3) for el in xrange(n_clusters)]
for i in range(n_clusters):
    members = cls.labels_ == i
    plt.scatter(X[members, 0], X[members, 1], s=60, marker=markers[i],
                c=color[i], alpha=0.5)
plt.title('*')
plt.show()