from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from prometheus_fastapi_instrumentator import Instrumentator
import numpy as np
from prometheus_client import Histogram
from prometheus_client import Histogram, Counter # ваш код здесь — необходимый импорт

# создание экземпляра FastAPI-приложения
app = FastAPI()

# инициализируем и запускаем экпортёр метрик
instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

main_app_predictions = Histogram(
    # имя метрики
    "main_app_predictions",
    # описание метрики
    "Histogram of predictions",
    # указываем корзины для гистограммы
    buckets=(1, 2, 4, 5, 10)
)


# Счётчик положительных предсказаний
positive_predictions_counter = Counter(
    "positive_predictions_total",
    "Total count of positive predictions (prediction > 0)"
)# ваш код здесь — объект для сбора метрики

@app.get("/predict")
def predict(x: int, y: int):
    np.random.seed(x)
    prediction = x+y + np.random.normal(0,1)
    main_app_predictions.observe(prediction)
    
    # Увеличиваем счётчик, если предсказание положительное
    if prediction > 0:
        positive_predictions_counter.inc()    # ваш код здесь — увеличение метрики счётчика
    

    return {'prediction': prediction}