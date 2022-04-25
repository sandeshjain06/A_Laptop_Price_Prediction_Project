# Laptop_Price_Prediction_Project

Objective - Customer can check the laptop price by entering the laptop specification , the model can predict price for different laptops with different specifications.

Click here to check the dataset - https://github.com/sandeshjain06/Laptop_price_predict_project/blob/main/laptop_data.csv

Click here to check the website hosted on heroku - https://laptop--price-predictor.herokuapp.com/


Screenshot of the website 

![image](https://user-images.githubusercontent.com/91243691/164948028-f1595989-0b17-4eac-8750-3e13c1bfa29b.png)

![image](https://user-images.githubusercontent.com/91243691/164949093-53f09d98-9afb-4387-bbdd-e2b2fdc54400.png)


Step 1 :

- Dataset consists of (1303, 11) .

- Features are ['Company', 'TypeName', 'Inches', 'ScreenResolution', 'Cpu', 'Ram','Memory', 'Gpu', 'OpSys', 'Weight', 'Price']

- All features are required to predict the laptop prices.

- In the output we want all the features , thus we have to perform EDA and check the null values , duplicated values and datatypes of all features.

- Convert the features (ram , weight) into integer datatype as it is in form of object datatype.

- In Screen ScreenResolution , we have multiple options such as whether laptop has touchscreen , IPS Panel , X-resolution and Y_resolution, so separate the values into different features.

- New features will be added such as touchscreen , IPS Panel , X_resolution , Y_resolution . 

- 
























