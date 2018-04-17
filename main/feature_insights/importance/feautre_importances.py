import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
import sys


class FeatureImportance(object):
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = pd.read_csv(file_path, parse_dates=[5, 6])
        y_header_naming = 'is_attributed'
        self.headers = [
            x for x in list(
                self.df.columns.values) if 'time' not in x and y_header_naming not in x]
        self.Y_train = self.df[y_header_naming]
        self.X_train = self.df.loc[:, self.df.columns != y_header_naming]
        self.feature_processing()

    def feature_processing(self):
        self.X_train.drop('attributed_time', 1, inplace=True)
        self.X_train = self.X_train.assign(
            click_time=pd.to_datetime(
                self.X_train['click_time']).astype(int))
        self.X_train['click_time'] = self.X_train['click_time'] / (10**9)

    def importance_by_xgboost(self):
        model = XGBClassifier()
        model.fit(self.X_train, self.Y_train)
        print 'xgboost feature importance:'
        for feature in tuple(
                sorted(zip(self.X_train.columns.values, model.feature_importances_))):
            print feature

    def importance_by_extratress(self):
        model = ExtraTreesClassifier(n_estimators=250, random_state=5)
        model.fit(self.X_train, self.Y_train)
        print '\nExtraTrees feature importance:'
        for feature in tuple(
                sorted(zip(self.X_train.columns.values, model.feature_importances_))):
            print feature

    def importance_by_rf(self):
        model = RandomForestClassifier(max_depth=5, random_state=5)
        model.fit(self.X_train, self.Y_train)
        print '\nRandomForest feature importance:'
        for feature in tuple(
                sorted(zip(self.X_train.columns.values, model.feature_importances_))):
            print feature


if __name__ == '__main__':
    csv_file_name = sys.argv[1]
    fi = FeatureImportance(csv_file_name)
    fi.importance_by_xgboost()
    fi.importance_by_extratress()
    fi.importance_by_rf()
