# creating serializers for login app and models
from rest_framework import serializers

from .models import Companyinfo

''' creating serializer class for SessionModel with named 
SessionSerializers with below criteria '''


class CompanyinfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Companyinfo
        fields = ('company_id', 'company_name', 'ceo_name', 'email','number','website','address','status','company_created_by')


class GetCompanyDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Companyinfo
        fields = ('company_id', )
    
class GetCompanyBasedListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Companyinfo
        fields = ( 'company_name', )
        


class DeleteCompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = Companyinfo
        fields = ('company_id', )
        

class UpdateCompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = Companyinfo
        fields = ('company_id', 'company_name', 'ceo_name', 'email','number','website','address','status','company_created_by')