import json

import tsm_app.app_tools.database as db

def read_dataset_from_json(filepath):
    with open(filepath, 'r') as f:
        dataset_json = json.load(f)
        project_datas = dataset_json['projects']
        for project_json in project_datas:
            project = db.Project.from_json_value(project_json)
            project.save()


def truncate_all_tables():
    for model_str, model in db.__dict__.items():
        if model_str.startswith('__'):
            continue
        if model_str.startswith('models'):
            continue
        model.objects.all().delete()
