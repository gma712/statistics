# coding: utf-8
import numpy as np


class OneDimentionalData(object):
    '''
    OneDimentionalData serves some tools to calculate arround one-dimantional-data.
    '''
    def __init__(self, array):
        self.array = array

    # 平均
    def average(self):
        return sum(self.array) / len(self.array)

    # 分散
    def variance(self):
        av = self.average()
        variance = sum([(i - av)**2 for i in self.array]) / len(self.array)
        return variance

    # 標準得点
    def standard_score_array(self):
        av = self.average()
        var = self.variance()
        z_array = [(i - av) / var for i in self.array]
        return z_array

    # 偏差値
    def deviation_score_array(self):
        z_array = self.standard_score_array()
        return list(map(lambda x: x * 10 + 50, z_array))

    # 相対頻度
    def relative_frequency_array(self):
        array = [i / sum(self.array) for i in self.array]
        return array

    # エントロピー
    def entropy_from_array(self):
        r_array = self.relative_frequency_array()
        entropy = -1 * sum([p_i * np.log10(p_i + 1e-10) for p_i in r_array])
        return entropy


def main():
    print('You can input numbers divided " ".')
    array = list(map(int, input().split(' ')))
    print('Your input: {}'.format(array))
    data = OneDimentionalData(array)
    print('平均値: {}'.format(data.average()))
    print('分散: {}'.format(data.variance()))
    print('標準得点: {}'.format(data.standard_score_array()))
    print('偏差値: {}'.format(data.deviation_score_array()))
    print('相対頻度: {}'.format(data.relative_frequency_array()))
    print('エントロピー（底10）: {}'.format(data.entropy_from_array()))


if __name__ == '__main__':
    main()
