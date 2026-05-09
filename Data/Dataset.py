import kagglehub
import os
path=kagglehub.dataset_download("abcsds/pokemon")
print("The path of the dataset from the kaggle is: ", path)
path_csv=os.path.join(path, "pokemon.csv")
print(path_csv)