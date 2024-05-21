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

            employee = Employee.objects.get(name = data['name'])

            meeting_data = {
                'subject': data['subject'],
                'meetTime': data['meetTime'],
                'place': data['place'],
                'description': data['description'],
                'participants': employee
            }

            meeting = Meeting.objects.create(**meeting_data)

            response_data = {
                    'id': meeting.id,
                    'subject': meeting.subject,
                    'meetTime': meeting.meetTime,
                    'place': meeting.place,
                    'description': meeting.description,
                    'participants': employee.name
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
            meeting.meetTime = data['meetTime']
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
      meeting_data = {
        'id': meeting.id,
        'subject': meeting.subject,
        'meetTime': meeting.meetTime,
        'place': meeting.place,
        'description': meeting.description,
        'participants': meeting.participants.name
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

    for org in meetings:
      meeting_list.append({
        'id': org.id,
        'subject': org.subject,
        'meetTime': org.meetTime,
        'place': org.place,
        'description': org.description,
        'participants': org.participants.name
      })

    return JsonResponse(meeting_list, safe=False, status=200)

  return JsonResponse({'error': 'Invalid request method'}, status=405)
