from rest_framework import serializers
from .models import Blog, BlogComment, Rate

class BlogSerializer(serializers.ModelSerializer):
    time = serializers.TimeField(format="%-I:%M%p", read_only=True)
    date = serializers.DateField(format="%B %-d, %Y", read_only=True)
    author = serializers.CharField(source='author.username')
    class Meta:
        model = Blog
        fields = fields = ["id", "title", "content", "date", "time"]

class BlogCommentSerializer(serializers.ModelSerializer):
    time = serializers.TimeField(format="%-I:%M%p", read_only=True)
    date = serializers.DateField(format="%B %-d, %Y", read_only=True)
    class Meta:
        model = BlogComment
        fields = "__all__"

class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = "__all__"