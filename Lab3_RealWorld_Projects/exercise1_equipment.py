# APPENDIX 1 - Equipment Diagnostic System - Torres
LAST_NAME = "TORRES"
SEED_NUM = 4
FAVORITE_ARTIST = "POST MALONE" 

# 1. Decorator to record diagnostic process
def diagnostic_logger(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Starting {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"[LOG] Finished {func.__name__} -> {result}")
        return result
    return wrapper

# 2. Generate student-specific readings
def generate_readings():
    base = len(LAST_NAME) + SEED_NUM  # 6 + 4 = 10
    artist_factor = len(FAVORITE_ARTIST)
    readings = [base + i*2 + (artist_factor % 5) for i in range(5)]
    print(f"Generated Equipment Data (based on {LAST_NAME}/{SEED_NUM}/{FAVORITE_ARTIST}): {readings}")
    return readings

# 3. Validation
def validate_readings(data):
    if not data:
        raise ValueError("No readings found!")
    for val in data:
        if val < 0 or val > 100:
            raise ValueError(f"Invalid reading: {val}")
    print(f"Validation Results: All {len(data)} readings VALID")
    return True

# 4. Calculation
@diagnostic_logger
def calculate_average(data):
    return sum(data) / len(data)

# 5. Classification
@diagnostic_logger
def classify_condition(avg):
    if avg < 20:
        return "GOOD - Equipment Normal"
    elif avg < 30:
        return "WARNING - Needs Monitoring"
    else:
        return "CRITICAL - Immediate Check Required"

# Main Execution with Exception Handling
try:
    readings = generate_readings()
    validate_readings(readings)
    avg = calculate_average(readings)
    diagnosis = classify_condition(avg)
    
    print("\n--- FINAL DIAGNOSTIC SUMMARY ---")
    print(f"Average Reading: {avg}")
    print(f"Diagnostic Results: {diagnosis}")
    print(f"Execution Log: Decorator recorded calculation and classification")
    
except Exception as e:
    print(f"[ERROR] Diagnostic failed: {e}")