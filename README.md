# DataRobot TasK:
Data description:

Data Source: Kaggle Digit Competition(https://www.kaggle.com/c/digit-recognizer)
The data were taken from the MNIST dataset. The MNIST ("Modified National Institute of Standards and Technology") dataset is a classic within the Machine Learning community that has been extensively studied.  More detail about the dataset, including Machine Learning algorithms that have been tried on it and their levels of success, can be found at http://yann.lecun.com/exdb/mnist/index.html.

Data details:
The data files train.csv and test.csv contain gray-scale images of hand-drawn digits, from zero through nine.

Each image is 28 pixels in height and 28 pixels in width, for a total of 784 pixels in total. Each pixel has a single pixel-value associated with it, indicating the lightness or darkness of that pixel, with higher numbers meaning darker. This pixel-value is an integer between 0 and 255, inclusive.

The training data set, (train.csv), has 785 columns. The first column, called "label", is the digit that was drawn by the user. The rest of the columns contain the pixel-values of the associated image.

Python Script: Get the predictions result from Google API prediction

Before that:
1 Greated a DataRobot project on Google Developer Consoles and upload a training data into buckets(Got project ID)
2 Used Google API prediction to train the model(Got model ID)
3 Greated client credentials and got the json file

Code schema:
1 Open JASON file to get client_email and private key
2 Since only Prediction API is used, SignedJwtAssertionCredentials Class is used to create credentials using 1
3 Authorize the credential by using authorize method
4 Call Google API prediction
  4.1 Build a prediction service by using build method
  4.2 make request to prediction service using prediction.trainedmodels().predict method(need to imput model ID and project ID)
5 get the prediction result by output label



