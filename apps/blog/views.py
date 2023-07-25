from rest_framework import viewsets, status
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from drf_util.decorators import serialize_decorator

from apps.blog.models import Category, Blog, Comments
from apps.blog.serializers import CategorySerializer, BlogSerializer, CommentSerializer
from apps.common.permissions import ReadOnly


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class BlogListView(GenericAPIView):
    serializer_class = BlogSerializer
    permission_classes = (ReadOnly,)

    def get(self, request):
        blogs = Blog.objects.all()
        return Response(BlogSerializer(blogs, many=True).data)


class BlogItemView(GenericAPIView):
    serializer_class = BlogSerializer
    permission_classes = (ReadOnly,)

    def get(self, request, pk):
        blog = get_object_or_404(Blog.objects.filter(pk=pk))
        comments = Comments.objects.filter(blog=pk)
        serializer_list = [BlogSerializer(blog).data, CommentSerializer(comments, many=True).data]

        return Response(serializer_list)


class BlogCreatePostView(GenericAPIView):
    serializer_class = BlogSerializer

    permission_classes = (AllowAny,)

    @serialize_decorator(BlogSerializer)
    def post(self, request):
        validated_data = request.serializer.validated_data

        # Create blog
        blog = Blog.objects.create(
            **validated_data,
        )

        blog.save()

        return Response(BlogSerializer(blog).data)


class CommentCreateView(GenericAPIView):
    serializer_class = CommentSerializer

    permission_classes = (AllowAny,)

    @serialize_decorator(CommentSerializer)
    def post(self, request):
        validated_data = request.serializer.validated_data

        # Create blog
        comment = Comments.objects.create(
            **validated_data,
        )

        comment.save()

        return Response(CommentSerializer(comment).data)
