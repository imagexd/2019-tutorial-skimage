from skimage import measure
def getLargestCC(segments):
        '''Return a mask corresponding to the largest object'''
        labels = measure.label(segments)
        largestCC = labels == np.argmax(np.bincount(labels.flat, weights=segments.flat))
        return largestCC

a=getLargestCC(relabeled)
plt.imshow(a[30,:,:])
