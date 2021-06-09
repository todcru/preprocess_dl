Preprocessing Text Python Package

This python package is a collaborative work of Aswin and Karthik. All rights resereved.

Dependencies

pip install spacy==2.2.3
python -m spacy download en_core_web_sm
pip install beautifulsoup4==4.9.1
pip install textblob==0.15.3

How to use it for preprocessing
You have to have installed spacy and python3 to make it work.
1. Acquire the dataset
Use open data. These are easily accessible and available to use, typically online.
Create a custom data set. You can build your own data set using your own resources or services you hire. 
Partner with a third party to create data sets.

2. Import all the crucial libraries
Create a Python file containing the required functions.
Create another Python file and import the previous Python file into it.
Call the functions defined in the imported file.

3. Import the dataset
If needed, select your dataset from list on the Datasets page to open its Import tab.
Choose the import source for your data: BigQuery, Cloud Storage, or your local computer. Provide the information required.
Click Import to start the import process.

4. Identifying and handling the missing values
Ignore the data row.
Use a global constant to fill in for missing values.
Use attribute mean.
Use attribute mean for all samples belonging to the same class.
Use a data mining algorithm to predict the most probable value.

5. Encoding the categorical data
Categorical data must be encoded to numbers before we can use it to fit and evaluate a model. There are many ways to encode categorical variables for modeling, although the three most common are as follows: Integer Encoding: Where each unique label is mapped to an integer.

6. Splitting the dataset
Splitting your dataset is essential for an unbiased evaluation of prediction performance. In most cases, it's enough to split your dataset randomly into three subsets: The training set is applied to train, or fit, your model.

7. Feature scaling
Feature Scaling is a technique to standardize the independent features present in the data in a fixed range. It is performed during the data pre-processing to handle highly varying magnitudes or values or units.
