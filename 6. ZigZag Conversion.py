class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        s_len = len(s)
        if numRows == 1 or s_len <= numRows:
            return s
        
        zig_zag = [""]*numRows
        
        for idx in range(s_len):
            temp_pos = idx % (2*numRows - 2)
            pos = temp_pos if temp_pos < numRows else 2*numRows - 2 - temp_pos
            # if temp_pos < numRows:
            #     zig_zag[temp_pos] += s[idx]
            # else:
            #     zig_zag[2*numRows - 2 - temp_pos] += s[idx]
            zig_zag[pos] += s[idx]
        
        return "".join(zig_zag)
