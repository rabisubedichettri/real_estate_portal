from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# make sure model should be in order in queryset or in model
def customPagination(Serializers,queryset,page_number,page_size):
    paginator_instance = Paginator(queryset, page_size)
    try:
        data = paginator_instance.page(page_number)

    except PageNotAnInteger:
        data = paginator_instance.page(1)

    except EmptyPage:
        data = paginator_instance.page(paginator_instance.num_pages)

    serializer = Serializers(data, many=True)
    return {
        "data": serializer.data,
        "paginator": {
            "total_page": paginator_instance.num_pages,
            "current_page": page_number,
            "page_size": page_size

        }
    }