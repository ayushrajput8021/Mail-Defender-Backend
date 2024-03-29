import pickle

loaded_model = pickle.load(open('./Models/trained_model.sav', 'rb'))
feature_extraction = pickle.load(open('./Models/feature_extraction.sav', 'rb'))


def Predict(text):
    input_mail = [text]
    input_data_features = feature_extraction.transform(input_mail)
    prediction = loaded_model.predict(input_data_features)
    return prediction
