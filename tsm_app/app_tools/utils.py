import json

import tsm_app.app_tools.database as db

def read_dataset_from_json(filepath):
    with open(filepath, 'r') as f:
        dataset_json = json.load(f)
        model_datas = dataset_json.get('models', None)
        if model_datas is not None:
            for model_data in model_datas:
                model_class_name = model_data.get('model_class')
                model_class = getattr(db, model_class_name)
                tuples = model_data.get('tuples')
                for tup in tuples:
                    model = model_class.from_json_value(tup)
                    model.save()

        relations = dataset_json.get('relations', None)
        if relations is not None:
            for relation in relations:
                relation_field = relation.get('relation')
                reference = relation.get('reference')
                reference_model = getattr(db, reference['model_class']).\
                    objects.get(id=reference['id'])
                assert reference_model is not None, f"Not found {reference['model_class']} with id {reference['id']}"
                target = relation.get('target')
                target_model = getattr(db, target['model_class']). \
                    objects.get(id=target['id'])
                assert reference_model is not None, f"Not found {target_model['model_class']} with id {target['id']}"
                setattr(target_model, relation_field, reference_model)
                target_model.save()


def truncate_all_tables():
    for model_str, model in db.__dict__.items():
        if model_str.startswith('__'):
            continue
        if model_str in ['user_models', 'issue_models',
                         'staff_models', 'device_models', 'team_models']:
            continue
        model.objects.all().delete()
