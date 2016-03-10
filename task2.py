import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import scipy.linalg as sp

img=mpimg.imread('photo.tiff')
[r,g,b] = [img[:,:,i] for i in range(3)]

plt.imshow(img)
plt.show()
plt.imshow(r, cmap = 'Reds')
plt.show()
plt.imshow(g, cmap = 'Greens')
plt.show()
plt.imshow(b, cmap = 'Blues')
plt.show()

red = {'Index' : 0,'Mat': r, 'Color' : 'Reds'}
green = {'Index' : 1, 'Mat': g, 'Color' : 'Greens'}
blue = {'Index' : 2, 'Mat': b, 'Color' : 'Blues'}
rgb = [red,green,blue]

for color in rgb:
    
    # SVD decomposition of img
    U,s,V = sp.svd(color['Mat'])
    
    S = np.zeros(color['Mat'].shape,s.dtype)
    
    for i in range(s.size):
        S[i][i] = s[i]
        
    color['U'] = U
    color['eigenval'] = s
    color['S'] = S
    color['V'] = V
    
new_photo = np.zeros_like(img)

for dimension in (30, 200):
    for color in rgb:
        S_new = np.zeros(color['Mat'].shape,s.dtype)
        
        for i in range(dimension):
            S_new[i][i] = color['eigenval'][i]
            
        new_photo[:,:,color['Index']]= np.dot(np.dot(color['U'],S_new),color['V'])
    plt.imshow(new_photo)
    plt.show()
    
