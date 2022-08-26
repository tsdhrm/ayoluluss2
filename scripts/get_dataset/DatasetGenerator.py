import os
import shutil
import re

class Dataset:
    def __init__(self, targetdir:str, datasetdir:str)->None:
        self.TARGET_DIR = targetdir
        self.DATASET_DIR = datasetdir
        self.LABELS = {'HRF':'D1',
                'DGS':'D2',
                'RIMONE':'D3'}

    def create_folders(self)->None:
        dataset_dir = os.path.join(self.TARGET_DIR, 'Dataset')
        print(f'Creating new directory at {dataset_dir}')
        if os.path.exists(dataset_dir):
            shutil.rmtree(dataset_dir)
        self.POSITIVE_DIR = os.path.join(dataset_dir, 'Positive')
        self.NEGATIVE_DIR = os.path.join(dataset_dir, 'Negative')
        self.TARGET_DIR = dataset_dir
        os.makedirs(self.POSITIVE_DIR)
        os.makedirs(self.NEGATIVE_DIR)

    def create_dataset(self)->None:
        self.create_folders()
        for data in self.DATASET_DIR:
            if data == 'HRF':
                self.select_hrf(data)
            else:
                self.select_dgsrm()

    def select_hrf(self, data)->None:
        regexcompiler = re.compile('[._]')
        expected_label = ['g', 'h']
        posneg = [self.POSITIVE_DIR, self.NEGATIVE_DIR]
        for j in range(0, len(expected_label)):
            i = 0
            for file in  os.listdir(self.DATASET_DIR[data]):
                filename, file_label, fileformat = regexcompiler.split(file)
                filename = f'{self.LABELS[data]}_{i+1}_{file_label}.{fileformat}'
                if file_label == expected_label[j]:
                    shutil.copyfile(src=os
                            .path
                            .join(self.DATASET_DIR[data], file),
                            dst=os
                            .path
                            .join(posneg[j], filename))
                    i+=1

    def select_dgsrm(self):
        print('Hello world!')
