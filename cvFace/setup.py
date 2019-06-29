print("Going to install...")
from distutils.core import setup
print("Imported setup tool...")
setup(name="cvFace",
      version='1.0',
      packages=['cvFace'],
      author="Kendell R.",
      author_email="ejrejr@hotmail.com",
      license="MIT",
      description="A wrapper for OpenCV's face dectection and recogniton.",
      download_url="https://github.com/family-richards/opencvFace",
      url="https://github.com/family-richards/opencvFace")
print("Package installed!")
