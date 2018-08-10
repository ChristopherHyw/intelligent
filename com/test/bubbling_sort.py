class bubbing_sorts:
    def __index__(self):
        pass

    def b_s(self,a):
        for i in range(0, len(a) - 1):
            for j in range(0, len(a) - i - 2):
                if a[j] > a[j + 1]:
                    n = a[j]
                    a[j] = a[j + 1]
                    a[j + 1] = n
        return a

