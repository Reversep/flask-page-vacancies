from . import app, db
from . import views

app.add_url_rule('/', view_func=views.employee_list)
app.add_url_rule('/branch', view_func=views.branch_list)
app.add_url_rule('/position', view_func=views.position_list)
app.add_url_rule('/branch/add', view_func=views.branch_add, methods=['POST', 'GET'])
app.add_url_rule('/position/add', view_func=views.position_add, methods=['POST', 'GET'])
app.add_url_rule('/employee/add', view_func=views.employee_add, methods=['POST', 'GET'])