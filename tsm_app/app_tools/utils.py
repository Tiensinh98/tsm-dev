import json

import tsm_app.app_tools.database as db

def read_dataset_from_json(filepath):
    with open(filepath, 'r') as f:
        dataset_json = json.load(f)
        project_datas = dataset_json.get('projects')
        if project_datas is not None:
            for project_json in project_datas:
                project = db.Project.from_json_value(project_json)
                project.save()
        leader_datas = dataset_json.get('leaders')
        if leader_datas is not None:
            for leader_data in leader_datas:
                leader = db.Leader.from_json_value(leader_data)
                if leader is not None:
                    leader.save()


def truncate_all_tables():
    for model_str, model in db.__dict__.items():
        if model_str.startswith('__'):
            continue
        if model_str in ['user_models', 'issue_models',
                         'staff_models', 'device_models', 'team_models']:
            continue
        model.objects.all().delete()
