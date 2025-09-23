% Load your trained deep learning network
load('trainedNet.mat');  % assumes your network is saved as 'trainedNet'

% Load or prepare input data for classification
% Example: load image data or feature matrix
inputData = imread('testImage.jpg');  % for image classification

% Preprocess the input if needed (resize, normalize, etc.)
inputData = imresize(inputData, [224 224]);  % resize to match network input size

% Classify the input using the trained network
predictedLabel = classify(trainedNet, inputData);

% Display the result
disp(['Predicted class: ', char(predictedLabel)]);