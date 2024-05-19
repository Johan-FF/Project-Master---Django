from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Organization, ContactOrganization
import json

@csrf_exempt
def create(request):
  if request.method == 'POST':
    try:
      data = json.loads(request.body)

      contact_organization_data = {
        'contact_name': data['contactName'],
        'contact_phone': data['contactPhone']
      }
      contact_organization = ContactOrganization.objects.create(**contact_organization_data)

      organization_data = {
        'company_name': data['companyName'],
        'industry': data['industry'],
        'employees_number': data['employeeCount'],
        'address': data['address'],
        'city': data['city'],
        'country': data['country'],
        'postal_code': data['postalCode'],
        'phone': data['companyPhone'],
        'id_contact': contact_organization
      }
      organization = Organization.objects.create(**organization_data)

      response_data = {
        'id': organization.id,
        'companyName': organization.company_name,
        'industry': organization.industry,
        'employeeCount': organization.employees_number,
        'address': organization.address,
        'city': organization.city,
        'postalCode': organization.postal_code,
        'country': organization.country,
        'companyPhone': organization.phone,
        'contactName': contact_organization.contact_name,
        'contactPhone': contact_organization.contact_phone
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
      organization = Organization.objects.get(id=id)

      organization.company_name = data['companyName']
      organization.industry = data['industry']
      organization.employees_number = data['employeeCount']
      organization.address = data['address']
      organization.city = data['city']
      organization.country = data['country']
      organization.postal_code = data['postalCode']
      organization.phone = data['companyPhone']

      organization.save()

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
      organization = Organization.objects.get(id=id)
      organization_data = {
        'id': organization.id,
        'companyName': organization.company_name,
        'industry': organization.industry,
        'employeeCount': organization.employees_number,
        'address': organization.address,
        'city': organization.city,
        'postalCode': organization.country,
        'country': organization.postal_code,
        'companyPhone': organization.phone,
        'contactName': organization.id_contact.contact_name,
        'contactPhone': organization.id_contact.contact_phone
      }
      organization.delete()

      return JsonResponse(organization_data, status=200)
    except KeyError as e:
      return JsonResponse({'error': f'Missing key: {e.args[0]}'}, status=400)
    except Exception as e:
      return JsonResponse({'error': str(e)}, status=400)

  return JsonResponse({'error': 'Invalid request method'}, status=405)

def list(request):
  if request.method == 'GET':
    organizations = Organization.objects.all()
    organization_list = []

    for org in organizations:
      organization_list.append({
        'id': org.id,
        'companyName': org.company_name,
        'industry': org.industry,
        'employeeCount': org.employees_number,
        'address': org.address,
        'city': org.city,
        'postalCode': org.postal_code,
        'country': org.country,
        'companyPhone': org.phone,
        'contactName': org.id_contact.contact_name,
        'contactPhone': org.id_contact.contact_phone
      })

    return JsonResponse(organization_list, safe=False, status=200)

  return JsonResponse({'error': 'Invalid request method'}, status=405)
