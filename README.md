Markdown测试：

    def detail(request, pk):
        artical = get_object_or_404(Artical, pk=pk)
        artical.content = markdown.markdown(artical.content, extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
        return render(request, 'flyingzone/detail.html', context={'artical': artical})