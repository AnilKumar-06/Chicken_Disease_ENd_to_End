import time
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
from ChickenDisease.entity.entity_config import CallbacksConfig
import os

class PrepareCallback:
    def __init__(self, config:CallbacksConfig):
        self.config = config
       # print(config)
    @property
    def create_tb_callback(self):
        timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
        tb_running_log_dir = os.path.join(self.config.tensorboard_root_log_dir,
                                          f"tb_logs_at_{timestamp}",)
        return tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)
    
    @property
    def ckpt_callback(self):
        return tf.keras.callbacks.ModelCheckpoint(
            filepath=self.config.checkpoint_model_filepath,
            save_best_only=True
        )
        
    
    def get_tb_ckpt_callbacks(self):
        return [
            self.create_tb_callback,
            self.ckpt_callback
        ]
