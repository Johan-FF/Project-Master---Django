from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from employee.models import Employee
from role.models import Role
from organization.models import *
import json

@csrf_exempt
def login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            employee = Employee.objects.get(email = data['email'])

            if employee.password == data['password']:
              response_data = {
                'id': employee.id,
                'name': employee.name,
                'lastName': employee.last_name,
                'generalRole': employee.role.permissions,
                'role': employee.role.role_name,
                'organizationId': employee.member_organization.id
              }
              return JsonResponse(response_data, status=200)
            else:
              return JsonResponse({'error': "Password incorrect"}, status=400)

        except KeyError as e:
            return JsonResponse({'error': f'Missing key: {e.args[0]}'}, status=400)
        except Exception as e:
            if str(e)=="Employee matching query does not exist.":
               return JsonResponse({'error': "Email incorrect"}, status=400)
            return JsonResponse({'error': str(e)}, status=400)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)
