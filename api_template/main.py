from fastapi import FastAPI
from ml import predict
from preprocess import preprocess
from sample import Sample


app = FastAPI()


@app.post("/predict/")
def read_items(sample: Sample) -> int:
    sample_dict = sample.__dict__
    preprocessed_sample = preprocess(sample_dict)
    prediction = predict(preprocessed_sample)

    return prediction


@app.get("/whoami")
def whoami() -> str:
    # TODO
    isim = "Oğuzhan Sezer"
    soyisim = "Sezer"
    mail = "oguzhansezer14@gmail.com"
    
    person_card = {
        "isim": isim,
        "soyisim": soyisim,
        "mail": mail
    }

    return person_card


@app.get("/model_card")
def model_card() -> str:
    # TODO

    model_card = {
        'model_name': 'Hyperparameter Optimization',
        'model_description': 'TheBest',
        'model_version': '1.0',
        'model_author': 'Oğuzhan Sezer',
        'model_author_mail': 'oguzhansezer14@gmail.com',
        'model_creation_date': '29.03.2022',
        'model_last_update_date': '31.03.2022',
        'required_parameters_list': '',
        'required_parameters_descriptions': '',
    }

    return model_card


import uvicorn
if __name__=="__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=5000,log_level="info")
    





