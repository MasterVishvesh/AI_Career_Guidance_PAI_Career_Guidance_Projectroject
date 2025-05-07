def recommend_career(skills_with_levels, interests, experience):
    skill_names = [skill.lower() for skill in skills_with_levels.keys()]
    skill_strength = sum(skills_with_levels.values()) / len(skills_with_levels)

    # 🔒 Custom logic for Java + DSA
    if "java" in skill_names and ("dsa" in skill_names or "data structures" in skill_names):
        if skill_strength >= 7 and experience >= 5:
            return "Senior Java Developer", 100000
        elif skill_strength >= 5 and experience >= 3:
            return "Java Developer", 75000
        elif skill_strength >= 2 and experience >= 1:
            return "Junior Java Developer", 55000
        else:
            return "Java Intern", 30000

    # 📊 General logic
    if skill_strength > 7 and experience >= 7:
        recommended_career = "Sr. Software Engineer"
        avg_salary = 100000
    elif skill_strength >= 5 and experience >= 5:
        recommended_career = "Data Analyst"
        avg_salary = 70000
    elif skill_strength >= 2 and experience >= 3:
        recommended_career = "Data Analyst"
        avg_salary = 50000
    else:
        recommended_career = "Support Engineer, Jr. Software Engineer"
        avg_salary = 35000

    return recommended_career, avg_salary
