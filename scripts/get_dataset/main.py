import os
from DatasetGenerator import Dataset

def main():
    dataset = Dataset('/Users/teguhsatya/Dev/T/dataset/HRF/images',
            '/Users/teguhsatya/Dev/T/dataset/DrishtiGS',
            '/Users/teguhsatya/Dev/T/dataset/RIMONE/partitioned_by_hospital')
    cwd =  os.getcwd()
    dataset.create_dataset('/Users/teguhsatya/Dev/segeralulus')

if __name__ == '__main__':
    main()
