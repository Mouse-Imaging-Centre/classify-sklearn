# the standard setup.py that assumes that the C code has already been generated

from distutils.core import setup
from distutils.extension import Extension

setup(
    name = "classify-sklearn",
    version = "0.1",
    description = "MINC wrapper for classification using scikit-learn",
    author = "Jason Lerch",
    author_email = 'jason.lerch@utoronto.ca',
    url = 'https://github.com/Mouse-Imaging-Centre/classify-sklearn',
    scripts = ["classify_sklearn_predict", "classify_sklearn_fit", "classify_sklearn_unsupervised"]
)
