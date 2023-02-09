class Solution:
    def reformatDate(self, date: str) -> str:
        month = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}

        i = 0
       
        day = ""
        while i < len(date) and date[i].isdigit():
            day += date[i]
            i += 1
        
        while i < len(date) and date[i] != " ":
            i += 1
        i += 1
        mth = ""
        while i < len(date) and date[i] != " ":
            mth += date[i]
            i += 1
        i += 1
        
        year = ""
        while i < len(date) and date[i].isdigit():
            year += date[i]
            i += 1
        if len(day) <= 1:
            day = "0" + day
        ans = year + "-" + month[mth] + "-" + day
        
        return ans