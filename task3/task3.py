import json


def get_values(id: int, results: dict):
    for test in results['values']:
        if id == test['id']:
            return test['value']
    
    
def add_values(structure: dict, results: dict):
    for test in structure:
        if 'value' in test:
            test['value'] = get_values(test['id'], results)
        if 'values' in test:
            add_values(test['values'], results)
            

def make_report(test_structure_path: str, test_results_path: str, report_path: str):
    with open(test_structure_path, 'r') as file2:
        structure = json.load(file2)
    
    with open(test_results_path, 'r') as file1:
        results = json.load(file1)
        
    add_values(structure['tests'], results)
    
    with open(report_path, 'w') as file3:
        json.dump(structure, file3, indent=2)


make_report('task3/tests.json', 'task3/values.json', 'task3/report.json')