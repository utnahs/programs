cls
print "enter -1 to stop entering values"
dim a(100)
dim n as integer 
while i < 100
    input "enter val ",n
    if n = -1 then 
        exit while
    end if 
    a(i) = n 
    i = i+1
wend
for j = 0 to i-1
    s = s + a(j)
next j 
print "average of numbers ",s/i
end
