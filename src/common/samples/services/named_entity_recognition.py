import json
from soffosai import SoffosAIServices


service = SoffosAIServices.NERService()
output = service(
    user = 'client_id',
    text = "Patient Name: John Smith\nDate of Admission: June 15, 2023\nMedical Record Number: 123456789\n\nChief Complaint:\nThe patient presents with severe abdominal pain and vomiting.\n\nHistory of Present Illness:\nMr. Smith, a 45-year-old male, reports the onset of abdominal pain two days ago. The pain is localized to the lower right quadrant and has been progressively worsening. He has experienced multiple episodes of non-bloody vomiting. No significant alleviating or exacerbating factors have been identified.\n\nPast Medical History:\nThe patient has a history of hypertension and type 2 diabetes mellitus. He underwent an appendectomy in his childhood. He denies any known allergies or previous surgeries.\n\nMedications:\n- Lisinopril 10mg once daily for hypertension\n- Metformin 500mg twice daily for diabetes\n\nFamily History:\nThe patient's father had a history of myocardial infarction at the age of 60. His mother is alive and well with no significant medical conditions. There is no known family history of gastrointestinal disorders.\n\nSocial History:\nMr. Smith is a non-smoker and does not consume alcohol. He is married and works as an accountant. He denies any illicit drug use.\n\nPhysical Examination:\n- Vital Signs: Blood pressure 130/80 mmHg, heart rate 82 bpm, respiratory rate 16 breaths per minute, temperature 37.2°C (oral)\n- General: The patient appears uncomfortable and is lying still in bed.\n- Abdomen: There is tenderness in the right lower quadrant with guarding and rebound tenderness. No palpable masses or organomegaly. Bowel sounds are diminished.\n\nAssessment and Plan:\nThe patient's presentation is concerning for acute appendicitis. He will undergo further diagnostic evaluation, including complete blood count, urinalysis, and abdominal ultrasound. In the meantime, he will be kept NPO (nothing by mouth) and started on intravenous fluids. Surgical consultation will be obtained for potential appendectomy.\n\nPlease note that this is a fictional clinical text generated for demonstration purposes only. Any resemblance to actual patients or medical scenarios is purely coincidental.",
    labels = {
        "PERSON": "Refers to the name of the patient",
        "DATE": "Represents dates mentioned in the text",
        "MEDICAL_RECORD_NUMBER": "Identifies the unique identifier for the patient's medical record",
        "CHIEF_COMPLAINT": "Describes the primary reason for the patient's visit or main symptom",
        "SURGICAL_HISTORY": "Lists any previous surgeries the patient has undergone.",
        "ALLERGIES": "Indicates any known allergies or sensitivities the patient has",
        "MEDICATION": "Refers to current medications being taken by the patient",
        "DIAGNOSIS": "Specifies the preliminary or final diagnosis of the patient's condition"
    }
)
print(json.dumps(output, indent=4))


# Labels can also be added like this:
service.add_label("PERSON", "Refers to the name of the patient")
service.add_label("DATE", "Represents dates mentioned in the text")
output = service(
    user = 'client_id',
    text = "Patient Name: John Smith\nDate of Admission: June 15, 2023\nMedical Record Number: 123456789\n\nChief Complaint:\nThe patient presents with severe abdominal pain and vomiting.\n\nHistory of Present Illness:\nMr. Smith, a 45-year-old male, reports the onset of abdominal pain two days ago. The pain is localized to the lower right quadrant and has been progressively worsening. He has experienced multiple episodes of non-bloody vomiting. No significant alleviating or exacerbating factors have been identified.\n\nPast Medical History:\nThe patient has a history of hypertension and type 2 diabetes mellitus. He underwent an appendectomy in his childhood. He denies any known allergies or previous surgeries.\n\nMedications:\n- Lisinopril 10mg once daily for hypertension\n- Metformin 500mg twice daily for diabetes\n\nFamily History:\nThe patient's father had a history of myocardial infarction at the age of 60. His mother is alive and well with no significant medical conditions. There is no known family history of gastrointestinal disorders.\n\nSocial History:\nMr. Smith is a non-smoker and does not consume alcohol. He is married and works as an accountant. He denies any illicit drug use.\n\nPhysical Examination:\n- Vital Signs: Blood pressure 130/80 mmHg, heart rate 82 bpm, respiratory rate 16 breaths per minute, temperature 37.2°C (oral)\n- General: The patient appears uncomfortable and is lying still in bed.\n- Abdomen: There is tenderness in the right lower quadrant with guarding and rebound tenderness. No palpable masses or organomegaly. Bowel sounds are diminished.\n\nAssessment and Plan:\nThe patient's presentation is concerning for acute appendicitis. He will undergo further diagnostic evaluation, including complete blood count, urinalysis, and abdominal ultrasound. In the meantime, he will be kept NPO (nothing by mouth) and started on intravenous fluids. Surgical consultation will be obtained for potential appendectomy.\n\nPlease note that this is a fictional clinical text generated for demonstration purposes only. Any resemblance to actual patients or medical scenarios is purely coincidental.",
)
print(json.dumps(output, indent=4))