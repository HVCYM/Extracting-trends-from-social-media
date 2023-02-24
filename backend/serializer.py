from rest_framework import serializers
from .models import Card,HashtagList,Uploadfile

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields=["id","Category","url","Tweet_Text","Trend_score","IMAGE_URL","video_img_url", "item_id","Brand","Sub_Category","Flipkart_url","product_image_link","product_title"]

        # def create(self, validated_data):
        #     return Card.objects.create(**validated_data)
class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = HashtagList
        fields=["item_id","hash_tag"]

class UploadfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uploadfile
        fields=["file"]
