import joblib

class SaveModel:
    def save_model(self, model, model_path='stock-high-low.pkl'):
        joblib.dump(model, model_path)
