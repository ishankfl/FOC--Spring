### Algorithm: BubbleSort using Two For Loops

```
Algorithm BubbleSort
Input: list of numbers

for i = 0 to list.count - 1 do
    for j = 0 to list.count - i - 2 do
        if list[j] > list[j + 1] then
            temp = list[j]
            list[j] = list[j + 1]
            list[j + 1] = temp
        end if
    end for
end for

Output: sorted list
End BubbleSort
```
