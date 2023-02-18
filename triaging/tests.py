from audioop import reverse

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


# Create your tests here.
class HelloWorldTestCase(APITestCase):
  def test_hello_world(self):
    response = self.client.get(reverse("hello_world"))
    
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data["msg"], "Hello World!")

class TriagingTestCase(APITestCase):
  

  def test_triaging(self):
    """
        Ensure we can get a new a feature color as a result.
    """
    url = reverse('triaging')
    data = {
              "bmi":24,
              "waist_hip_ratio": 0.8,
              "temperature": 37.5,
              "spo2":86,
              "bp_sys":180, 
              "bp_dia": 115,
              "blood_sugar":17,
              "blood_hemoglobin":6,
              "pulse_rate":30,
              "blood_cholesterol": 230,
              "blood_uric_acid": 14
            }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    