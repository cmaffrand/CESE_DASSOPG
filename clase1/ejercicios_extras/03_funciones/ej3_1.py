def hms2s(h,m,s):
    return s+m*60+h*60*60

def s2hms(s):
    r = []
    r.append(int(s/60/60))
    r.append(int((s-r[0]*60*60)/60))
    r.append(int(s-r[0]*60*60-r[1]*60))
    return r