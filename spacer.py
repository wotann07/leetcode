class Spacer:
    @staticmethod
    def space_out_worker(sentence: str, word_dict: set):
        sol = []
        for j in range(1, len(sentence) + 1):
            word = sentence[:j]
            if word in word_dict:
                next_sentence = sentence[j:]
                if len(next_sentence) == 0:
                    sol.append(word)
                    return sol
                else:
                    tmp = Spacer.space_out_worker(next_sentence, word_dict)
                    if len(tmp) > 0:
                        sol.append(word)
                        sol += tmp
                        return sol
        return sol

    @staticmethod
    def space_out(sentence: str, word_dict: set):
        sol = Spacer.space_out_worker(sentence, word_dict)
        if len(sol) > 0:
            return ' '.join(sol)
