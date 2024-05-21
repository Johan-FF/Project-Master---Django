from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Task
from project.models import Project
from employee.models import Employee
import json

@csrf_exempt
def create(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            project = Project.objects.get(project_name = data['project_name'])
            employee = Employee.objects.get(name = data['name'])

            task_data = {
                'task_name': data['task_name'],
                'comments': data['comments'],
                'delivery_date': data['delivery_date'],
                'state': data['state'],
                'tied_project': project,
                'associated_employee': employee
            }

            task = Task.objects.create(**task_data)

            response_data = {
                'id': task.id,
                'task_name': task.task_name,
                'comments': task.comments,
                'delivery_date': task.delivery_date,
                'state': task.state,
                'tied_project': project.project_name,
                'associated_employee': employee.name
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
      task = Task.objects.get(id=id)

      task.task_name = data['task_name']
      task.comments = data['comments']
      task.delivery_date = data['delivery_date']
      task.state = data['state']

      task.save()

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
      task = Task.objects.get(id=id)
      task_data = {
        'id': task.id,
        'task_name': task.task_name,
        'comments': task.comments,
        'delivery_date': task.delivery_date,
        'state': task.state,
        'tied_project': task.tied_project.project_name,
        'associated_employee': task.associated_employee.name
      }
      task.delete()

      return JsonResponse(task_data, status=200)
    except KeyError as e:
      return JsonResponse({'error': f'Missing key: {e.args[0]}'}, status=400)
    except Exception as e:
      return JsonResponse({'error': str(e)}, status=400)

  return JsonResponse({'error': 'Invalid request method'}, status=405)

def list(request):
  if request.method == 'GET':
    tasks = Task.objects.all()
    task_list = []

    for org in tasks:
      task_list.append({
        'id': org.id,
        'task_name': org.task_name,
        'comments': org.comments,
        'delivery_date': org.delivery_date,
        'state': org._state,
        'tied_project': org.tied_project.project_name,
        'associated_employee': org.associated_employee.name
      })

    return JsonResponse(task_list, safe=False, status=200)

  return JsonResponse({'error': 'Invalid request method'}, status=405)