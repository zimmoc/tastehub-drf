from django.contrib.humanize.templatetags.humanize import naturaltime
from likes.models import Like
from rest_framework import serializers
from recipes.models import Recipe
from ratings.models import Rating
from django.db.models import Avg


class RecipeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()
    ratings_count = serializers.ReadOnlyField()
    ratings_average = serializers.ReadOnlyField()

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, recipe=obj
            ).first()
            return like.id if like else None
        return None
    
    def get_created_at(self, obj):
        return naturaltime(obj.created_at)
    
    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)
    
    def update(self, instance, validated_data):
        request = self.context.get('request')
        if request and 'no_new_image' in request.data:
            validated_data.pop('image', None)
        return super().update(instance, validated_data)


    class Meta:
        model = Recipe
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'title', 'description',
            'image', 'ingredients', 'instructions', 'is_owner', 'profile_id',
            'profile_image', 'like_id', 'likes_count', 'comments_count', 'ratings_count',
            'ratings_average'
        ]