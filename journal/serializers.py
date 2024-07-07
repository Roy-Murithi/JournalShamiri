# journal/serializers.py
from rest_framework import serializers
from .models import JournalEntry, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class JournalEntrySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )

    class Meta:
        model = JournalEntry
        fields = ['id', 'title', 'content', 'category', 'category_id', 'created_at', ]
        read_only_fields = ['created_at', ]

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)