from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Project
from employee.models import Employee
from task.models import Task
import json

@csrf_exempt
def create(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            project_data = {
              'project_name': data['projectName'],
              'description': data['description']
            }

            project = Project.objects.create(**project_data)
            employees = Employee.objects.filter(id__in=data['employees'])
            project.participants.add(*employees)

            employees_response = []
            for empl in employees:
              employee_data = {
                'id': empl.id,
                'name': empl.name,
                'lastName': empl.last_name,
                'email': empl.email,
                'identification': empl.identification,
                'role': empl.role.role_name,
                'organization': empl.member_organization.company_name
              }
              employees_response.append(employee_data) 

            response_data = {
                'project_id': project.id,
                'projectName': project.project_name,
                'description': project.description,
                'participants': employees_response,
                'tasks': []
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
            project = Project.objects.get(id=id)

            project.project_name = data['projectName']
            project.description = data['description']

            project.save()

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
      project = Project.objects.get(id=id)

      employees_response = []
      for empl in project.participants.values():
        employee_data = {
          'id': empl["id"],
          'name': empl["name"],
          'lastName': empl["last_name"],
          'email': empl["email"],
          'identification': empl["identification"],
          'role': empl["role_id"],
          'organization': empl["organization_id"]
        }
        employees_response.append(employee_data)

      project_data = {
        'id': project.id,
        'projectName': project.project_name,
        'description': project.description,
        'participants': employees_response
      }
      project.delete()

      return JsonResponse(project_data, status=200)
    except KeyError as e:
      return JsonResponse({'error': f'Missing key: {e.args[0]}'}, status=400)
    except Exception as e:
      return JsonResponse({'error': str(e)}, status=400)

  return JsonResponse({'error': 'Invalid request method'}, status=405)

def list(request):
  if request.method == 'GET':
    projects = Project.objects.all()
    project_list = []

    for org in projects:
      employees_response = []
      for empl in org.participants.values():
        employee_data = {
          'id': empl["id"],
          'name': empl["name"],
          'lastName': empl["last_name"],
          'email': empl["email"],
          'identification': empl["identification"],
          'role': empl["role_id"],
          'organization': empl["organization_id"]
        }
        employees_response.append(employee_data)

      project_list.append({
        'id': org.id,
        'projectName': org.project_name,
        'description': org.description,
        'participants': employees_response
      })

    return JsonResponse(project_list, safe=False, status=200)

  return JsonResponse({'error': 'Invalid request method'}, status=405)
