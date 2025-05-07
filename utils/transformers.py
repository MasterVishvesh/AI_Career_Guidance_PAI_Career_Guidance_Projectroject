from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd

class SkillCombiner(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        combined_skills = []
        for skills, levels in zip(X["Skills"], X["Skill_Levels"]):
            skills_list = skills.split(",")
            levels_list = levels.split(",")
            combined = [
                f"{s.strip()}_{levels_list[i].strip()}" if i < len(levels_list) else s.strip()
                for i, s in enumerate(skills_list)
            ]
            combined_skills.append(" ".join(combined))

        return pd.DataFrame({
            "Combined_Skills": combined_skills,
            "Interests": X["Interests"].values,
            "Experience": X["Experience"].values
        })
