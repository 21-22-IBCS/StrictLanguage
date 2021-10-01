def main():
    
    def sleep_in(weekday, vacation):
      if not weekday or vacation :
        return True
      else:
        return False
    
    def monkey_trouble(a_smile, b_smile):
      if a_smile == b_smile:
        return True
      else:
        return False

    def sum_double(a, b):
      if a == b:
        return (2*(a+b))
      else:
        return(a+b)

    def diff21(n):
      if n <= 21:
        return (21-n)
      else:
        return 2*(n-21)

    def parrot_trouble(talking, hour):
      if talking and (hour >20 or hour< 7):
        return True
      else:
        return False

    def makes10(a, b):
      if (a == 10 or b ==10) or a+b==10:
        return True
      else:
        return False

    def near_hundred(n):
      if abs(n-100) <=10 or abs(n-200) <= 10:
        return True
      else:
        return False

    def pos_neg(a, b, negative):
      if ((a>0 and b<0) or (a<0 and b>0)) and not negative:
        return True
      elif negative and (a<0 and b <0):
        return True
      else:
        return False

    def not_string(str):
      if str[:3] =="not":
        return str
      else:
        return ("not " +str )

    def missing_char(str, n):
      return str[0:n]+str[n+1:]

    def front_back(str):
      if len(str) >1 :
       return str[len(str)-1]+str[1:len(str)-1]+str[0]
      else:
        return str

    def front3(str):
      if len(str)<3:
        return str+str+str
      else:
        return str[0:3]+str[0:3]+str[0:3]




    

if __name__ == "__main__":
    main()
