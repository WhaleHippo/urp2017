import firebaseServer as fs

firebase = fs.firebaseServer(8765)

while True:
    url = raw_input("input url : ");
    val = raw_input("input url : ");
    firebase.callback(url);
