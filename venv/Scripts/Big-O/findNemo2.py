# Version#2 of nemo
# 
import time

# Arrays (lists in Python)
nemo = ['nemo']
everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla', 'hank']
large = ['nemo'] * 1000  # Create a 100 Elements list and fill with 'nemo'

def find_nemo(array):
    # Start Time
    t0 = time.perf_counter()
    for item in array:
        if item == 'nemo':
            print('Found NEMO!')
    # End Time
    t1 = time.perf_counter()
    print(f"Call to find Nemo took {(t1 - t0) * 1000:.4f} milliseconds.")

# find_nemo(nemo)
# find_nemo(everyone)
find_nemo(large)