def degree_rank(a):
    result=0
    if 'ssc' in ' '.join(a):
        result=1
    elif 'hsc' in ' '.join(a):
        result=2
    elif 'bsc' in ' '.join(a):
        result=3
    elif 'msc' in ' '.join(a):
        result=4
    elif 'phd' in ' '.join(a):
        result=5
    return result

