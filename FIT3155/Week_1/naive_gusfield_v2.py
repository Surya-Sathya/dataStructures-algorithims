class Gusfield_Z():
    def __init__(self):
        self.comparison_counter = 0
        self.total_comp_counter = 0

    def naive_string_match(self, txt: str, idx: int) -> int:
        z_score = 0
        for i in range(0, len(txt)-idx):
            #print(f"Comparing txt[{i}] with txt[{idx+i}]")
            self.comparison_counter += 1
            self.total_comp_counter += 1
            if txt[i] == txt[idx+i]: z_score += 1
            else: 
                #print("Mismatch!")
                break
        #print(f"Z_score = {z_score} for Index: {idx}")
        return z_score

    def quadratic_string(self, txt: str): 
        res = [None]*len(txt)
        for i in range(1, len(txt)): res[i] = self.naive_string_match(txt, i)
        print(res)

    def z_algorithim(self, txt: str): 
        if len(txt) == 0: return "String is of size zero"
        res = [None]*len(txt)
        l = 0
        r = 0


        #Explicit comparison for Z2
        res[1] = self.naive_string_match(txt,1)
        if(res[1] > 0): l, r = 1, res[1]
        print(f"Iteration: {1}, with a comparison count of: {1 if self.comparison_counter == 0 else self.comparison_counter}")
        #print(f"Left point of furthest box: {l} and Right point of furthest box: {r}\n")


        for k in range(2, len(txt)): 
            print(f"Iteration: {k}", end=", with a comparison count of: ")
            #Case 1) Zk is greater than the rightmost point of the furthest z-box
            if k > r: 
                zk_score = self.naive_string_match(txt, k)
                if(zk_score > 0): l, r = k, k+zk_score-1

            else:
                adj_z_score = res[k-l]
                if adj_z_score < r-k+1: zk_score = adj_z_score

                elif adj_z_score > r-k+1: zk_score = r-k+1

                elif adj_z_score == r-k+1:
                    if r+1 == len(txt): zk_score = adj_z_score
                    else:
                        zk_score = self.naive_string_match(txt, r-k+1) + r-k+1
            
            print(1 if self.comparison_counter == 0 else self.comparison_counter)
            self.comparison_counter = 0
            res[k] = zk_score

            #print(f"Left point of furthest box: {l} and Right point of furthest box: {r}\n")

        print(res)

txt = "aabcaabxaabcaabcay"
# naive_method = Gusfield_Z()
# naive_method.quadratic_string(txt)
# print(f"Number of comparisons with naive algorithim: {naive_method.comparison_counter} \n")

gusfield_z_method = Gusfield_Z()
gusfield_z_method.z_algorithim(txt)
print("\n", end="")
print(f"Number of comparisons with z-algo algorithim: {gusfield_z_method.total_comp_counter}")
print(f"Length of text = {len(txt)}")





