from enum import unique

from django.contrib.auth import authenticate
from django.db.models import ForeignKey

from rest_framework import serializers


from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.isa_active:
            return user
        raise serializers.ValidationError('Неверные учетные данные')


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileSimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id','first_name','last_name']

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class ProductPhotosSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductPhotos
        fields = ['images']

class RatingSerializers(serializers.ModelSerializer):
    user = UserProfileSimpleSerializers()
    class Meta:
        model = Rating
        fields = ['user','stars',]



class ReviewSerializers(serializers.ModelSerializer):
    author = UserProfileSerializers()
    created_date = serializers.DateTimeField(format='%d-%m-%Y %H:%M')
    class Meta:
        model = Review
        fields = ['id','author','text', 'perent_review','created_date']


class ProductListSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    category = CategorySerializers()

    class Meta:
        model = Product
        fields = ['id','product_name','product','category','price','average_rating','date']

    def get_average_rating(self,obj):
            return obj.get_average_rating()

class ProductSerializers(serializers.ModelSerializer):

    category = CategorySerializers()
    rating = RatingSerializers(read_only=True, many=True)
    reviews = ReviewSerializers(read_only=True, many=True)
    product = ProductPhotosSerializers(read_only=True, many=True)
    date = serializers.DateField(format='%d-%m-%Y')
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['product_name','category','description','price','product','product_video','active','average_rating',
                  'date', 'rating','reviews']

    def get_average_rating(self, obj):
        return obj.get_average_rating()