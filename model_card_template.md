# Model Card

## Model Details

Model Created by: Corbin Spargo
Model Date: 4/14/2025
Model Type: Random Forrest Classifier
Additional Information: Model was created as part of a class project.
Features: Machine learning pipeline, performance evaluation using precision, F1 score, recall and various functions used in model inferennce and serialization.

## Intended Use

It is intended to use relevant demographic data to determine a person's income level, "<=50k" or ">50k".
The audience usage is for students/academic purposes only.

## Training Data

Dataset used: Census.csv which is an extraction was done by Barry Becker from the 1994 Census database.The set included 14 features and 48,842 instances. Data types included numeric, string, and boolean types.

## Evaluation Data

The data was split into a training dataset and a test dataset. The test dataset split was 20% of the overall dataset.

## Metrics

Metrics used for measurement are Precision, Recall, and F1 scores.

- Precision: 0.7453
- Recall: 0.6353
- F1: 0.6859

## Ethical Considerations

As data collection method is unclear, biases towards population groups may be present.

## Caveats and Recommendations

As the origins and collection methods of the data are unclear, this model and its associated dataset should be viewed purely as a theoretical exercise rather than as factual or authoritative. It is intended to serve as a demonstration of the potential functionality of an ML Classifier.
