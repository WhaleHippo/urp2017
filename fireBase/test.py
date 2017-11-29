import firebaseServer as fs

firebase = fs.firebaseServer(8765)

while True:
    val = raw_input("input : ");
    firebase.update("/hanzo",val);
    firebase.remove(val);
