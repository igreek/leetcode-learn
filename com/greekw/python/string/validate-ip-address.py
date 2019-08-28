__author__ = 'greek'

class Solution(object):

    def validIpAdress(self,IP):

        """

        :param IP:
        :return:
        """
        block=IP.split(".")
        if len(block)==4:
            for i in range(len(block)):
                if not block[i].isdigit() or not 0<=int[block[i]]<256 \
                    or (block[i][0]==0 and len(block[i]))>1:
                        return "Neither"
                return True
        if(len(block)==8):
            for i in range(len(block)):

                return "IPV6"

        return "Neither"


if __name__=="__main__":

    s=Solution();
    print(s.validIpAdress("192.168.0.1"))