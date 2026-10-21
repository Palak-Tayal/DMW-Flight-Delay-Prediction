I have completed a Data Mining and Warehousing (DMW) assignment on **Flight Departure Delay Prediction using Machine Learning**. I now need you to build a polished, functional Streamlit UI for the existing project.

I am providing my existing project files. Please inspect them carefully before writing any code. The main analysis and model evaluation are in `flight_data_analysis.ipynb`, and the project includes Python scripts, a trained model file, and CSV datasets.

### 1. First, understand my existing project

Inspect the provided files to determine:

- How the dataset was generated and structured.
- Which preprocessing steps were applied.
- Which features were used to train the models.
- How categorical and numerical features were handled.
- Which model was selected as the final candidate and its exact configuration.
- How the trained model and preprocessing pipeline were saved.
- Which input columns and data types the model expects.
- Which airline codes, airport codes, and weather variables exist in the dataset.

Do not assume the model's expected input columns or invent airport and airline categories. Derive them from the provided files.

### 2. Final model and evaluation results

Our current best candidate is a `HistGradientBoostingRegressor` pipeline named `stronger_model`.

Its recorded test-set results are:

- MAE: 14.2678 minutes
- RMSE: 17.7405 minutes
- R²: 0.1550
- Predictions within ±5 minutes: 21.82%
- Predictions within ±10 minutes: 42.02%
- Predictions within ±15 minutes: 59.37%
- Predictions within ±20 minutes: 73.17%
- Predictions within ±25 minutes: 83.44%

These results were obtained on a synthetic flight dataset. The UI must clearly identify this as an academic demonstration using synthetic data, not a validated real-world flight forecasting service.

You may display the evaluation metrics on the dashboard, but label them accurately. In particular, the 83.44% result is **the percentage of test-set predictions within ±25 minutes**, not conventional classification accuracy.

### 3. Build the Streamlit UI

Create a complete, ready-to-run `app.py` file with a clean, modern aviation analytics dashboard.

The application should include:

**A. Header and overview**
- Title: Flight Departure Delay Predictor.
- Short project description.
- A visible note that the dataset is synthetic.
- A neat, professional layout suitable for a college project demonstration.

**B. Flight input form**
Allow users to enter:
- Airline.
- Origin airport.
- Destination airport.
- Scheduled departure time.
- Flight distance.
- Month, day, and day of week, if required by the model.
- Weather features required by the model, such as temperature, humidity, precipitation, rain, cloud cover, wind speed, wind direction, pressure, and weather code, but only if those columns were actually used during training.

Use dropdowns for categorical fields and suitable number inputs or sliders for numerical fields. Use valid options and sensible defaults grounded in the project dataset.

Prevent the user from selecting the same origin and destination.

**C. Prediction**
- Load the existing trained model or pipeline from the provided saved model file.
- Predict the departure delay when the user clicks a button.
- Display the predicted delay in minutes in a clear result card.
- If negative predictions are possible, explain that a negative delay represents an early departure.
- Validate inputs and handle errors gracefully.
- Ensure the prediction input has exactly the expected feature names, columns, types, and preprocessing format.

**D. Analytics dashboard**
If appropriate and supported by the supplied data, include useful visualizations such as:
- Average departure delay by airline.
- Departure delay by scheduled departure hour.
- Delay distribution.
- Weather and delay relationships.

Load the existing dataset rather than fabricating chart data. Keep the dashboard lightweight and avoid reading a large CSV repeatedly on every rerun; use Streamlit caching where appropriate.

**E. Model evaluation section**
Display our final model metrics and explain:
- MAE.
- RMSE.
- R².
- Tolerance-based prediction performance.

Make the distinction between test-set evaluation and an individual prediction clear.

### 4. Critical technical requirements

- Preserve the existing trained model and preprocessing pipeline.
- Do not retrain models or repeat the completed analysis.
- Do not change the existing notebook, model-training scripts, or datasets.
- Do not modify or overwrite the saved model file.
- Do not silently substitute a different model or invent new model performance results.
- Avoid serialization problems involving notebook-defined functions, lambda functions, or objects that cannot be imported by Streamlit.
- If the existing `.pkl` file cannot be loaded safely, diagnose the precise cause and provide the smallest necessary fix. Do not assume the model can be loaded merely because the file exists.
- If the current model artifact is unusable, explain exactly what is missing and provide the smallest practical recovery procedure using the existing notebook and trained model. Do not rebuild the entire project.
- Use relative paths based on the location of `app.py`, so the app can run from the project directory.
- Do not require API keys, cloud services, or paid services.
- Keep the code compatible with the Python and library versions used by the existing project as far as possible.
- Include clear error messages for missing files, incompatible dependencies, or model-loading failures.
- Avoid unnecessary dependencies and unnecessary files.

### 5. Expected deliverables

Please provide:

1. The complete contents of `app.py`.
2. Any additional small helper file that is genuinely necessary for loading the existing model.
3. A list of required packages and a `requirements.txt` if useful.
4. The exact terminal command to launch the application in VS Code.
5. Any minimal setup or model-saving correction required before launching.
6. A brief explanation of how the UI connects to the existing trained model.

### 6. Work carefully

Before producing the final code, inspect the notebook and existing scripts for the exact model pipeline, feature columns, preprocessing, and artifact dependencies.

Do not give me a generic Streamlit template with guessed features. I need an application that is actually compatible with the project files I have provided.

The goal is to finish the UI without repeating the completed modeling work. Prioritize correctness, functionality, and a polished presentation over adding unnecessary features.
