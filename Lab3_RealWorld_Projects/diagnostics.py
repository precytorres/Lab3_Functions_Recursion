def diagnostic_logger(f):
    def w(*a,**k):
        print(f"[DIAG] Checking {f.__name__}"); r=f(*a,**k); print(f"[DIAG] Result: {r}"); return r
    return w

classify_status = lambda avg: "GOOD" if avg<30 else "WARNING" if avg<40 else "CRITICAL"

def recursive_trace(code, step=6):
    print(f"-> Trace {code}")
    if code<=4: return [code]
    return [code] + recursive_trace(code-step)

@diagnostic_logger
def validate(data):
    valid=[x for x in data if 0<=x<=100]
    invalid=len(data)-len(valid)
    print(f"Valid: {len(valid)}, Invalid: {invalid}")
    return valid, invalid