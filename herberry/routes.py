from app import application
from herberry.analyzer.views import analyze
from herberry.medications.views import medications


@application.route('/', endpoint='api-list')
def index():
    return {
        route.rule: route.endpoint
        for route in application.url_map.iter_rules()
    }


application.route('/analyze/')(analyze)
application.route('/medications/')(medications)
