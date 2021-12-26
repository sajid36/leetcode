class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        h, result = {}, []
        for val in cpdomains:
            arr = val.split()
            domain = arr[1]
            subdomains = {domain}
            for i in range(len(domain)):
                if domain[i] == ".":
                    subdomains.add(domain[i + 1:])
            for subdomain in subdomains:
                h[subdomain] = h.get(subdomain, 0) + int(arr[0])
        for k, v in h.items():
            result.append(str(v) + " " + k)
        return result
        