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

            employee = Employee.objects.get(name = data['name'])
            task = Task.objects.get(task_name = data['task_name'])

            project_data = {
                'project_name': data['project_name'],
                'description': data['description'],
                'participants': employee,
                'tasks': task
            }

            project = Project.objects.create(**project_data)

            response_data = {
                'project_id': project.id,
                'project_name': project.project_name,
                'description': project.description,
                'participants': employee.name,
                'tasks': task.task_name
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

            project.project_name = data['project_name']
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
      project_data = {
        'id': project.id,
        'project_name': project.project_name,
        'description': project.description,
        'participants': project.participants.name
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
      project_list.append({
        'id': org.id,
        'project_name': org.project_name,
        'description': org.description,
        'participants': org.participants.name
      })

    return JsonResponse(project_list, safe=False, status=200)

  return JsonResponse({'error': 'Invalid request method'}, status=405)
