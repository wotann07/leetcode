# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


class LongestSubstring:
    @staticmethod
    def get_length_of_longest_substring(s: str):
        """
        :type s: str
        :rtype: int
        """

        holder = ''
        longest = ''
        for i, c in enumerate(s):
            hit = holder.find(c)
            if hit is -1:
                holder += c
            else:
                if len(holder) >= len(longest):
                    longest = holder

                holder = holder[hit + 1:] + c

        return len(longest) if len(longest) > len(holder) else len(holder)

    @staticmethod
    def get_length_of_longest_substring_hash(s: str):
        """
        :type s: str
        :rtype: int
        """

        # using a set for non repetition
        letters = set([c for c in s])
        chars = dict.fromkeys(letters, -1)
        len_holder = 0
        max_len = 0
        point_0 = -1
        for i, c in enumerate(s):
            point_holder = chars[c]
            chars[c] = i
            if point_holder <= point_0:
                len_holder += 1
            else:
                point_0 = point_holder
                if len_holder > max_len:
                    max_len = len_holder

                len_holder = i - point_holder

        return max(len_holder, max_len)
