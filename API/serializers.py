
from rest_framework import serializers
from API.models import Products
from django.contrib.auth.models import User
from API.models import Carts
class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    price=serializers.IntegerField()
    description=serializers.CharField()
    category=serializers.CharField()
    image=serializers.ImageField(required=False,default=None)

class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:

        model = Products
        fields = "__all__"
        #fields = ["name","price","description"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:

        model = User
        fields = ["first_name","last_name","email","username","password"]

    def create(self,validated_data):
        return User.objects.create_user(**self.validated_data)
class CartSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only = True)
    user = serializers.CharField(read_only = True)
    product = serializers.CharField(read_only = True)
    date = serializers.CharField(read_only = True)
    class Meta:

        model = Carts
        fields = "__all__"






