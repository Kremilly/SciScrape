#!/usr/bin/python3

import yaml

class Settings:
    
    file_path = './sciscrape.yml'
    
    @classmethod
    def get(self, property):
        try:
            with open(self.file_path, 'r') as content:
                data = yaml.safe_load(content)
            
            property_parts = property.split('.')
            value = data

            for part in property_parts:
                value = value[part]
                
            return value
        
        except FileNotFoundError:
            print(f"File '{self.file_path}' not found")
            return None
        
        except yaml.YAMLError as e:
            print(f"Error while parsing the YAML file.: {e}")
            return None
