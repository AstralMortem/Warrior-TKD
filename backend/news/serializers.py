from rest_framework.serializers import ModelSerializer
from .models import News, NewsImage


class NewsImageSerializer(ModelSerializer):
    class Meta:
        model = NewsImage
        fields = ['image']

    def to_representation(self, instance):
        return str(instance.image.url)

class NewsSerializer(ModelSerializer):
    news_images = NewsImageSerializer(many=True, read_only=True)
    class Meta:
        model = News
        fields = "__all__"


