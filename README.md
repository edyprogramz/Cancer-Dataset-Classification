## CANCER CLASSIFICATION PROJECT
*SVM*

- can be used for both classifications & regression

###  Attributes
['mean radius' 'mean texture' 'mean perimeter' 'mean area'
 'mean smoothness' 'mean compactness' 'mean concavity'
 'mean concave points' 'mean symmetry' 'mean fractal dimension'
 'radius error' 'texture error' 'perimeter error' 'area error'
 'smoothness error' 'compactness error' 'concavity error'
 'concave points error' 'symmetry error' 'fractal dimension error'
 'worst radius' 'worst texture' 'worst perimeter' 'worst area'
 'worst smoothness' 'worst compactness' 'worst concavity'
 'worst concave points' 'worst symmetry' 'worst fractal dimension']

###  Label / The prediction
- classes = ['malignant', 'benign']

### Requirements
<!-- 1. pandas
   
    ```python import pandas as pd ```

2. Numpy
   
    ```python import numpy as np ``` -->


1. sklearn
   
    ```python 
    import sklearn 
    from sklearn import datasets
    from sklearn import svm
    ```
## HOW SUPPORT VECTOR MACHINES works!!!

- SVM create a hyperplane, that divides your data

## CASE 1:

![Web capture_20-6-2023_10430_www youtube com](https://github.com/edyprogramz/Cancer-Dataset-Classification/assets/116636391/b779ac6a-37b7-4d03-9174-32a5dd8e2fd5)

- The hyperplane is the same distance from the two closest data points from both classes (red & green) in this case.

<a id="a-item"></a>
a. ![Web capture_20-6-2023_104740_www youtube com](https://github.com/edyprogramz/Cancer-Dataset-Classification/assets/116636391/69538d9c-ad85-4b4f-ae07-2773c0ccd9de)

NOTE: Meaning we could generate multiple hyperplanes eg;

b. ![Web capture_20-6-2023_10505_www youtube com](https://github.com/edyprogramz/Cancer-Dataset-Classification/assets/116636391/8498a5a8-c6fd-42c5-96a5-33c89bea7b3e)

c. ![Web capture_20-6-2023_105148_www youtube com](https://github.com/edyprogramz/Cancer-Dataset-Classification/assets/116636391/a5e9b043-2fc2-4670-9870-9a9685f06b82)

- The best hyperplane to use is the one where the distance between our classes is the greatest. In our case The best to use is [a.](#a-item).

## CASE 2:

- if we get this type of data what happens? **kernel trick**

![Web capture_20-6-2023_11116_www youtube com](https://github.com/edyprogramz/Cancer-Dataset-Classification/assets/116636391/ec394fc5-86e9-481f-9b04-f6b19e1ef390)

- In this case we use **kernel trick**

- Kernel, simply take the x1's and x2 of each data point and comes up with an x3. For 3D

![Web capture_20-6-2023_111853_www youtube com](https://github.com/edyprogramz/Cancer-Dataset-Classification/assets/116636391/dc0fd092-cc4e-449e-aad3-2050ccfab418)

![Web capture_20-6-2023_112012_www youtube com](https://github.com/edyprogramz/Cancer-Dataset-Classification/assets/116636391/89480f9d-e213-4cee-87df-87f85269e248)

- This shows how a 2D is converted to a 3D.

![Web capture_20-6-2023_112246_www youtube com](https://github.com/edyprogramz/Cancer-Dataset-Classification/assets/116636391/da7fcaa9-72ec-4241-8604-56683a9c6c04)

## CASE 3:

- Using a soft margin

![Web capture_20-6-2023_112813_www youtube com](https://github.com/edyprogramz/Cancer-Dataset-Classification/assets/116636391/f2890d4e-f5b6-4185-813b-603ea42a56ca)

- If this occurs like in our case where by a RED DATA POINT has strayed. We ignore it to get a better result.

- a few points maybe ignored

![Web capture_20-6-2023_11318_www youtube com](https://github.com/edyprogramz/Cancer-Dataset-Classification/assets/116636391/726d2eb7-72ec-4f1e-90d7-8304763a9743)

NOTE: In a hard margin this is not allowed.


