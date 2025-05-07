# utils/custom_transformers.py

from sklearn.base import BaseEstimator, TransformerMixin

class extract_text_column(BaseEstimator, TransformerMixin):
    def __init__(self, key):
        self.key = key

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X[self.key]

# ✅ Add this new function:
def reshape_column(x):
    return x.values.reshape(-1, 1)

class CombineSkillsTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        combined = []
        for skills, levels in zip(X["Skills"], X["Skill_Levels"]):
            skills_list = skills.split(",")
            levels_list = levels.split(",")
            combo = [f"{s.strip()}_{levels_list[i].strip()}" if i < len(levels_list) else s.strip()
                     for i, s in enumerate(skills_list)]
            combined.append(" ".join(combo))
        return np.array(combined).reshape(-1, 1)
