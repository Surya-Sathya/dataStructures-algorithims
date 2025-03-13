def calc_z_score(txt: str) -> list[int]:
    """
    Problem Statement: Given a string txt and a pattern p, find all occurences of p in txt and output the repsective indexes
    Input: txt and p
    Output: List of integers
    """
    res = [None]*len(txt)
    l = 0
    r = 0

    for k in range(1, len(txt)):
        print(f"k-value: {k}")


        if k > r:
            curr_z_score = 0
            for i in range(0, len(txt)-k):
                if txt[0+i] == txt[k+i]: curr_z_score += 1
                else: 
                    res[k] = curr_z_score
                    break
            if curr_z_score > 0: l,r = min(l, k), k+i-1
            print(f"With z score of: {curr_z_score}\n")


        elif k <= r: 
            z = res[k-l]
            print(f"k: {k} <= r: {r}, with associated Z-score value of: {z}")

            #Size of z-box within z'-box: Proper subset of z-box, hence can't be any bigger
            #By definition, if it was bigger, it would be bigger
            if z < r-k: res[k] = z

            if z > r-k: res[k] = z

            if z == r-k:
                curr_z_score = 0
                for i in range(0, len(txt)-k):
                    if txt[0+i] == txt[k+i]: curr_z_score += 1
                    else: 
                        res[k] = curr_z_score
                        break
                if curr_z_score > 0: l,r = min(l, k), k+i-1
                print(f"With z score of: {curr_z_score}\n")     

        else: res[k] = "Undetermined case"

    return res

txt = "aabcaabxaaaz"
print(calc_z_score(txt))