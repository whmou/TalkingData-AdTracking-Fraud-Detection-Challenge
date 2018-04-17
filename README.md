# TalkingData-AdTracking-Fraud-Detection-Challenge

A deep diving into a kaggle competetion "TalkingData-AdTracking-Fraud-Detection-Challenge" (https://www.kaggle.com/c/talkingdata-adtracking-fraud-detection/data)
Include 2 main parts:
- Data Exploration
- Classifiers Comparison
## Data Exploration
### Usage
```console
cd main/feature_insights/visualization/
python data_insights.py ../../main/data/train_sample.csv 
# output png files are in the output folder
```
  - Feature Heat Map: <br/>
  ![Heat Map](https://github.com/whmou/TalkingData-AdTracking-Fraud-Detection-Challenge/blob/master/main/feature_insights/visualization/output/corr_heat_map.png)
  - Feature Pair Map: <br/>
  ![Pair Map](https://github.com/whmou/TalkingData-AdTracking-Fraud-Detection-Challenge/blob/master/main/feature_insights/visualization/output/pair_plot.png)
 - Feature Histogram: <br/>
 ![histogram](https://github.com/whmou/TalkingData-AdTracking-Fraud-Detection-Challenge/blob/master/main/feature_insights/visualization/output/ip_histgram_amount_classes.png)
![histogram](https://github.com/whmou/TalkingData-AdTracking-Fraud-Detection-Challenge/blob/master/main/feature_insights/visualization/output/app_histgram_amount_classes.png)
![histogram](https://github.com/whmou/TalkingData-AdTracking-Fraud-Detection-Challenge/blob/master/main/feature_insights/visualization/output/device_histgram_amount_classes.png)
![histogram](https://github.com/whmou/TalkingData-AdTracking-Fraud-Detection-Challenge/blob/master/main/feature_insights/visualization/output/os_histgram_amount_classes.png)
![histogram](https://github.com/whmou/TalkingData-AdTracking-Fraud-Detection-Challenge/blob/master/main/feature_insights/visualization/output/channel_histgram_amount_classes.png)

  - Feature Boxplots: <br/>
   ![boxplot](https://github.com/whmou/TalkingData-AdTracking-Fraud-Detection-Challenge/blob/master/main/feature_insights/visualization/output/app_boxplot_amount_classes.png)
![boxplot](https://github.com/whmou/TalkingData-AdTracking-Fraud-Detection-Challenge/blob/master/main/feature_insights/visualization/output/ip_boxplot_amount_classes.png)
![boxplot](https://github.com/whmou/TalkingData-AdTracking-Fraud-Detection-Challenge/blob/master/main/feature_insights/visualization/output/app_boxplot_amount_classes.png)
![boxplot](https://github.com/whmou/TalkingData-AdTracking-Fraud-Detection-Challenge/blob/master/main/feature_insights/visualization/output/device_boxplot_amount_classes.png)
![boxplot](https://github.com/whmou/TalkingData-AdTracking-Fraud-Detection-Challenge/blob/master/main/feature_insights/visualization/output/os_boxplot_amount_classes.png)
![boxplot](https://github.com/whmou/TalkingData-AdTracking-Fraud-Detection-Challenge/blob/master/main/feature_insights/visualization/output/channel_boxplot_amount_classes.png)

## Feature importance

```
python main/feature_insights/importance/feautre_importances.py main/data/train_sample.csv

xgboost feature importance:
('app', 0.33282444)
('channel', 0.20305343)
('click_time', 0.079389311)
('device', 0.12977099)
('ip', 0.19083969)
('os', 0.06412214)

ExtraTrees feature importance:
('app', 0.21306116235738021)
('channel', 0.15531389700691334)
('click_time', 0.18661141480186574)
('device', 0.099059296834343447)
('ip', 0.20542837318401089)
('os', 0.14052585581548629)

RandomForest feature importance:
('app', 0.18273912869613443)
('channel', 0.15020469480418228)
('click_time', 0.12178531327828397)
('device', 0.15908994155421691)
('ip', 0.24489949043695178)
('os', 0.1412814312302306)
```
