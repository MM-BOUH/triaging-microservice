# Smart Gant Chart(Triaging microservice)


## Introduction
This repository is for th Smart Gantt Chart for Health Events. It contains the backend microservices.

## Tech We Have Used

We have used :
- Django
- Django Rest Framework
- SQLite
- Swager for documenting the APIs

<br>

## Getting started 
[To access the documentation]
your_domain/documentation 
example : localhost/documentation

[In order to update the triaging values], you can visit : DN/smart-gantt-chart-admin/
example : localhost/smart-gantt-chart-admin/

### For django credentials 
username : gant-admin
password : gant-admin1245


## How to do an API call to this microservice?
This endpoint should be called in order to connect with the microservice : site_name/triaging/feature-color
`Request format example`
``` 
{
              "bmi":37,
              "waist_hip_ratio": 0.9,
              "temperature": 36,
              "spo2":86,
              "bp_sys":180, 
              "bp_dia": 115,
              "blood_sugar":17,
              "blood_hemoglobin":7,
              "pulse_rate":30,
              "blood_cholesterol": 230,
              "blood_uric_acid": 14
}

``` 
`It is important to note that an API key has been added to this microservice. This key should be sent through the header of the request as below: `
```
{
    Authorization: "Bearer API_KEY"
}
```
P.S: The bearer and the KEY would be sent privately

`
Here is what to expect as a Response 
`
```
{
  "BMI_COLOR": "red",
  "WAIST_HIP_RATIO_COLOR": "yellow",
  "TEMPERATURE_COLOR": "green",
  "SPO2_COLOR": "red",
  "BP_SYS_COLOR": "red",
  "BP_DIA_COLOR": "red",
  "BLOOD_SUGAR_COLOR": "red",
  "BLOOD_HEMOGLOBIN_COLOR": "red",
  "Pulse_Rate_COLOR": "orange",
  "BLOOD_CHOLESTEROL_COLOR": "orange",
  "BLOOD_URIC_ACID_COLOR": "red",
  "HEALTH_STATUS_COLOR": "red"
}
```
`Note that that the endpoint accepts also one/multiple features by request`

