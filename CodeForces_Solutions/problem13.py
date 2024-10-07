n,k,l,c,d,p,nl,np = map(int, input().split())

total_drinks = k*l
total_limes = c*d
total_salt = p

total_toasts = min(total_drinks//nl, total_limes, total_salt//np)//n

print(total_toasts)