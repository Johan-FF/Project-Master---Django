from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Role
import json

@csrf_exempt
def create(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            role_data = {
                'role_name': data['roleName'],
                'description': data['description'],
                'permissions': data['permissions']
            }

            role = Role.objects.create(**role_data)

            response_data = {
                'id': role.id,
                'roleName': role.role_name,
                'description': role.description,
                'permissions': role.permissions
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
            role = Role.objects.get(id=id)

            role.role_name = data['roleName']
            role.description = data['description']
            role.permissions = data['permissions']

            role.save()

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
      role = Role.objects.get(id=id)
      role_data = {
        'id': role.id,
        'roleName': role.role_name,
        'description': role.description,
        'permissions': role.permissions
      }
      role.delete()

      return JsonResponse(role_data, status=200)
    except KeyError as e:
      return JsonResponse({'error': f'Missing key: {e.args[0]}'}, status=400)
    except Exception as e:
      return JsonResponse({'error': str(e)}, status=400)

  return JsonResponse({'error': 'Invalid request method'}, status=405)

def list(request):
  if request.method == 'GET':
    roles = Role.objects.all()
    role_list = []

    for org in roles:
      role_list.append({
        'id': org.id,
        'roleName': org.role_name,
        'description': org.description,
        'participants': org.permissions
      })

    return JsonResponse(role_list, safe=False, status=200)

  return JsonResponse({'error': 'Invalid request method'}, status=405)
