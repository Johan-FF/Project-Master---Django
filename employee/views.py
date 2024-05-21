from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Employee
from role.models import Role
from organization.models import Organization
import json

@csrf_exempt
def create(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            role = Role.objects.get(id = data['roleId'])
            organization = Organization.objects.get(id = data['companyId'])

            employee_data = {
                'name': data['name'],
                'last_name': data['lastName'],
                'email': data['email'],
                'identification': data['identification'],
                'role': role,
                'organization': organization
            }

            employee = Employee.objects.create(**employee_data)

            response_data = {
                'id': employee.id,
                'name': employee.name,
                'lastName': employee.last_name,
                'email': employee.email,
                'identification': employee.identification,
                'roleName': role.role_name,
                'companyName': organization.company_name
            }
            return JsonResponse(response_data, status=201)
  
        except KeyError as e:
            return JsonResponse({'error': f'Missing key: {e.args[0]}'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def update(request, id):
  if request.method == 'PUT':
    try:
      data = json.loads(request.body)
      employee = Employee.objects.get(id=id)

      employee.name = data['name']
      employee.last_name = data['lastName']
      employee.email = data['email']
      employee.identification = data['identification']

      employee.save()

      return JsonResponse({"message": "success"}, status=204)
    
    except KeyError as e:
      return JsonResponse({'error': f'Missing key: {e.args[0]}'}, status=400)
    except Exception as e:
      return JsonResponse({'error': str(e)}, status=400)

  return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def delete(request, id):
  if request.method == 'DELETE':
    try:
      employee = Employee.objects.get(id=id)
      employee_data = {
        'id': employee.id,
        'name': employee.name,
        'lastName': employee.last_name,
        'email': employee.email,
        'identification': employee.identification,
        'role': employee.role.role_name,
        'organization': employee.organization.company_name
      }
      employee.delete()

      return JsonResponse(employee_data, status=200)
    except KeyError as e:
      return JsonResponse({'error': f'Missing key: {e.args[0]}'}, status=400)
    except Exception as e:
      return JsonResponse({'error': str(e)}, status=400)

  return JsonResponse({'error': 'Invalid request method'}, status=405)

def list(request):
  if request.method == 'GET':
    employees = Employee.objects.all()
    employee_list = []

    for org in employees:
      employee_list.append({
        'id': org.id,
        'name': org.name,
        'lastName': org.last_name,
        'email': org.email,
        'identification': org.identification,
        'role': org.role.role_name,
        'organization': org.organization.company_name
      })

    return JsonResponse(employee_list, safe=False, status=200)

  return JsonResponse({'error': 'Invalid request method'}, status=405)