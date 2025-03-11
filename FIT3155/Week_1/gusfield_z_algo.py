def calc_z_score(txt: str) -> list[int]:
    """
    Problem Statement: Given a string txt and a pattern p, find all occurences of p in txt and output the repsective indexes
    Input: txt and p
    Output: List of integers
    """
    res = []*len(txt)
    l = 0
    r = 0

    for k in range(1, len(txt)):
        if k > r:
            curr_z_score = 0
            for i in range(0, len(txt)):
                if txt[0+i] == txt[k+i]: curr_z_score += 1
                else: break
            
            if curr_z_score > 0: l,r = min(l, k), k+i-1

        else: res[k] = 0

txt = "aabcaabxaaaz"
calc_z_score(txt)