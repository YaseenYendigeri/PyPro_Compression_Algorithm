import zlib, base64

def compress(i, o):
    data = open(i, "r").read()
    b = bytes(data, "utf-8")
    cp = base64.b64encode(zlib.compress(b, 9))
    d = cp.decode("utf-8")
    n = open(o, "w")
    n.write(d)


def decompress(cf, dc1):
    content = open(cf, "r").read()
    content_encode = content.encode("utf-8")
    dc = zlib.decompress(base64.b64decode(content_encode))
    k = dc.decode("utf-8")
    file = open(dc1, "w")
    file.write(k)


