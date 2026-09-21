# APPENDIX 2 - Recursive Fault Trace - Torres - POST MALONE
LAST_NAME = "TORRES"
SEED_NUM = 4
FAVORITE_ARTIST = "POST MALONE"

def generate_fault_code():
    # Formula: (Surname Length * 10) + SEED + Artist Length
    # (6*10) + 4 + 11 = 75
    code = (len(LAST_NAME) * 10) + SEED_NUM + len(FAVORITE_ARTIST)
    print(f"Generated Fault Data: {code} (based on {LAST_NAME}/{SEED_NUM}/{FAVORITE_ARTIST})")
    return code

def recursive_trace(fault_code, level=1):
    print(f"Trace {level}: Fault Code {fault_code}")
    if fault_code <= SEED_NUM:
        print(f"Level {level}: Fault code {fault_code} reached termination. Diagnostic Complete.")
        return [fault_code]
    else:
        next_code = fault_code - len(LAST_NAME)  # minus 6 each level
        return [fault_code] + recursive_trace(next_code, level+1)

# Execution
fault = generate_fault_code()
sequence = recursive_trace(fault)

print(f"\n--- FINAL TRACE SUMMARY ---")
print(f"Generated Fault Data: {fault}")
print(f"Trace Summary: {sequence}")
print(f"Recursive Calls: {len(sequence)}")
print(f"Termination Point: {sequence[-1]}")
print(f"Final Output: {sequence[-1]} (with termination message)")