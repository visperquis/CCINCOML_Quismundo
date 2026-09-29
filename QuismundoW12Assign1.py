Quismundo_patients = {
    "Ana": (80, 50, 150, 90, 140),
    "Ben": (130, 140, 135, 90, 140),
    "Carlo": (90, 100, 95, 140)
}
print(Quismundo_patients)
print()
for patient, readings in Quismundo_patients.items():
    print("Patient:", patient)
    average=0
    high_count=0
    print("==== BLOOD SUGAR SUMMARY ====")
    for Quismundo_reading in readings:
        if Quismundo_reading>120:
            status = "High"
            high_count +=1
        else:
            status="Normal"

    print(Quismundo_reading, "-", status)
    print("Number of High Readings:", high_count)
    print("Highest Blood Sugar Count", max(readings), "-", patient)
    print("Lowest Blood Sugar Count", min(readings), "-", patient)
    print(f"Average: {average:.2f}")
    print("Difference: ", max(readings)-min(readings))