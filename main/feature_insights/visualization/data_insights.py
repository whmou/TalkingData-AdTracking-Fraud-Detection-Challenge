import sys
import pandas as pd
from scipy.stats import norm
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import seaborn as sns


class DataInsights(object):

    def __init__(self, file_path):
        self.file_path = file_path
        self.df = pd.read_csv(csv_file_name)
        self.headers = [
            x for x in list(
                self.df.columns.values) if 'time' not in x and 'is_attributed' not in x]
        print 'inspect headers: {0}'.format(self.headers)
        print 'total counts: {0}'.format(len(self.df))
        print 'positive counts: {0}'.format(
            len(self.df.query('is_attributed == 1')))
        self.pos_df = self.df.query('is_attributed == 1')
        self.neg_df = self.df.query('is_attributed == 0')

    def gen_all_plots(self, png_output_folder):
        self.boxplot_amount_classes(png_output_folder)
        self.histgram_amount_classes(png_output_folder)
        self.corr_heat_map(png_output_folder)
        self.pair_plot(png_output_folder)

    def boxplot_amount_classes(self, png_output_folder):
        for feature in self.headers:
            plt.clf()
            output_file_path = '{0}/{1}_boxplot_amount_classes.png'.format(
                png_output_folder, feature)
            pos_quantile_list = self.pos_df[feature].describe().tolist()[3:]
            neg_quantile_list = self.neg_df[feature].describe().tolist()[3:]
            plt.title(feature)
            plt.xticks([1, 2], ['{0} positive'.format(
                feature), '{0} negative'.format(feature)], rotation=0)
            pt = plt.boxplot(
                [self.pos_df[feature], self.neg_df[feature]], patch_artist=True, sym='')
            for patch, color in zip(pt['boxes'], ['red', 'blue']):
                patch.set_facecolor(color)
            plt.savefig(output_file_path)

    def histgram_amount_classes(self, png_output_folder):
        for feature in self.headers:
            plt.clf()
            output_file_path = '{0}/{1}_histgram_amount_classes.png'.format(
                png_output_folder, feature)
            n, bins, patches = plt.hist(
                self.df[feature], 100, normed=1, facecolor='green', alpha=0.5)
            (mu, sigma) = norm.fit(self.df[feature])
            y = mlab.normpdf(bins, mu, sigma)
            plt.plot(bins, y, 'r--')
            plt.xlabel(feature)
            plt.ylabel('Value')
            plt.savefig(output_file_path)

    def corr_heat_map(self, png_output_folder):
        plt.clf()
        output_file_path = '{0}/corr_heat_map.png'.format(png_output_folder)
        corrmat = self.df.corr()
        sns.heatmap(corrmat,
                    xticklabels=corrmat.columns,
                    yticklabels=corrmat.columns, annot=True)
        plt.savefig(output_file_path)

    def pair_plot(self, png_output_folder):
        plt.clf()
        sns.set()
        output_file_path = '{0}/pair_plot.png'.format(png_output_folder)
        sns.pairplot(
            data=self.df[['ip', 'app', 'device', 'os', 'channel']], size=2.5)
        plt.savefig(output_file_path)


if __name__ == '__main__':
    csv_file_name = sys.argv[1] 
    di = DataInsights(csv_file_name)
    di.gen_all_plots('output')
