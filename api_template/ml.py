import pickle

# TODO
model_path = 'models/Hyper.pkl'


with open(model_path, 'rb') as f:
    model = pickle.load(f)


def predict(sample):
    return model.predict(sample).tolist()[0]