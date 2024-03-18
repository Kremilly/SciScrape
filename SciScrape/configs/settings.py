#!/usr/bin/python3

import yaml

from configs.env import Env

from exceptions.settings_exception import SettingsException

class Settings:
    
    configs_file = Env.CONFIGS_FILE
    
    @classmethod
    def search_property_in_file(self, property):
        property = property.split('.')[-1]
        
        try:
            with open(self.configs_file, 'r') as file:
                lines = file.readlines()
                
                for line_number, line in enumerate(lines, start = 1):
                    if property in line:
                        return f"{line_number} -> '{line.strip()}'"
                        
        except FileNotFoundError:
            return None
    
    @classmethod
    def is_valid(self, property, value, data_type):
        if type(value) == str:
            value_type = 'STRING'
        elif type(value) == int:
            value_type = 'INT'
        elif type(value) == float:
            value_type = 'FLOAT'
        elif type(value) == bool:
            value_type = 'BOOLEAN'
            
        data_type = data_type.upper()
        line_position = self.search_property_in_file(property)
        
        if value_type != data_type:
            raise SettingsException(f"The '{property}' configuration is invalid. Expected type {data_type}, but instead a {value_type} was passed. Please fix it in the file: sciscrape.yml:{line_position}")
        
        return value
    
    @classmethod
    def get(self, property, data_type):
        try:
            with open(self.configs_file, 'r') as content:
                data = yaml.safe_load(content)
            
            value = data
            property_parts = property.split('.')

            for part in property_parts:
                value = value[part]
                
            return self.is_valid(property, value, data_type)
        
        except FileNotFoundError:
            print(f"File '{self.configs_file.replace('./', '')}' not found")
            return None
        
        except yaml.YAMLError as e:
            print(f"Error while parsing the YAML file.: {e}")
            return None
