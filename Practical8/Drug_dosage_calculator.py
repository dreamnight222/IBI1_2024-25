def calculate_drug_dosage(weight, strength):
    if not (10 <= weight <= 100):
        return "Error: Weight must be between 10 and 100 kg"
    if strength not in [120, 250]:
        return "Error: Strength must be 120 or 250 mg/5 ml"
    
    dose_mg = 15 * weight
    if strength == 120:
        volume_ml = (dose_mg * 5) / 120
    else:
        volume_ml = (dose_mg * 5) / 250
    return round(volume_ml, 2)

# example
print(calculate_drug_dosage(20, 120))  # output 12.5
print(calculate_drug_dosage(50, 250))  # output 15.0