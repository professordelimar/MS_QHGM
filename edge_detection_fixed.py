import numpy as np

eps = np.finfo(float).eps

def normalize01(a):
    a = np.asarray(a, dtype=float)
    amin = np.nanmin(a)
    amax = np.nanmax(a)
    return ((a-amin)/(amax-amin+eps))

def otsu_threshold(data, nbins=256):  
    '''
    Automatic Otsu threshold computed only from the
    filter-response distribution.
    '''
    values = np.asarray(data, dtype=float)
    values = values[np.isfinite(values)]
    hist, bin_edges = np.histogram(values,bins=nbins,range=(0.0, 1.0))    
    hist = hist.astype(float)    
    probability = hist / np.sum(hist)
    bin_centers = 0.5*(bin_edges[:-1]+bin_edges[1:])
    omega = np.cumsum(probability)    
    mu = np.cumsum(probability * bin_centers)    
    mu_total = mu[-1]    
    sigma_b2 = ((mu_total*omega-mu)**2/(omega*(1.0-omega)+eps))
    idx = np.nanargmax(sigma_b2)    
    return bin_centers[idx]

def detect_edge_ridges(response,border=4,nbins=256):
    # Normalize response
    R = normalize01(response)
    # Automatic Otsu threshold
    threshold = otsu_threshold(R,nbins=nbins)
    # Local maxima along x
    maxima_x = np.zeros_like(R,dtype=bool)    
    maxima_x[:, 1:-1] = ((R[:, 1:-1] >= R[:, :-2]) & (R[:, 1:-1] >  R[:, 2:]))
    # Local maxima along y    
    maxima_y = np.zeros_like(R,dtype=bool)    
    maxima_y[1:-1, :] = ((R[1:-1, :] >= R[:-2, :]) & (R[1:-1, :] >  R[2:, :]))
    # Candidate ridge = maximum in either direction
    ridge_candidates = (maxima_x | maxima_y)  
    # Threshold candidates
    ridges = (ridge_candidates & (R >= threshold))
    # Remove outer four grid cells  
    if border > 0:        
        ridges[:border, :] = False
        ridges[-border:, :] = False
        ridges[:, :border] = False
        ridges[:, -border:] = False    
    return R, threshold, ridges
