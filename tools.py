# basic tools for doing ml

def normalize_1d_data(data, range_func=None):
    if range_func:
        r = float(range_func(data))
    else:
        r = max(data) - min(data)
    mean = sum(data) / float(len(data))
    
    return [(item - mean) / r for item in data]
    

