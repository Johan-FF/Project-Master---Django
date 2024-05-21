from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Meeting
from employee.models import Employee
import json


@csrf_exempt
def create(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            meeting_data = {
                'subject': data['subject'],
                'meet_time': data['meetTime'],
                'place': data['place'],
                'description': data['description']
            }

            meeting = Meeting.objects.create(**meeting_data)
            employees = Employee.objects.filter(id__in=data['employees'])
            meeting.participants.add(*employees)

            employees_response = []
            for empl in employees:
              employee_data = {
                'id': empl.id,
                'name': empl.name,
                'lastName': empl.last_name,
                'email': empl.email,
                'identification': empl.identification,
                'role': empl.role.role_name,
                'organization': empl.organization.company_name
              }
              employees_response.append(employee_data)

            response_data = {
                    'id': meeting.id,
                    'subject': meeting.subject,
                    'meetTime': meeting.meet_time,
                    'place': meeting.place,
                    'description': meeting.description,
                    'participants': employees_response
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
            meeting = Meeting.objects.get(id=id)

            meeting.subject = data['subject']
            meeting.meet_time = data['meetTime']
            meeting.place = data['place']
            meeting.description = data['description']

            meeting.save()

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
      meeting = Meeting.objects.get(id=id)

      employees_response = []
      for empl in meeting.participants.values():
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

      meeting_data = {
        'id': meeting.id,
        'subject': meeting.subject,
        'meetTime': meeting.meet_time,
        'place': meeting.place,
        'description': meeting.description,
        'participants': employees_response
      }
      meeting.delete()

      return JsonResponse(meeting_data, status=200)
    except KeyError as e:
      return JsonResponse({'error': f'Missing key: {e.args[0]}'}, status=400)
    except Exception as e:
      return JsonResponse({'error': str(e)}, status=400)

  return JsonResponse({'error': 'Invalid request method'}, status=405)

def list(request):
  if request.method == 'GET':
    meetings = Meeting.objects.all()
    meeting_list = []

    for meet in meetings:
      employees_response = []
      for empl in meet.participants.values():
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

      meeting_list.append({
        'id': org.id,
        'subject': org.subject,
        'meetTime': org.meet_time,
        'place': org.place,
        'description': org.description,
        'participants': employees_response
      })

    return JsonResponse(meeting_list, safe=False, status=200)

  return JsonResponse({'error': 'Invalid request method'}, status=405)
