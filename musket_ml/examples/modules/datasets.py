from musket_core import datasets,genericcsv,coders,image_datasets, preprocessing, context
from numpy import ndarray
import numpy as np

@datasets.dataset_provider(origin="train.csv",kind="GenericDataSet")
def getTitanic():
    return genericcsv.GenericCSVDataSet("train.csv",["Sex","Fare","Age","Pclass"],["Survived"],[],
                                        {"Sex":"binary","Fare":"normalized_number","Age":"normalized_number","Pclass":"multi_class","Survived":"binary"},input_groups={"0":["Sex","Fare","Age","Pclass"]})
    
@datasets.dataset_provider(origin="saltExists.csv",kind="BinaryClassificationDataSet")
def getSe():
    return image_datasets.BinaryClassificationDataSet(["images"],"saltExists.csv","ImageId","Class")


@datasets.dataset_provider(origin="train.csv",kind="BinarySegmentationDataSet")
def getSaltTrain():
    return image_datasets.BinarySegmentationDataSet(["images","images"],"salt.csv","id","rle_mask")    

# We create separate dataset for the siamic network - with 2 outputs
class Questions2Outputs(datasets.DataSet):
    
    def __init__(self):
        self.data = context.csv_from_data('questions.csv')
        self.q1 = self.data['question1'].values
        self.q2 = self.data['question2'].values
        self.target = self.data['is_duplicate'].values
        
    def __len__(self):
        return len(self.data)
    
    def get_questions(self, item):
        return [str(self.q1[item]),str(self.q2[item])]
    
    def __getitem__(self, item):
        return datasets.PredictionItem(item, self.get_questions(item), np.array([self.target[item]]))

@datasets.dataset_provider(origin="questions.csv",kind="")
def get_train_siamic():
    return Questions2Outputs()