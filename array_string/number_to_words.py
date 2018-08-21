"""
Convert an integer into their english versions
"""


class Solution(object):

    def __init__(self):
        self.ones = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        self.teens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        self._ty = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        self.bigglies = ['Billion', 'Million', 'Thousand']

    def numberToWords(self, num):
        """
        The idea is to always pull out the rightmost 3 digits and divide/moudulus to get the hundred, tens,
        and ones digits. Use that value as the index to their respective lists.
        :type num: int
        :rtype: str
        """
        if not num:
            return 'Zero'

        english = []
        while num:
            three = num%1000  # get the rightmost 3 digits
            english = self.compose(three) + english
            num //= 1000  # shift 3 digits to the right
            if num > 0:
                bigly = self.bigglies.pop()
                if num%1000 > 0:
                    # Consider 1,000,000,001
                    # We dont want "One Billion Million Thousand One" as result
                    english = [bigly]+english

        return ' '.join(english)
            
    def compose(self, three):
        temp = []
        hundred = three//100
        if hundred:
            temp.extend([self.ones[hundred], 'Hundred'])

        ten = three%100  # get the rightmost 2 digits
        if 10 <= ten < 20:
            # special case for teens
            if self.teens[ten%10]:
                temp.append(self.teens[ten%10])
            return temp
        else:
            if self._ty[ten//10]:
                temp.append(self._ty[ten//10])
            if self.ones[ten%10]:
                temp.append(self.ones[ten%10])
        return temp


# test case
print(Solution().numberToWords(0))
print(Solution().numberToWords(1000000001))
print(Solution().numberToWords(123))
print(Solution().numberToWords(19))
print(Solution().numberToWords(16))
print(Solution().numberToWords(40))
print(Solution().numberToWords(59))
print(Solution().numberToWords(90))
print(Solution().numberToWords(1234))
print(Solution().numberToWords(987))
print(Solution().numberToWords(123987))
print(Solution().numberToWords(10987))
print(Solution().numberToWords(11917))
print(Solution().numberToWords(198625907))
