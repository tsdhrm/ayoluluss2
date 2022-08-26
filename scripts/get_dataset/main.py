from DatasetGenerator import Dataset

def main():
    TARGET_DIR = '/Users/teguhsatya/Dev/segeralulus'
    ALL_DATASET = {
            'HRF': '/Users/teguhsatya/Dev/T/dataset/HRF/images',
            'DGS': '/Users/teguhsatya/Dev/T/dataset/DrishtiGS',
            'RM': '/Users/teguhsatya/Dev/T/dataset/RIMONE/partitioned_by_hospital'
            }
    dataset = Dataset(TARGET_DIR, ALL_DATASET)
    dataset.create_dataset()


if __name__ == '__main__':
    main()
