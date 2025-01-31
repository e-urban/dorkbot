from urllib.parse import urlparse


def run(args):
    source = __name__.split(".")[-1]
    urls = [
        "http://www.example.com/foo.php?id=4",
        "http://admin.example.com/bar.php?page=home",
        "http://www.example.com/baz.jsp?size=124"
    ]

    return [urlparse(item.strip()).geturl() for item in urls], source
