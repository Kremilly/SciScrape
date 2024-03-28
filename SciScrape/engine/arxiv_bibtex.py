#!/usr/bin/python3

class ArxivBibTex:
    
    @classmethod
    def generate_bibtex(self, data: dict) -> str:
        return f"""@misc{{{data['id']},
        title={{ {data['title']} }},
        author={{ {' and '.join(data['authors'])} }},
        year={{ {data['year']} }},
        eprint={{ {data['eprint']} }},
        primaryClass={{ {data['primary_class']} }}
    }}"""
    
    @classmethod
    def get(self, json_data: dict):
        authors = []

        for author in json_data['authors']:
            authors.append(author['name'])
        
        return self.generate_bibtex({
            'authors': authors,
            'id': json_data['id'],
            'title': json_data['title'],
            'eprint': json_data['eprint'],
            'primary_class': json_data['categories'][0]['name'],
            'year': json_data['date']['published'].split('-')[0]
        })
