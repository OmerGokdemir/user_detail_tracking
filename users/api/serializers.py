from rest_framework import serializers
from django.contrib.auth import get_user_model
from users.models import Geo, Address, Company
import re
from django.contrib.auth import authenticate



User = get_user_model()

class GeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geo
        fields = ["lat", "lng"]
        
        
class AddressSerializer(serializers.ModelSerializer):
    geo = GeoSerializer()
    
    class Meta:
        model = Address
        fields = ["street", "suite", "city", "zipcode", "geo"]
        
    
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["name"]
        

class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    company = CompanySerializer()
    password = serializers.CharField(write_only=True, default="Test321.")
    
    class Meta:
        model = User
        fields = ["id", "name", "username", "email", "password", "address", "phone", "website", "company"]
        
    def create(self, validated_data):

        address_data = validated_data.pop("address", None)
        company_data = validated_data.pop("company", None)
        
        password = validated_data.pop("password", "Test321.")

        user = User.objects.create(**validated_data)
        user.set_password(password)

        if address_data:
            geo_data = address_data.pop("geo", None)
            if geo_data:
                geo = Geo.objects.create(**geo_data)
                address_data["geo"] = geo
            address = Address.objects.create(**address_data)
            user.address = address

        if company_data:
            company = Company.objects.create(**company_data)
            user.company = company

        user.save()
        return user
        
    
    
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)
    
    def validate(self, data):
        new_password = data.get("new_password")
        confirm_password = data.get("confirm_password")
        if new_password != confirm_password:
            raise serializers.ValidationError("New Password and Confirm Password do not match.")
        return data
    
    def validate_new_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("The new password must be at least 8 characters long.")
        if not re.search(r"[A-Z]", value):
            raise serializers.ValidationError("The new password must include at least one uppercase letter (A-Z).")
        if not re.search(r"[a-z]", value):
            raise serializers.ValidationError("The new password must include at least one lowercase letter (a-z).")
        if not re.search(r"[0-9]", value):
            raise serializers.ValidationError("The new password must include at least one digit (0-9).")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
            raise serializers.ValidationError("The new password must include at least one special character (e.g., @, #, $, etc.).")

        return value
        
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        email = data.get("email")
        password = data.get("password")
        
        if email and password:
            user = authenticate(request=self.context.get("request"), email=email, password=password)
            
            if not user:
                raise serializers.ValidationError("Invalid email or password.")
            
        else:
            raise serializers.ValidationError("Both email and password are required.")
        
        data["user"] = user
        return data