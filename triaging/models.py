from django.db import models

# Create your models here.
class TriagingSettings(models.Model):
    
    # For BMI
    BMI_GREEN_MIN = models.DecimalField(default=17, max_digits=9, decimal_places=3)
    BMI_GREEN_MAX = models.DecimalField(default=25, max_digits=9, decimal_places=3)
    BMI_YELLOW_MIN = models.DecimalField(default=25, max_digits=9, decimal_places=3)
    BMI_YELLOW_MAX = models.DecimalField(default=30, max_digits=9, decimal_places=3)
    BMI_ORANGE_MIN = models.DecimalField(default=30, max_digits=9, decimal_places=3)
    BMI_ORANGE_MAX = models.DecimalField(default=35, max_digits=9, decimal_places=3)
    BMI_RED_MIN = models.DecimalField(default=35, max_digits=9, decimal_places=3)
    BMI_RED_MAX = models.DecimalField(default=45, max_digits=9, decimal_places=3)
    
    # For WAIST/HIP RATIO
    WAIST_HIP_RATIO_GREEN_MIN = models.DecimalField(default=0.70, max_digits=9, decimal_places=3)
    WAIST_HIP_RATIO_GREEN_MAX = models.DecimalField(default=0.90, max_digits=9, decimal_places=3)
    WAIST_HIP_RATIO_YELLOW_MIN = models.DecimalField(default=0.90, max_digits=9, decimal_places=3)
    WAIST_HIP_RATIO_YELLOW_MAX = models.DecimalField(default=1, max_digits=9, decimal_places=3)  
    
    #For BODY TEMPERATURE 
    TEMPERATURE_GREEN_MIN = models.DecimalField(default=33, max_digits=9, decimal_places=3)
    TEMPERATURE_GREEN_MAX = models.DecimalField(default=37, max_digits=9, decimal_places=3)
    TEMPERATURE_YELLOW_MIN = models.DecimalField(default=37, max_digits=9, decimal_places=3)
    TEMPERATURE_YELLOW_MAX = models.DecimalField(default=37, max_digits=9, decimal_places=3)
    TEMPERATURE_ORANGE_MIN = models.DecimalField(default=37, max_digits=9, decimal_places=3)
    TEMPERATURE_ORANGE_MAX = models.DecimalField(default=38, max_digits=9, decimal_places=3)
    TEMPERATURE_RED_MIN = models.DecimalField(default=38, max_digits=9, decimal_places=3)
    TEMPERATURE_RED_MAX = models.DecimalField(default=42, max_digits=9, decimal_places=3)
    
    #For SPO2 
    SPO2_GREEN_MIN = models.DecimalField(default=96, max_digits=9, decimal_places=3)
    SPO2_GREEN_MAX = models.DecimalField(default=100, max_digits=9, decimal_places=3)
    SPO2_YELLOW_MIN = models.DecimalField(default=93, max_digits=9, decimal_places=3)
    SPO2_YELLOW_MAX = models.DecimalField(default=96, max_digits=9, decimal_places=3)
    SPO2_ORANGE_MIN = models.DecimalField(default=90, max_digits=9, decimal_places=3)
    SPO2_ORANGE_MAX = models.DecimalField(default=93, max_digits=9, decimal_places=3)
    SPO2_RED_MIN = models.DecimalField(default=90, max_digits=9, decimal_places=3)
    SPO2_RED_MAX = models.DecimalField(default=85, max_digits=9, decimal_places=3)
    
    # For BP sys
    BP_SYS_GREEN_MIN = models.DecimalField(default=95, max_digits=9, decimal_places=3)
    BP_SYS_GREEN_MAX = models.DecimalField(default=130, max_digits=9, decimal_places=3)
    BP_SYS_YELLOW_MIN = models.DecimalField(default=130, max_digits=9, decimal_places=3)
    BP_SYS_YELLOW_MAX = models.DecimalField(default=140, max_digits=9, decimal_places=3)
    BP_SYS_ORANGE_MIN = models.DecimalField(default=140, max_digits=9, decimal_places=3)
    BP_SYS_ORANGE_MAX = models.DecimalField(default=180, max_digits=9, decimal_places=3)
    BP_SYS_RED_MIN = models.DecimalField(default=180, max_digits=9, decimal_places=3)
    BP_SYS_RED_MAX = models.DecimalField(default=200, max_digits=9, decimal_places=3)
    
    # For BP dia
    BP_DIA_GREEN_MIN = models.DecimalField(default=75, max_digits=9, decimal_places=3)
    BP_DIA_GREEN_MAX = models.DecimalField(default=85, max_digits=9, decimal_places=3)
    BP_DIA_YELLOW_MIN = models.DecimalField(default=85, max_digits=9, decimal_places=3)
    BP_DIA_YELLOW_MAX = models.DecimalField(default=90, max_digits=9, decimal_places=3)
    BP_DIA_ORANGE_MIN = models.DecimalField(default=90, max_digits=9, decimal_places=3)
    BP_DIA_ORANGE_MAX = models.DecimalField(default=110, max_digits=9, decimal_places=3)
    BP_DIA_RED_MIN = models.DecimalField(default=110, max_digits=9, decimal_places=3)
    BP_DIA_RED_MAX = models.DecimalField(default=120, max_digits=9, decimal_places=3)
    
    # For Blood Sugar
    BLOOD_SUGAR_GREEN_MIN = models.DecimalField(default=3, max_digits=9, decimal_places=3)
    BLOOD_SUGAR_GREEN_MAX = models.DecimalField(default=7.78, max_digits=9, decimal_places=3)
    BLOOD_SUGAR_YELLOW_MIN = models.DecimalField(default=7.78, max_digits=9, decimal_places=3)
    BLOOD_SUGAR_YELLOW_MAX = models.DecimalField(default=11.11, max_digits=9, decimal_places=3)
    BLOOD_SUGAR_ORANGE_MIN = models.DecimalField(default=11.11, max_digits=9, decimal_places=3)
    BLOOD_SUGAR_ORANGE_MAX = models.DecimalField(default=16.67,max_digits=9, decimal_places=3)
    BLOOD_SUGAR_RED_MIN = models.DecimalField(default=16.67, max_digits=9, decimal_places=3)
    BLOOD_SUGAR_RED_MAX = models.DecimalField(default=30, max_digits=9, decimal_places=3)
    
    # For Blood HEMOGLOBIN
    BLOOD_HEMOGLOBIN_GREEN_MIN = models.DecimalField(default=18,max_digits=9, decimal_places=3)
    BLOOD_HEMOGLOBIN_GREEN_MAX = models.DecimalField(default=12,max_digits=9, decimal_places=3)
    BLOOD_HEMOGLOBIN_YELLOW_MIN = models.DecimalField(default=12,max_digits=9, decimal_places=3)
    BLOOD_HEMOGLOBIN_YELLOW_MAX = models.DecimalField(default=10,max_digits=9, decimal_places=3)
    BLOOD_HEMOGLOBIN_ORANGE_MIN = models.DecimalField(default=10,max_digits=9, decimal_places=3)
    BLOOD_HEMOGLOBIN_ORANGE_MAX = models.DecimalField(default=8,max_digits=9, decimal_places=3)
    BLOOD_HEMOGLOBIN_RED_MIN = models.DecimalField(default=8,max_digits=9, decimal_places=3)
    BLOOD_HEMOGLOBIN_RED_MAX = models.DecimalField(default=6,max_digits=9, decimal_places=3)
    
    # For Pulse Rate
    Pulse_Rate_GREEN_MIN = models.DecimalField(default=60, max_digits=9, decimal_places=3)
    Pulse_Rate_GREEN_MAX = models.DecimalField(default=100,max_digits=9, decimal_places=3)
    Pulse_Rate_YELLOW_MIN_1 = models.DecimalField(default=50,max_digits=9, decimal_places=3)
    Pulse_Rate_YELLOW_MAX_1 = models.DecimalField(default=60,max_digits=9, decimal_places=3)
    Pulse_Rate_YELLOW_MIN_2 = models.DecimalField(default=100,max_digits=9, decimal_places=3)
    Pulse_Rate_YELLOW_MAX_2 = models.DecimalField(default=120,max_digits=9, decimal_places=3)
    Pulse_Rate_ORANGE_MIN_1 = models.DecimalField(default=20,max_digits=9, decimal_places=3)
    Pulse_Rate_ORANGE_MIN_2 = models.DecimalField(default=50,max_digits=9, decimal_places=3)
    Pulse_Rate_ORANGE_MAX = models.DecimalField(default=120,max_digits=9, decimal_places=3)
    Pulse_Rate_RED_MIN = models.DecimalField(default=130,max_digits=9, decimal_places=3)
    Pulse_Rate_RED_MAX = models.DecimalField(default=150,max_digits=9, decimal_places=3)
    
    
    # For Blood Cholesterol
    Blood_Cholesterol_GREEN_MIN = models.DecimalField(default=120,max_digits=9, decimal_places=3)
    Blood_Cholesterol_GREEN_MAX = models.DecimalField(default=200,max_digits=9, decimal_places=3)
    Blood_Cholesterol_YELLOW_MIN = models.DecimalField(default=200,max_digits=9, decimal_places=3)
    Blood_Cholesterol_YELLOW_MAX = models.DecimalField(default=225,max_digits=9, decimal_places=3)
    Blood_Cholesterol_ORANGE_MIN = models.DecimalField(default=225,max_digits=9, decimal_places=3)
    Blood_Cholesterol_ORANGE_MAX = models.DecimalField(default=240,max_digits=9, decimal_places=3)
    Blood_Cholesterol_RED_MIN = models.DecimalField(default=240,max_digits=9, decimal_places=3)
    Blood_Cholesterol_RED_MAX = models.DecimalField(default=300,max_digits=9, decimal_places=3)

    # Blood Uric Acid 
    Blood_Uric_Acid_GREEN_MIN = models.DecimalField(default=2.5,max_digits=9, decimal_places=3)
    Blood_Uric_Acid_GREEN_MAX = models.DecimalField(default=7,max_digits=9, decimal_places=3)
    Blood_Uric_Acid_ORANGE_MIN = models.DecimalField(default=7,max_digits=9, decimal_places=3)
    Blood_Uric_Acid_ORANGE_MAX = models.DecimalField(default=8,max_digits=9, decimal_places=3)
    Blood_Uric_Acid_RED_MIN = models.DecimalField(default=8,max_digits=9, decimal_places=3)
    Blood_Uric_Acid_RED_MAX = models.DecimalField(default=16,max_digits=9, decimal_places=3)

    class Meta:
        db_table = "TriagingSettings"

