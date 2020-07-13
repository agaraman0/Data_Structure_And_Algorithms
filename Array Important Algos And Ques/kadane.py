def maxSubArray(arr):
        
        mxend = 0
        mx = 0
        flg = 1
        for i in arr:
            
            mxend = mxend + i
            
            if mxend<0:
                mxend = 0
            if mxend>0:
                flg = 0
            mx = max(mx,mxend)
                
        if flg:
            return max(arr)
        return mx