# Bad solution

# class Solution:
#     def invalidTransactions(self, transactions):
#         result_flag = [False] * len(transactions)
#         result = []
#         for i in transactions:
#             data = i.split(',')
#             name = data[0]
#             time = data[1]
#             amount = data[2]
#             city = data[3]
#             if int(amount) > 1000:
#                 result_flag[transactions.index(i)] = True
#             for j in transactions:
#                 data2 = j.split(',')
#                 name2 = data2[0]
#                 if i == j or name != name2:
#                     continue
#                 else:
#                     time2 = data2[1]
#                     # amount = data2[2]
#                     city2 = data2[3]
#                     if city != city2 and abs(int(time2) - int(time)) <= 60:
#                         result_flag[transactions.index(j)] = True
#         for k in range(len(transactions)):
#             if result_flag[k]:
#                 result.append(transactions[k])
#         return result
#


class Solution:
    def invalidTransactions(self, transactions):
        result_flag = [False] * len(transactions)
        result = []
        for i in transactions:
            data = i.split(',')
            name = data[0]
            time = data[1]
            amount = data[2]
            city = data[3]
            if int(amount) > 1000:
                result_flag[transactions.index(i)] = True
            for j in transactions:
                data2 = j.split(',')
                name2 = data2[0]
                if i == j or name != name2:
                    continue
                else:
                    time2 = data2[1]
                    # amount = data2[2]
                    city2 = data2[3]
                    if city != city2 and abs(int(time2) - int(time)) <= 60:
                        result_flag[transactions.index(j)] = True
        for k in range(len(transactions)):
            if result_flag[k]:
                result.append(transactions[k])
        return result


solution = Solution()
print(solution.invalidTransactions(["alice,20,800,mtv", "bob,50,1200,mtv"]))
