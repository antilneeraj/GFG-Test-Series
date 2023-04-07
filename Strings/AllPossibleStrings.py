def spaceString(str):
    def backtrack(index, current_str):
        if index == len(str):
            result.append(current_str)
            return
     
        backtrack(index + 1, current_str + str[index])
 
        if index < len(str) - 1:
            backtrack(index + 1, current_str + str[index] + " ")

    result = []
    backtrack(0, "")
    return sorted(result, reverse=True)
