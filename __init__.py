import hmac,base64,struct,hashlib,time
def Authenticator(code):
    intervals_no=int(time.time())//30
    key=base64.b32decode(code,True)
    msg=struct.pack(">Q",intervals_no)
    h=hmac.new(key,msg,hashlib.sha1).digest()
    o=h[19]&15
    h=(struct.unpack(">I",h[o:o+4])[0]&0x7fffffff)%1000000
    return h
auth=''
code=Authenticator(auth)
