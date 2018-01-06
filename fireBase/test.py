import firebaseServer as fs

def myfunction(msg):
    #print "recv msg : " + msg
    if msg[:3] == "git":
        print "git"
        '''
        implement git command
        '''
    if msg[:4] == "auto":
        print "auto"
        '''
        implement auto command
        '''
    if msg[:8] == "dataStop":
        print "stop"
        '''
        implement auto command
        '''
    
    if msg[:3] == "pre":
        print "pre"
        '''
        implement pre command
        '''
    
    if msg[:7] == "forward":
        print "forward"
        '''
        implement forward command
        '''
    '''
    user implement
    '''
#firebase init by user
firebase = fs.firebaseServer(8765)
fs.msgCon = myfunction;

for i in range(25):
    url = raw_input("input url : ");
    print(firebase.get(url))
    #val = raw_input("input val : ");
    #firebase.update(url, val);
    #firebase.update("/test/"+str(i), i*i+i);
