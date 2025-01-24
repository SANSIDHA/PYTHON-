def test(lst_tuples):
    result=[list(el)for el in list_tuples]
    return result
lst_tuples=[(1,2),(2,3),(3,4)]
print("original list of tuples:")
print(lst_tuples)
print("convert the said list of tuples to a list of lists.")
print(test(lst_tuples))
lst_tuples=[(1,2),(2,3,5),(3,4),(2,3,4,2)]
print("\noriginal list of tuples")
print(lst_tuples)
print("convert the said list of tuples to a list of lists:")
print(test(lst_tuples))
inttuple=0
number=int(input("please enter the total tuple items to store="))
for i in range(1,number+1):
    value=int(input("please enter %d binary tuple item="%i))
inttuple+=(value,)
print("tuple items=",inttuple)
res=int("".join(str(ele)for ele in inttuple),2)
print("decimal number is:"+str(res))
