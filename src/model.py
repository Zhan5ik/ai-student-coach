def predict_risk(model, student_row):
    return model.predict_proba(student_row)[0][1]
