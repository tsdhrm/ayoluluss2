import os
import shutil

class Dataset:
    def __init__(self, hrf_dir:str, dgs_dir:str, rm_dir:str)->None:
        self.HRF_DIR = hrf_dir
        self.DGS_DIR = dgs_dir
        self.RM_DIR = rm_dir


    def create_dataset(self, dst:str)->None:
        self.DST_DIR = dst
        if os.path.exists(os.path.join(self.DST_DIR, 'Dataset')):
            shutil.rmtree(os.path.join(self.DST_DIR, 'Dataset'))
        os.mkdir(os.path.join(self.DST_DIR, 'Dataset'))

        print(f'Creating dataset at {dst}')

        hrf = CreateHRF(self.HRF_DIR, self.DST_DIR)


class CreateHRF:
    def __init__(self, hrfdir:str, dstdir:str) -> None:
        self.code = 'D1'
        self.labels = ('g', 'h')
        print('Generating HRF Dataset...')

        for label in self.labels:
            idx = 1
            for file in os.listdir(hrfdir):
                if file[-5] == label:
                    format = file[-3:]
                    old_file_name = os.path.join(hrfdir, file)
                    new_file_name = os.path.join(os.path.join(dstdir, 'Dataset'),
                        f'{self.code}_{idx}.{format}')
                    shutil.copyfile(old_file_name, new_file_name)
                    idx += 1
            break




