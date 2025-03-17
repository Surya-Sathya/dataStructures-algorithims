class Gusfield_Z():
    def __init__(self):
        self.tmp_counter = 0
        self.total_comp_counter = 0

    def naive_string_match(self, txt: str, idx: int) -> int:
        z_score = 0
        for i in range(0, len(txt)-idx):
            self.tmp_counter += 1
            if txt[i] == txt[idx+i]: z_score += 1
            else: break
        return z_score

    def z_algorithim(self, txt: str): 
        if len(txt) == 0: return "String is of size zero"
        res = [None]*len(txt)
        l = 0
        r = 0

        #Explicit comparison for Z2
        res[1] = self.naive_string_match(txt,1)
        if(res[1] > 0): l, r = 1, res[1]


        for k in range(2, len(txt)): 
            print(f"Iteration k:{k} uses: ", end = " Case ")
            if k > r: 
                zk_score = self.naive_string_match(txt, k)
                if(zk_score > 0): l, r = k, k+zk_score-1
                print(f"1) with {self.tmp_counter} comparisons")
                self.total_comp_counter += self.tmp_counter
                self.tmp_counter = 0

            else:
                adj_z_score = res[k-l]
                if adj_z_score < r-k+1: 
                    print("2a) with 1 comparison")
                    self.total_comp_counter += 1
                    zk_score = adj_z_score

                elif adj_z_score > r-k+1:
                    print("2b) with 1 comparison")
                    self.total_comp_counter += 1
                    zk_score = r-k+1

                elif adj_z_score == r-k+1:
                    if r+1 == len(txt): 
                        zk_score = adj_z_score
                        print("2c) with 1 comparison")
                        self.total_comp_counter += 1
                    else:
                        zk_score = self.naive_string_match(txt, r-k+1) + r-k+1
                        print(f"2c) with {self.tmp_counter} comparisons")
                        self.total_comp_counter += self.tmp_counter
                        self.tmp_counter = 0
            
            self.comparison_counter = 0
            res[k] = zk_score

        print(res)

txt = "aabcaabxaabcaabcay"
gusfield_z_method = Gusfield_Z()
gusfield_z_method.z_algorithim(txt)
print("\n", end="")
print(f"Number of comparisons with z-algo algorithim: {gusfield_z_method.total_comp_counter}, with the text length {len(txt)}\n")





