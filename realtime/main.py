import data_collection
import feature_engineering
import data_processing

data = data_collection.get_live_data()
features = feature_engineering.build_features(data)
input_data = data_processing.preprocess(features)
