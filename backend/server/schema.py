from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from server.serializers import ChannelSerializer, ServerSerializer


server_lis_doc = extend_schema(
    responses=ServerSerializer(many=True), parameters=[
        OpenApiParameter(name="category", type=OpenApiTypes.STR, location=OpenApiParameter.QUERY, description="category name of server to retrieve."),
        OpenApiParameter(name="qty", type=OpenApiTypes.STR, location=OpenApiParameter.QUERY, description="number of server to retrieve."),
        OpenApiParameter(name="by_user", type=OpenApiTypes.BOOL, location=OpenApiParameter.QUERY, description="filter server by current user authenticate (true/false)."),
        OpenApiParameter(name="with_num_members", type=OpenApiTypes.BOOL, location=OpenApiParameter.QUERY, description="include numbers of members in servers (true/false)"),
        OpenApiParameter(name="by_serverid", type=OpenApiTypes.INT, location=OpenApiParameter.QUERY, description="include server by id")
        
    ]
)