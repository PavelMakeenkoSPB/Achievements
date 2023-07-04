import filecmp
import os

a = filecmp.cmp('Sample.jpg', 'Sample.tiff')
if a is True:
    os.remove('Sample.tiff')
