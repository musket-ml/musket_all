from musket_core import datasets,genericcsv,coders

@datasets.dataset_provider(origin="train.csv",kind="GenericDataSet")
def getTitanic():
    return genericcsv.GenericCSVDataSet("train.csv",["Sex","Fare","Age","Pclass"],["Survived"],[],
                                        {"Sex":"binary","Fare":"normalized_number","Age":"normalized_number","Pclass":"one_hot","Survived":"binary"},input_groups={"0":["Sex","Fare","Age","Pclass"]})