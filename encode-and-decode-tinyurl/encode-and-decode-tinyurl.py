class Codec:

    mapping = {}
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.mapping = {}
        self.mapping[abs(hash(longUrl)) % (10 ** 8)] = longUrl
        #print(self.mapping)
        #print(str(list(self.mapping.keys())[0]))
        return str(list(self.mapping.keys())[0])

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        #lastSlash = ''.join(shortUrl).rindex('/')
        key = shortUrl
        #print(key)
        key = ''.join(key.split())
        #print(self.mapping[key])
        return self.mapping[int(key)]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))