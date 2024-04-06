#!/usr/bin/python3

import random

from configs.env import Env

class GenerateUtils:
    
    @classmethod
    def random_string(cls, size: int) -> str:
        output_str = ''
        random_str_seq = Env.RANDOM_STR
        
        for _ in range(0, size):
            output_str += str(
                random_str_seq[
                    random.randint(
                        0, len(random_str_seq) - 1
                    )
                ]
            )
        
        return output_str
