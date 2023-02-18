import json

from django.http import HttpResponse, JsonResponse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from triaging.phcLogic import *


# Create your views here.
@api_view(['GET','POST'])
def hello(request):
        if request.method == 'GET':
          return Response({"msg": "Hello World!"}, status=status.HTTP_200_OK)
        return HttpResponse(status=405)

def get_traiging_values():
            try:
              triaging =TriagingSettings.objects.all()[0]
            except:
              return JsonResponse({'msg': 'Check the request to the database!'}, safe=False, status=400)
            
            result = {}
            
            result['BMI_GREEN_MIN'] = triaging.BMI_GREEN_MIN
            result['BMI_GREEN_MAX'] = triaging.BMI_GREEN_MAX
            result['BMI_YELLOW_MIN']  = triaging.BMI_YELLOW_MIN
            result['BMI_YELLOW_MAX'] = triaging.BMI_YELLOW_MAX
            result['BMI_ORANGE_MIN'] = triaging.BMI_ORANGE_MIN
            result['BMI_ORANGE_MAX'] = triaging.BMI_ORANGE_MAX
            result['BMI_RED_MIN'] = triaging.BMI_RED_MIN
            result['BMI_RED_MAX'] = triaging.BMI_RED_MAX
            
            
            result['WAIST_HIP_RATIO_GREEN_MIN']  = triaging.WAIST_HIP_RATIO_GREEN_MIN
            result['WAIST_HIP_RATIO_GREEN_MAX'] = triaging.WAIST_HIP_RATIO_GREEN_MAX
            result['WAIST_HIP_RATIO_YELLOW_MIN'] = triaging.WAIST_HIP_RATIO_YELLOW_MIN
            result['WAIST_HIP_RATIO_YELLOW_MAX'] = triaging.WAIST_HIP_RATIO_YELLOW_MAX
            
            result['TEMPERATURE_GREEN_MIN'] = triaging.TEMPERATURE_GREEN_MIN
            result['TEMPERATURE_GREEN_MAX'] = triaging.TEMPERATURE_GREEN_MAX
            result['TEMPERATURE_YELLOW_MIN'] = triaging.TEMPERATURE_YELLOW_MIN
            result['TEMPERATURE_YELLOW_MAX'] = triaging.TEMPERATURE_YELLOW_MAX
            result['TEMPERATURE_ORANGE_MIN'] = triaging.TEMPERATURE_ORANGE_MIN
            result['TEMPERATURE_ORANGE_MAX'] = triaging.TEMPERATURE_ORANGE_MAX
            result['TEMPERATURE_RED_MIN'] = triaging.TEMPERATURE_RED_MIN
            result['TEMPERATURE_RED_MAX'] = triaging.TEMPERATURE_RED_MAX
            
            
            result['SPO2_GREEN_MIN'] = triaging.SPO2_GREEN_MIN
            result['SPO2_GREEN_MAX'] = triaging.SPO2_GREEN_MAX
            result['SPO2_YELLOW_MIN'] = triaging.SPO2_YELLOW_MIN
            result['SPO2_YELLOW_MAX'] = triaging.SPO2_YELLOW_MAX
            result['SPO2_ORANGE_MIN'] = triaging.SPO2_ORANGE_MIN
            result['SPO2_ORANGE_MAX'] = triaging.SPO2_ORANGE_MAX
            result['SPO2_RED_MIN'] = triaging.SPO2_RED_MIN
            result['SPO2_RED_MAX'] = triaging.SPO2_RED_MAX
            
            
            result["BP_SYS_GREEN_MIN"] = triaging.BP_SYS_GREEN_MIN
            result["BP_SYS_GREEN_MAX"] = triaging.BP_SYS_GREEN_MAX
            result["BP_SYS_YELLOW_MIN"] = triaging.BP_SYS_YELLOW_MIN
            result["BP_SYS_YELLOW_MAX"] = triaging.BP_SYS_YELLOW_MAX
            result["BP_SYS_ORANGE_MIN"] = triaging.BP_SYS_ORANGE_MIN
            result["BP_SYS_ORANGE_MAX"] = triaging.BP_SYS_ORANGE_MAX
            result["BP_SYS_RED_MIN"] = triaging.BP_SYS_RED_MIN
            result["BP_SYS_RED_MAX"] = triaging.BP_SYS_RED_MAX
            

            result["BP_DIA_GREEN_MIN"] = triaging.BP_DIA_GREEN_MIN
            result["BP_DIA_GREEN_MAX"] = triaging.BP_DIA_GREEN_MAX
            result["BP_DIA_YELLOW_MIN"] = triaging.BP_DIA_YELLOW_MIN
            result["BP_DIA_YELLOW_MAX"] = triaging.BP_DIA_YELLOW_MAX
            result["BP_DIA_ORANGE_MIN"] = triaging.BP_DIA_ORANGE_MIN
            result["BP_DIA_ORANGE_MAX"] = triaging.BP_DIA_ORANGE_MAX
            result["BP_DIA_RED_MIN"] = triaging.BP_DIA_RED_MIN
            result["BP_DIA_RED_MAX"] = triaging.BP_DIA_RED_MAX
            
            
            result["BLOOD_SUGAR_GREEN_MIN"] = triaging.BLOOD_SUGAR_GREEN_MIN
            result["BLOOD_SUGAR_GREEN_MAX"] = triaging.BLOOD_SUGAR_GREEN_MAX
            result["BLOOD_SUGAR_YELLOW_MIN"] = triaging.BLOOD_SUGAR_YELLOW_MIN
            result["BLOOD_SUGAR_YELLOW_MAX"] = triaging.BLOOD_SUGAR_YELLOW_MAX
            result["BLOOD_SUGAR_ORANGE_MIN"] = triaging.BLOOD_SUGAR_ORANGE_MIN
            result["BLOOD_SUGAR_ORANGE_MAX"] = triaging.BLOOD_SUGAR_ORANGE_MAX
            result["BLOOD_SUGAR_RED_MIN"] = triaging.BLOOD_SUGAR_ORANGE_MAX
            result["BLOOD_SUGAR_RED_MAX"] = triaging.BLOOD_SUGAR_RED_MAX
            
          
            result["BLOOD_HEMOGLOBIN_GREEN_MIN"] = triaging.BLOOD_HEMOGLOBIN_GREEN_MIN
            result["BLOOD_HEMOGLOBIN_GREEN_MAX"] = triaging.BLOOD_HEMOGLOBIN_GREEN_MAX
            result["BLOOD_HEMOGLOBIN_YELLOW_MIN"] = triaging.BLOOD_HEMOGLOBIN_YELLOW_MIN
            result["BLOOD_HEMOGLOBIN_YELLOW_MAX"] = triaging.BLOOD_HEMOGLOBIN_YELLOW_MAX
            result["BLOOD_HEMOGLOBIN_ORANGE_MIN"] = triaging.BLOOD_HEMOGLOBIN_ORANGE_MIN
            result["BLOOD_HEMOGLOBIN_ORANGE_MAX"] = triaging.BLOOD_HEMOGLOBIN_ORANGE_MAX
            result["BLOOD_HEMOGLOBIN_RED_MIN"] = triaging.BLOOD_HEMOGLOBIN_RED_MIN
            result["BLOOD_HEMOGLOBIN_RED_MAX"] = triaging.BLOOD_HEMOGLOBIN_RED_MAX

            result["Pulse_Rate_GREEN_MIN"] = triaging.Pulse_Rate_GREEN_MIN
            result["Pulse_Rate_GREEN_MAX"] = triaging.Pulse_Rate_GREEN_MAX
            result["Pulse_Rate_YELLOW_MIN_1"] = triaging.Pulse_Rate_YELLOW_MIN_1
            result["Pulse_Rate_YELLOW_MAX_1"] = triaging.Pulse_Rate_YELLOW_MAX_1
            result["Pulse_Rate_YELLOW_MIN_2"] = triaging.Pulse_Rate_YELLOW_MIN_2
            result["Pulse_Rate_YELLOW_MAX_2"] = triaging.Pulse_Rate_YELLOW_MAX_2
            result["Pulse_Rate_ORANGE_MIN_1"] = triaging.Pulse_Rate_ORANGE_MIN_1
            result["Pulse_Rate_ORANGE_MIN_2"] = triaging.Pulse_Rate_ORANGE_MIN_2
            result["Pulse_Rate_ORANGE_MAX"] = triaging.Pulse_Rate_ORANGE_MAX
            result["Pulse_Rate_RED_MIN"] = triaging.Pulse_Rate_RED_MIN
            result["Pulse_Rate_RED_MAX"] = triaging.Pulse_Rate_RED_MAX

            
            result["Blood_Cholesterol_GREEN_MIN"] = triaging.Blood_Cholesterol_GREEN_MIN
            result["Blood_Cholesterol_GREEN_MAX"] = triaging.Blood_Cholesterol_GREEN_MAX
            result["Blood_Cholesterol_YELLOW_MIN"] = triaging.Blood_Cholesterol_YELLOW_MIN
            result["Blood_Cholesterol_YELLOW_MAX"] = triaging.Blood_Cholesterol_YELLOW_MAX
            result["Blood_Cholesterol_ORANGE_MIN"] = triaging.Blood_Cholesterol_ORANGE_MIN
            result["Blood_Cholesterol_ORANGE_MAX"] = triaging.Blood_Cholesterol_ORANGE_MAX
            result["Blood_Cholesterol_RED_MIN"] = triaging.Blood_Cholesterol_RED_MIN
            result["Blood_Cholesterol_RED_MAX"] = triaging.Blood_Cholesterol_RED_MAX
            
           
            result["Blood_Uric_Acid_GREEN_MIN"] = triaging.Blood_Uric_Acid_GREEN_MIN
            result["Blood_Uric_Acid_GREEN_MAX"] = triaging.Blood_Uric_Acid_GREEN_MAX
            result["Blood_Uric_Acid_ORANGE_MIN"] = triaging.Blood_Uric_Acid_ORANGE_MIN
            result["Blood_Uric_Acid_ORANGE_MAX"] = triaging.Blood_Uric_Acid_ORANGE_MAX
            result["Blood_Uric_Acid_RED_MIN"] = triaging.Blood_Uric_Acid_RED_MIN
            result["Blood_Uric_Acid_RED_MAX"] = triaging.Blood_Uric_Acid_RED_MAX
            print(result["BLOOD_HEMOGLOBIN_GREEN_MIN"])
            return result
            
            
# here we define that this view accepts a json (or object parameter) that has these parameters(bmi, wait_hip_ratio, etc.) inside of it
@swagger_auto_schema(method='post', 
    request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT, # object because the data is in json format
    properties={
        'bmi': openapi.Schema(type=openapi.TYPE_NUMBER,),
        'waist_hip_ratio': openapi.Schema(type=openapi.TYPE_NUMBER,),
        'temperature': openapi.Schema(type=openapi.TYPE_NUMBER,),
        'spo2': openapi.Schema(type=openapi.TYPE_NUMBER,),
        'bp_sys': openapi.Schema(type=openapi.TYPE_NUMBER,),
        'bp_dia': openapi.Schema(type=openapi.TYPE_NUMBER,),
        'blood_sugar': openapi.Schema(type=openapi.TYPE_NUMBER,),
        'blood_hemoglobin': openapi.Schema(type=openapi.TYPE_NUMBER,),
        'pulse_rate': openapi.Schema(type=openapi.TYPE_NUMBER,),
        'blood_cholesterol': openapi.Schema(type=openapi.TYPE_NUMBER,),
        'blood_uric_acid': openapi.Schema(type=openapi.TYPE_NUMBER,),

    }
), operation_id="feature_triaging")

@api_view(['POST',])
def triagingView(request):
    if request.method == 'POST':
        try:
            print(request.body)
            data = json.loads(request.body.decode('utf-8'))
            result = {}
            triaging_values = get_traiging_values()
            # For BMI triaging
            if 'bmi' in data.keys():
              if data['bmi'] >= triaging_values['BMI_GREEN_MIN'] and data['bmi']<triaging_values['BMI_GREEN_MAX']:
                BMI_COLOR = GREEN
                result['BMI_COLOR'] = BMI_COLOR
              elif data['bmi'] >= triaging_values['BMI_YELLOW_MIN'] and data['bmi'] < triaging_values['BMI_YELLOW_MAX']:
                BMI_COLOR = YELLOW
                result['BMI_COLOR'] = BMI_COLOR
              elif data['bmi'] >= triaging_values['BMI_ORANGE_MIN'] and data['bmi'] < triaging_values['BMI_ORANGE_MAX']:
                BMI_COLOR = ORANGE
                result['BMI_COLOR'] = BMI_COLOR
              elif data['bmi'] >= triaging_values['BMI_RED_MIN'] and data['bmi']<triaging_values['BMI_RED_MAX']:
                BMI_COLOR = RED
                result['BMI_COLOR'] = BMI_COLOR
              else:
                msg = f'BMI value should be between {triaging_values["BMI_GREEN_MIN"]} and {triaging_values["BMI_RED_MAX"]}'
                return JsonResponse({'msg': msg}, safe=False, status=400)
            
            # For Waist/Hip Ratio triaging
            if 'waist_hip_ratio' in data.keys():
              if data['waist_hip_ratio'] >= triaging_values['WAIST_HIP_RATIO_GREEN_MIN'] and data['waist_hip_ratio']<triaging_values['WAIST_HIP_RATIO_GREEN_MAX']:
                WAIST_HIP_RATIO_COLOR = GREEN
                result['WAIST_HIP_RATIO_COLOR'] = WAIST_HIP_RATIO_COLOR
              elif data['waist_hip_ratio'] >= triaging_values['WAIST_HIP_RATIO_YELLOW_MIN'] and data['waist_hip_ratio'] < triaging_values['WAIST_HIP_RATIO_YELLOW_MAX']:
                WAIST_HIP_RATIO_COLOR = YELLOW
                result['WAIST_HIP_RATIO_COLOR'] = WAIST_HIP_RATIO_COLOR
              else:
                msg = f'Waist Hip Ratio value should be between {triaging_values["WAIST_HIP_RATIO_GREEN_MIN"]} and {triaging_values["WAIST_HIP_RATIO_YELLOW_MAX"]}'
                return JsonResponse({'msg': msg}, safe=False, status=400)
            
            # For temperature triaging
            if 'temperature' in data.keys():
              if data['temperature'] >= triaging_values["TEMPERATURE_GREEN_MIN"] and data['temperature']<triaging_values["TEMPERATURE_GREEN_MAX"]:
                TEMPERATURE_COLOR = GREEN
                result['TEMPERATURE_COLOR'] = TEMPERATURE_COLOR
              elif data['temperature'] >= triaging_values["TEMPERATURE_YELLOW_MIN"] and data['temperature'] < triaging_values["TEMPERATURE_YELLOW_MAX"]:
                TEMPERATURE_COLOR = YELLOW
                result['TEMPERATURE_COLOR'] = TEMPERATURE_COLOR
              elif data['temperature'] >= triaging_values["TEMPERATURE_ORANGE_MIN"] and data['temperature'] < triaging_values["TEMPERATURE_ORANGE_MAX"]:
                TEMPERATURE_COLOR = ORANGE
                result['TEMPERATURE_COLOR'] = TEMPERATURE_COLOR
              elif data['temperature'] >= triaging_values["TEMPERATURE_RED_MIN"] and data['temperature']<triaging_values["TEMPERATURE_RED_MAX"]:
                TEMPERATURE_COLOR = RED
                result['TEMPERATURE_COLOR'] = TEMPERATURE_COLOR
              else:
                msg = f'TEMPERATURE value should be between {triaging_values["TEMPERATURE_GREEN_MIN"]} and {triaging_values["TEMPERATURE_RED_MAX"]}'
                return JsonResponse({'msg': msg}, safe=False, status=400)
            
            # For SPO2 triaging
            if 'spo2' in data.keys():
              if data['spo2'] >= triaging_values["SPO2_GREEN_MIN"] and data['spo2']<triaging_values["SPO2_GREEN_MAX"]:
                SPO2_COLOR = GREEN
                result['SPO2_COLOR'] = SPO2_COLOR
              elif data['spo2'] >= triaging_values["SPO2_YELLOW_MIN"] and data['spo2'] < triaging_values["SPO2_YELLOW_MAX"]:
                SPO2_COLOR = YELLOW
                result['SPO2_COLOR'] = SPO2_COLOR
              elif data['spo2'] >= triaging_values["SPO2_ORANGE_MIN"] and data['spo2'] < triaging_values["SPO2_ORANGE_MAX"]:
                SPO2_COLOR = ORANGE
                result['SPO2_COLOR'] = SPO2_COLOR
              elif data['spo2'] >= triaging_values["SPO2_RED_MAX"] and data['spo2']<triaging_values["SPO2_RED_MIN"]:
                SPO2_COLOR = RED
                result['SPO2_COLOR'] = SPO2_COLOR
              else:
                msg = f'SPO2 value should be between {triaging_values["SPO2_RED_MAX"]} and {triaging_values["SPO2_GREEN_MAX"]}'
                return JsonResponse({'msg': msg}, safe=False, status=400)
            
            # For BP sys triaging
            if 'bp_sys' in data.keys():
              if data['bp_sys'] >= triaging_values["BP_SYS_GREEN_MIN"] and data['bp_sys']<triaging_values["BP_SYS_GREEN_MAX"]:
                BP_SYS_COLOR = GREEN
                result['BP_SYS_COLOR'] = BP_SYS_COLOR
              elif data['bp_sys'] >= triaging_values["BP_SYS_YELLOW_MIN"] and data['bp_sys'] < triaging_values["BP_SYS_YELLOW_MAX"]:
                BP_SYS_COLOR = YELLOW
                result['BP_SYS_COLOR'] = BP_SYS_COLOR
              elif data['bp_sys'] >= triaging_values["BP_SYS_ORANGE_MIN"] and data['bp_sys'] < triaging_values["BP_SYS_ORANGE_MAX"]:
                BP_SYS_COLOR = ORANGE
                result['BP_SYS_COLOR'] = BP_SYS_COLOR
              elif data['bp_sys'] >= triaging_values["BP_SYS_RED_MIN"] and data['bp_sys']<triaging_values["BP_SYS_RED_MAX"]:
                BP_SYS_COLOR = RED
                result['BP_SYS_COLOR'] = BP_SYS_COLOR
              else:
                msg = f'Blood pressure(sys) value should be between {triaging_values["BP_SYS_GREEN_MIN"]} and {triaging_values["BP_SYS_RED_MAX"]}'
                return JsonResponse({'msg': msg}, safe=False, status=400)
            
            # For BP dia triaging
            if 'bp_dia' in data.keys():
              if data['bp_dia'] >= triaging_values["BP_DIA_GREEN_MIN"] and data['bp_dia']< triaging_values["BP_DIA_GREEN_MAX"]:
                BP_DIA_COLOR = GREEN
                result['BP_DIA_COLOR'] = BP_DIA_COLOR
              elif data['bp_dia'] >= triaging_values["BP_DIA_YELLOW_MIN"]  and data['bp_dia'] < triaging_values["BP_DIA_YELLOW_MAX"]:
                BP_DIA_COLOR = YELLOW
                result['BP_DIA_COLOR'] = BP_DIA_COLOR
              elif data['bp_dia'] >= triaging_values["BP_DIA_ORANGE_MIN"] and data['bp_dia'] < triaging_values["BP_DIA_ORANGE_MAX"]:
                BP_DIA_COLOR = ORANGE
                result['BP_DIA_COLOR'] = BP_DIA_COLOR
              elif data['bp_dia'] >= triaging_values["BP_DIA_RED_MIN"]  and data['bp_dia']<triaging_values["BP_DIA_RED_MAX"]:
                BP_DIA_COLOR = RED
                result['BP_DIA_COLOR'] = BP_DIA_COLOR
              else:
                msg = f'Blood pressure(dia) value should be between {triaging_values["BP_DIA_GREEN_MIN"]} and {triaging_values["BP_DIA_GREEN_MAX"]}'
                return JsonResponse({'msg': msg}, safe=False, status=400)
            
            # For Blood Sugar triaging
            if 'blood_sugar' in data.keys():
              if data['blood_sugar'] >= triaging_values["BLOOD_SUGAR_GREEN_MIN"] and data['blood_sugar']<triaging_values["BLOOD_SUGAR_GREEN_MAX"]:
                BLOOD_SUGAR_COLOR = GREEN
                result['BLOOD_SUGAR_COLOR'] = BLOOD_SUGAR_COLOR
              elif data['blood_sugar'] >= triaging_values["BLOOD_SUGAR_YELLOW_MIN"] and data['blood_sugar'] < triaging_values["BLOOD_SUGAR_YELLOW_MAX"]:
                BLOOD_SUGAR_COLOR = YELLOW
                result['BLOOD_SUGAR_COLOR'] = BLOOD_SUGAR_COLOR
              elif data['blood_sugar'] >=  triaging_values["BLOOD_SUGAR_ORANGE_MIN"]  and data['blood_sugar'] <triaging_values["BLOOD_SUGAR_ORANGE_MAX"] :
                BLOOD_SUGAR_COLOR = ORANGE
                result['BLOOD_SUGAR_COLOR'] = BLOOD_SUGAR_COLOR
              elif data['blood_sugar'] >= triaging_values["BLOOD_SUGAR_RED_MIN"] and data['blood_sugar']<triaging_values["BLOOD_SUGAR_RED_MAX"]:
                BLOOD_SUGAR_COLOR = RED
                result['BLOOD_SUGAR_COLOR'] = BLOOD_SUGAR_COLOR
              else:
                msg = f'Blood pressure(dia) value should be between {triaging_values["BLOOD_SUGAR_GREEN_MIN"]} and {triaging_values["BLOOD_SUGAR_RED_MAX"]}'
                return JsonResponse({'msg': msg}, safe=False, status=400)



            # For Blood Hemoglobin triaging
            if 'blood_hemoglobin' in data.keys():
              if data['blood_hemoglobin'] < triaging_values["BLOOD_HEMOGLOBIN_GREEN_MIN"] and data['blood_hemoglobin']>=triaging_values["BLOOD_HEMOGLOBIN_GREEN_MAX"]:
                
                BLOOD_HEMOGLOBIN_COLOR = GREEN
                result['BLOOD_HEMOGLOBIN_COLOR'] = BLOOD_HEMOGLOBIN_COLOR
              elif data['blood_hemoglobin'] < triaging_values["BLOOD_HEMOGLOBIN_YELLOW_MIN"] and data['blood_hemoglobin'] >= triaging_values["BLOOD_HEMOGLOBIN_YELLOW_MAX"]:
                
                BLOOD_HEMOGLOBIN_COLOR = YELLOW
                result['BLOOD_HEMOGLOBIN_COLOR'] = BLOOD_HEMOGLOBIN_COLOR
              elif data['blood_hemoglobin'] < triaging_values["BLOOD_HEMOGLOBIN_ORANGE_MIN"] and data['blood_hemoglobin'] >= triaging_values["BLOOD_HEMOGLOBIN_ORANGE_MAX"]:
                
                BLOOD_HEMOGLOBIN_COLOR = ORANGE
                result['BLOOD_HEMOGLOBIN_COLOR'] = BLOOD_HEMOGLOBIN_COLOR
              elif data['blood_hemoglobin'] < triaging_values["BLOOD_HEMOGLOBIN_RED_MIN"] and data['blood_hemoglobin']>=triaging_values["BLOOD_HEMOGLOBIN_RED_MAX"]:
                BLOOD_HEMOGLOBIN_COLOR = RED
                result['BLOOD_HEMOGLOBIN_COLOR'] = BLOOD_HEMOGLOBIN_COLOR
              else:
                msg = f'Blood hemoglobin value should be between {triaging_values["BLOOD_HEMOGLOBIN_RED_MAX"]} and {triaging_values["BLOOD_HEMOGLOBIN_GREEN_MIN"]}'
                return JsonResponse({'msg': msg}, safe=False, status=400)
              
            # For  Pulse Rate triaging
            if 'pulse_rate' in data.keys():
              if data['pulse_rate'] >= triaging_values["Pulse_Rate_GREEN_MIN"] and data['pulse_rate']<triaging_values["Pulse_Rate_GREEN_MAX"]:
                Pulse_Rate_COLOR = GREEN
                result['Pulse_Rate_COLOR'] = Pulse_Rate_COLOR
              elif (data['pulse_rate'] >= triaging_values["Pulse_Rate_YELLOW_MIN_1"]  and data['pulse_rate'] < triaging_values["Pulse_Rate_YELLOW_MAX_1"] ) or (data['pulse_rate'] >= triaging_values["Pulse_Rate_YELLOW_MIN_2"] and data['pulse_rate'] < triaging_values["Pulse_Rate_YELLOW_MAX_2"]):
                Pulse_Rate_COLOR = YELLOW
                result['Pulse_Rate_COLOR'] = Pulse_Rate_COLOR
              elif (data['pulse_rate'] >= triaging_values["Pulse_Rate_ORANGE_MIN_1"] and data['pulse_rate'] < triaging_values["Pulse_Rate_ORANGE_MIN_2"])  or (data['pulse_rate'] >= triaging_values["Pulse_Rate_ORANGE_MAX"] and data['pulse_rate'] < triaging_values["Pulse_Rate_RED_MIN"]):
                Pulse_Rate_COLOR = ORANGE
                result['Pulse_Rate_COLOR'] = Pulse_Rate_COLOR
              elif data['pulse_rate'] >= triaging_values["Pulse_Rate_RED_MIN"] and data['pulse_rate']<triaging_values["Pulse_Rate_RED_MAX"]:
                Pulse_Rate_COLOR = RED
                result['Pulse_Rate_COLOR'] = Pulse_Rate_COLOR
              else:
                msg = f'Pulse rate value should be between {triaging_values["Pulse_Rate_ORANGE_MIN_1"]} and {triaging_values["Pulse_Rate_RED_MAX"]}'
                return JsonResponse({'msg': msg}, safe=False, status=400)

            # For  Blood cholesterol Rate triaging
            if 'blood_cholesterol' in data.keys():
              if data['blood_cholesterol'] >= triaging_values["Blood_Cholesterol_GREEN_MIN"] and data['blood_cholesterol']<triaging_values["Blood_Cholesterol_GREEN_MAX"]:
                BLOOD_CHOLESTEROL_COLOR = GREEN
                result['BLOOD_CHOLESTEROL_COLOR'] = BLOOD_CHOLESTEROL_COLOR
              elif data['blood_cholesterol'] >= triaging_values["Blood_Cholesterol_YELLOW_MIN"] and data['blood_cholesterol'] < triaging_values["Blood_Cholesterol_YELLOW_MAX"]:
                BLOOD_CHOLESTEROL_COLOR = YELLOW
                result['BLOOD_CHOLESTEROL_COLOR'] = BLOOD_CHOLESTEROL_COLOR
              elif data['blood_cholesterol'] >= triaging_values["Blood_Cholesterol_ORANGE_MIN"] and data['blood_cholesterol'] < triaging_values["Blood_Cholesterol_ORANGE_MAX"]:
                BLOOD_CHOLESTEROL_COLOR = ORANGE
                result['BLOOD_CHOLESTEROL_COLOR'] = BLOOD_CHOLESTEROL_COLOR
              elif data['blood_cholesterol'] >= triaging_values["Blood_Cholesterol_RED_MIN"]  and data['blood_cholesterol']< triaging_values["Blood_Cholesterol_RED_MAX"]:
                BLOOD_CHOLESTEROL_COLOR = RED
                result['BLOOD_CHOLESTEROL_COLOR'] = BLOOD_CHOLESTEROL_COLOR
              else:
                msg = f'Blood cholesterol value should be between {triaging_values["Blood_Cholesterol_GREEN_MIN"]} and {triaging_values["Blood_Cholesterol_RED_MAX"]}'
                return JsonResponse({'msg': msg}, safe=False, status=400)

            # For  Blood uric acid triaging
            if 'blood_uric_acid' in data.keys():
              if data['blood_uric_acid'] >= triaging_values["Blood_Uric_Acid_GREEN_MIN"] and data['blood_uric_acid']<triaging_values["Blood_Uric_Acid_GREEN_MAX"]:
                BLOOD_URIC_ACID_COLOR = GREEN
                result['BLOOD_URIC_ACID_COLOR'] = BLOOD_URIC_ACID_COLOR
              
              elif data['blood_uric_acid'] > triaging_values["Blood_Uric_Acid_ORANGE_MIN"]  and data['blood_uric_acid'] < triaging_values["Blood_Uric_Acid_ORANGE_MAX"]:
                BLOOD_URIC_ACID_COLOR = ORANGE
                result['BLOOD_URIC_ACID_COLOR'] = BLOOD_URIC_ACID_COLOR
              elif data['blood_uric_acid'] >= triaging_values["Blood_Uric_Acid_RED_MIN"] and data['blood_uric_acid']<triaging_values["Blood_Uric_Acid_RED_MAX"]:
                BLOOD_URIC_ACID_COLOR = RED
                result['BLOOD_URIC_ACID_COLOR'] = BLOOD_URIC_ACID_COLOR
              else:
                msg = f'Blood uric acid value should be between {triaging_values["Blood_Uric_Acid_GREEN_MIN"]} and {triaging_values["Blood_Uric_Acid_RED_MAX"]}'
                return JsonResponse({'msg': msg}, safe=False, status=400)


            elif len(data) == None:
              return JsonResponse({'msg': 'To triage the features, there should be features!'}, safe=False, status=400)

            if RED in result.values(): 
              result["HEALTH_STATUS_COLOR"] = RED
            elif ORANGE in result.values():
              result["HEALTH_STATUS_COLOR"] = ORANGE
            elif YELLOW in result.values():
              result["HEALTH_STATUS_COLOR"] = YELLOW
            elif GREEN in result.values():
              result["HEALTH_STATUS_COLOR"] = GREEN
              
              
            return Response(result, status=status.HTTP_200_OK)

        except:
            return JsonResponse({'msg': ' Json format input invalid !'}, safe=False, status=400)
    else:
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)


