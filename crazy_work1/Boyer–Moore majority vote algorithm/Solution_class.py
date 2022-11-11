class Solution:

    def __init__(self, new_num_list):
        self.num_list = new_num_list

    def printMethod(self):
        print(self.num_list)

    def findMajority(self):

        num_list = self.num_list

        majority = num_list[0]
        counter = 1

        for num in num_list[1:]:
            if counter == 0:
                majority = num
                counter += 1

            if majority == num:
                counter += 1
            else:
                counter -= 1

            print("majority=" + str(majority) + " counter=" + str(counter))

        return majority
