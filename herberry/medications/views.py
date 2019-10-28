from flask import request
from herberry.medications.models import Medication


PAGE_OFFSET = 5000


def medications():
    try:
        page = int(request.args.get('page', 0))
    except ValueError:
        page = 0

    full_meds = Medication.all().sort('name')
    if page:
        curr = page * PAGE_OFFSET
        next = curr + PAGE_OFFSET
        paginated_meds = full_meds[curr:next]
    else:
        paginated_meds = full_meds[:PAGE_OFFSET]

    result = []
    for item in paginated_meds:
        item['id'] = str(item.pop('_id'))
        result.append(item)

    return {
        'count': full_meds.count(),
        'next': f'{request.path}?page={page+1}',
        'result': result
    }
