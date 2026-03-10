import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def MarvellousPredictor():

    border = "-"*60

    #--------------------------------------------------------------------
    # Step 1 : Load the data/Get the data
    #--------------------------------------------------------------------

    print(border)
    print("Step 1 : Load the data/Get the data")
    print(border)

    df = pd.read_csv("WinePredictor.csv")

    print("Few records from the dataset : ")
    print(df.head())

    #--------------------------------------------------------------------
    # Step 2 : Clean,Prepare & Manipulate the data
    #--------------------------------------------------------------------

    print(border)
    print("Step 2 : Clean,Prepare & Manipulate the data")
    print(border)

    print(border)
    print("Cleaning the data by removing empty rows")
    print(border)

    df.dropna(inplace=True)

    print("Total records : ",df.shape[0])
    print("Total columns : ",df.shape[1])

    print(border)
    print("Separating the data into dependent & independent variables")
    print(border)

    X = df.drop(columns=['Class'])
    Y = df['Class']

    print("Shape of Independent Variables : ",X.shape)
    print("Shape of Dependent Variables : ",Y.shape)

    print(border)
    print("Spliting data for training & testing")
    print(border)

    X_train , X_test , Y_train , Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)

    print(border)
    print("Information of training & testing : ")
    print("X_train shape : ",X_train.shape)
    print("X_test shape : ",X_test.shape)
    print("Y_train shape : ",Y_train.shape)
    print("Y_test shape : ",Y_test.shape)
    print(border)

    print(border)
    print("Feature Scalling")
    print(border)

    scalar = StandardScaler()

    X_trained_Scaled = scalar.fit_transform(X_train)
    X_test_scaled = scalar.fit_transform(X_test)

    print("Feature scaling is done")

    print(border)
    print("Exploring multiple values of k (Hyper parameter tunning)")
    print(border)

    accuracy_scores = []

    K_values = range(1,21)

    for k in K_values:
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_trained_Scaled,Y_train)
        Y_pred = model.predict(X_test_scaled)
        accuracy = accuracy_score(Y_test,Y_pred)

        accuracy_scores.append(accuracy)

    for values in accuracy_scores:
        print(values)
    print(border)

    print(border)
    print("Finding best value of k : ")

    best_k = list(K_values)[accuracy_scores.index(max(accuracy_scores))]

    print("Best value of K is : ",best_k)

    #--------------------------------------------------------------------
    # Step 3 : Train the data
    #--------------------------------------------------------------------

    print(border)
    print("Step 3 : Train the data")
    print(border)

    final_model = KNeighborsClassifier(n_neighbors = best_k)

    final_model.fit(X_trained_Scaled,Y_train)

    #--------------------------------------------------------------------
    # Step  : Test the data & find the accuracy
    #--------------------------------------------------------------------

    print(border)
    print("Step  : Test the data")
    print(border)

    Y_pred = final_model.predict(X_test_scaled)

    accuracy = accuracy_score(Y_test,Y_pred)

    print("Final accuracy of the data is : ",accuracy*100)

def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()