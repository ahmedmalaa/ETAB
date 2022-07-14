import config
from etab.utils.ETAB_data_loaders import *
from etab.utils.callbacks import *

available_datasets = ["EchoNet", "CAMUS", "TMED"]

class echocardiography_dataset:
    
    """
    Generic class with common functionalities for echo data sets 
    
    """
    
    def __init__(self,
                 name="echonet",
                 target_type="EF",
                 view="A4CH",
                 video=False,
                 normalize=True,
                 length=16, 
                 period=2,
                 max_length=250,
                 padding=None):
        
        self.name        = name
        self.target_type = target_type
        self.view        = view
        self.video       = video
        self.normalize   = normalize
        self.length      = length
        self.period      = period
        self.max_length  = max_length
        self.padding     = padding
        
        
    def load_data(self, **kwargs):
        
        """
        
        ** Generic function for loading echo data sets **
        
        :param n_clips: Number of distinct echocardiography clips to be loaded 
        
        """    
        
        self.data          = load_ETAB_dataset(dataset_type=config.dataset_names[self.name], 
                                               echo_view=self.view, 
                                               label_type=config.task_targets[self.target_type])
        

        
class echonet(echocardiography_dataset):
    
    
    """
    The EchoNet dataset, introduced in [1, 2], comprises one apical-4 chamber (AP4CH) 2D gray-scale video is extracted from each echo study. 
    A total of 10,036 videos are collected from 10,036 distinct individuals who underwent echocardiography between 2006 and 2018 as part of 
    routine care at a University Hospital. Individuals in the data set were selected at random from hospital records cardiac function assessments 
    and calculations obtained by a registered sonographer and verified by a level-3 echocardiographer are provided. 
    
    Data is accessible via: https://echonet.github.io/echoNet/.
    
    The "echonet" class is part of the etab.datasets module and contains the functionalities required for loading and processing the EchoNet data set.

    
    References:
    -----------
    
    [1] David Ouyang, Bryan He, Amirata Ghorbani, Matt P Lungren, Euan A Ashley, David H Liang, and James Y Zou. 
        Echonet-dynamic: a large new cardiac motion video data resource for medical machine learning. 
        In NeurIPS ML4H Workshop: Vancouver, BC, Canada, 2019.
        
    [2] David Ouyang, Bryan He, Amirata Ghorbani, Neal Yuan, Joseph Ebinger, Curtis P Langlotz, Paul A Heidenreich, Robert A Harrington, 
        David H Liang, Euan A Ashley, et al. Video-based AI for beat-to-beat assessment of cardiac function. Nature, 580(7802):252–256, 2020.

    """
    
    def __init__(self, root=None, name="echonet", view="A4CH"):
        
        self.name     = "echonet" 

        super().__init__()

        if root is None:
            
            self.root = config.echonet_dir
            
        else:
            
            self.root = root
                       