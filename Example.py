# Import library
from Integration.JagaAksara import JagaAksara

# BEFORE FLASK

# Config
# The model folder is where the model to be used is located
ai = JagaAksara('Models')


# INSIDE OCR HANDLER FLASK

# First save the image obtained from the http request
# do ocr with the image path input
text = ai.ocr('hello.png')