import  pandas as pd
dl = pd.read_csv("winequalityRED.csv")
dl.info()

#check for null values
dl.isnull().sum()
print(dl[dl["chlorides"].isnull()].index.to_list)

#replace missing values with mean value
mean_density = dl["density"].mean()
mean_ch = dl["chlorides"].mean()
print("density " ,mean_density)
print("density ", mean_ch)

dl["density"].fillna(value = mean_density , inplace=True )
dl["chlorides"].fillna(value = mean_ch , inplace=True )
dl.isnull().sum()

dl.to_csv("clean_data.csv")

dl = pd.read_csv("clean_data.csv")
dl.info()


