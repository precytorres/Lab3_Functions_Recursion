from telemetry import sensor_stream
from diagnostics import validate, classify_status, recursive_trace

LAST_NAME="TORRES"; SEED_NUM=4; FAVORITE_ARTIST="POST MALONE"

def main():
    print(f"--- EXERCISE 3 PIPELINE - {LAST_NAME}/{SEED_NUM}/{FAVORITE_ARTIST} ---")
    readings=list(sensor_stream())
    print(f"Raw Stream: {readings}")
    valid, invalid_count = validate(readings)
    print(f"Processed: {len(readings)}, Valid: {len(valid)}, Invalid: {invalid_count}")

    if valid:
        avg=sum(valid)/len(valid)
        status=classify_status(avg)
        print(f"Average: {avg:.2f} -> Status: {status}")
        fault=(len(LAST_NAME)*10)+SEED_NUM+len(FAVORITE_ARTIST)
        print(f"Generated Fault Code: {fault}")
        seq=recursive_trace(fault)
        print(f"Final Sequence: {seq}")
        print(f"\nFINAL OUTPUT: Avg={avg:.2f}, Status={status}, Fault Trace={seq}")

if __name__=="__main__":
    main()