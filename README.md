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

- New features will be added such as touchscreen , IPS Panel , X_resolution , Y_resolution from the ScreenResolution.                                                   
-  PPI is the new features added , formula would be -  (X_res *2 + Y_res) * 1/2  / Inches

- PPI (pixel per Inch)  - df['ppi']= (((df['X_res']**2) + (df['Y_res']**2)) ** 0.5 / df['Inches']).astype('float')

- From CPU features , take only the required details such as whether the CPU is i5,i3 or i7 processor , so apply split on the features.

![image](https://user-images.githubusercontent.com/91243691/165017431-fd5fe511-91e3-4184-8e8e-c7e7db51d82e.png)

- df['Cpu_name']=df['Cpu'].apply(lambda x : " ".join(x.split()[0:3]))






- Ops features contains multiple values 

![image](https://user-images.githubusercontent.com/91243691/165017607-d5974005-51a5-4392-a829-73a7cfc336f1.png)

def fetch_OperatingSys(text):
    if text == 'Windows 10' or text == 'Windows 7' or text == 'Windows 10 S' :
        return 'Windows'
    elif text == 'macOS' or text == 'Mac OS X':
        return 'mac'
    else:
        return 'Others'
        
        
- df['OpSys'] = df['OpSys'].apply(fetch_OperatingSys)  - Apply function to return only 3 values .


- The Final df 

![image](https://user-images.githubusercontent.com/91243691/165017735-6e8f0f7b-85ea-4d46-8c0a-796b61a2615d.png)


























