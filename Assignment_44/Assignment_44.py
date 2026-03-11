import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error , r2_score
from sklearn.model_selection import train_test_split

def MarvellousAdvertising():
    border = "-"*60

    #-----------------------------------------------------------------
    # Step 1 : Load the data
    #-----------------------------------------------------------------

    print(border)
    print("Step 1 : Load the data")
    print(border)

    df = pd.read_csv("Advertising.csv")

    print("Few records from the dataset")
    print(df.head())

    #-----------------------------------------------------------------
    # Step 2 : Clean,Prepare Manipulate the data
    #-----------------------------------------------------------------

    print(border)
    print("Step 2 : Clean,Prepare Manipulate the data")
    print(border)
    
    print(border)
    print("Cleaning the dataset by removing the unwanted columns")
    print(border)

    print("Shape before cleaning : ",df.shape)

    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'],inplace=True)

    print("Shape after cleaning : ",df.shape)

    print(border)
    print("Data after cleaning is : ")
    print(df.head())
    print(border)

    print(border)
    print("Checking misssing values : ")
    print(df.isnull().sum())
    print(border)

    print(border)
    print("Displaying statistical summary")
    print(df.describe())
    print(border)

    print(border)
    print("Displaying correlation between the columns ")
    print(df.corr())
    print(border)

    print(border)
    print("Splitting data into independent & dependent variables")

    X = df[['TV' , 'radio' , 'newspaper']]
    Y = df['sales']
    print(border)

    print("Shape of the Independent varaibles : ",X.shape)
    print("Shape of the Dependent varaibles : ",Y.shape)

    print(border)
    print("Splitting data for training & testing ")

    X_train , X_test , Y_train , Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    print(border)

    print("X_train shape : ",X_train.shape)
    print("X_test shape : ",X_test.shape)
    print("Y_train shape : ",Y_train.shape)
    print("Y_test shape : ",Y_test.shape)

    print(border)

    #-----------------------------------------------------------------
    # Step 3 : Create & train the data
    #-----------------------------------------------------------------

    print(border)
    print("Step 3 : Create & train the data")
    print(border)

    model = LinearRegression()

    model.fit(X_train , Y_train)

    #-----------------------------------------------------------------
    # Step 4 : Test the data
    #-----------------------------------------------------------------

    print(border)
    print("Step 4 : Test the data")
    print(border)
    
    Y_pred = model.predict(X_test)

    #-----------------------------------------------------------------
    # Step 4 : Evaluating the data
    #-----------------------------------------------------------------

    print(border)
    print("Step 4 : Evaluating the data")
    print(border)

    MSE = mean_squared_error(Y_test,Y_pred)
    RMSE = np.sqrt(MSE)
    r2 = r2_score(Y_test,Y_pred)

    print("Mean sqaured error : ",MSE)
    print("Root mean squared error : ",RMSE)
    print("Rsquare value : ",r2)

    #-----------------------------------------------------------------
    # Step 5 : Comparing actual v/s predicted data
    #-----------------------------------------------------------------

    print(border)
    print("Step 5 : Comparing actual v/s predicted data")
    print(border)

    Result = pd.DataFrame({'Actual sales  ' : Y_test.values ,'Predictes sales ': Y_pred})

    print(df.head(10))

def main():
    MarvellousAdvertising()

if __name__ == "__main__":
    main()

    