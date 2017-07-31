from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient


token = Token.objects.get(user__username='lauren')
user = User.objects.get(username='lauren')
client = APIClient(enforce_csrf_checks=True)
client.force_authenticate(user=user)
client.force_authenticate(user=None)
client.credentials(HTTP_AUTHORIZATION='Token' + token.key)
client.post('/notes', {'title': 'new idea'}, format='json')
client.login(username='lauren', password='secret')
client.logout()
# Create your tests here.
