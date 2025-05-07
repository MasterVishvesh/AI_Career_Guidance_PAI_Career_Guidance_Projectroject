import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from joblib import dump
from utils.transformers import SkillCombiner

# Load dataset
df = pd.read_csv("data/expanded_career_dataset.csv")

# Split inputs and targets
X = df[["Skills", "Skill_Levels", "Interests", "Experience"]]
y_career = df["Recommended_Career"]
y_salary = df["Average_Salary"]

# Preprocessing pipeline
preprocessor = ColumnTransformer(transformers=[
    ("tfidf_skills", TfidfVectorizer(), "Combined_Skills"),
    ("tfidf_interests", TfidfVectorizer(), "Interests"),
    # ("scale_exp", StandardScaler(), "Experience")
    ("scale_exp", StandardScaler(), ["Experience"]) 

])

# Full pipeline with custom transformer
career_pipeline = Pipeline(steps=[
    ("combine", SkillCombiner()),
    ("preprocess", preprocessor),
    ("classifier", RandomForestClassifier(random_state=42))
])

salary_pipeline = Pipeline(steps=[
    ("combine", SkillCombiner()),
    ("preprocess", preprocessor),
    ("regressor", RandomForestRegressor(random_state=42))
])

# Train models
career_pipeline.fit(X, y_career)
salary_pipeline.fit(X, y_salary)

# Save models
dump(career_pipeline, "model/career_model_pipeline.pkl")
dump(salary_pipeline, "model/salary_model_pipeline.pkl")
print("✅ Models trained and saved successfully.")
