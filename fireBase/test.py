import firebaseServer as fs

firebase = fs.firebaseServer(8765)

url = raw_input("input callback url : ");
firebase.callback(url);
while True:
    url = raw_input("input url : ");
    val = raw_input("input val : ");
    firebase.update(url, val);
