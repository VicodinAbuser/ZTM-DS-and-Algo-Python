import time

nemo = ['nemo']
everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla']
def find_nemo(array):
    t0 = time.time()
    for i in range(0,len(nemo)):
        if array[i] == 'nemo':
            print("Found Nemo!!")
    t1 = time.time()
    print(f'The search took {t1-t0} seconds.')
find_nemo(nemo)
find_nemo(everyone)
