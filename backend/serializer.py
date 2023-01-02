from rest_framework import serializers
from .models import Card

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields=["id","Category","url","Tweet_Text","Trend_score","IMAGE_URL","video_img_url", "item_id","Brand","Sub_Category","Flipkart_url","product_image_link","product_title"]

        # def create(self, validated_data):
        #     return Card.objects.create(**validated_data)