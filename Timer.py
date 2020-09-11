import time
import pandas as pd
from uuid import uuid4
import os

# %% Timer Class for Execution Time

class Timer():
    
    start_time = None
    end_time = None
    time_storage = []
    timer_count = 0
    output_directory = None
    
    def __init__(self):
        pass
    
    
    @classmethod
    def add_output_directory(cls, dir_path):
        cls.output_directory = dir_path
    
    @classmethod
    def start_timer(cls):
        cls.start_time = time.time()
    
    @classmethod
    def end_timer(cls):
        cls.end_time = time.time()
    
    @classmethod
    def display_time(cls, description = ''):
        if cls.start_time == None or cls.end_time == None:
            pass
        else:
            print(f'{description} Time Elapsed: {cls.end_time - cls.start_time}')
            cls._store_timer_data(description)
            
    @classmethod
    def _store_timer_data(cls, description = ''):
        timer_data = {'ID':cls.timer_count,
                      'Description': description,
                      'Start_Time': cls.start_time,
                      'End_Time': cls.end_time,
                      'Duration': cls.end_time - cls.start_time}
        cls.time_storage.append(timer_data)
        cls.start_time = None
        cls.end_time = None
        cls.timer_count += 1
        
    @classmethod
    def export_time_log(cls):
        if cls.output_directory == None:
            os.makedirs(os.path.join(os.getcwd(), 'LogFiles/'), exist_ok=True)
            cls.output_directory = os.path.join(os.getcwd(), 'LogFiles/')
        pd.DataFrame().from_dict(cls.time_storage).to_csv(cls.output_directory + str(uuid4()) + '.log', index = False)
        

# %% Testing Timer Class - Uncomment to see the results

# x = Timer()

# x.start_timer()
# time.sleep(2)
# x.end_timer()

# x.display_time('Test')
# print(x.time_storage)

# x.start_timer()
# time.sleep(1)
# x.end_timer()
# x.display_time('Test_2')
# print(x.time_storage)
