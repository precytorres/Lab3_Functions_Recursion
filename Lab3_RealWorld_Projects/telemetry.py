LAST_NAME="TORRES"; SEED_NUM=4; FAVORITE_ARTIST="POST MALONE"
def sensor_stream():
    base=len(LAST_NAME)+SEED_NUM+len(FAVORITE_ARTIST) # 21
    for i in range(9):
        if i==3: yield -999
        else: yield base + i*3