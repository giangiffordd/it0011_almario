A = set(["a", "b", "c", "d", "f", "g"])
B = set(("b", "c", "h", "l", "m", "o"))
C = {"c", "d", "f", "h", "j", "k", "i"}

union_AB = len(A | B)
diff_B_AC = len(B - (A | C))

print("a. Number of elements in the union of A and B:", union_AB)
print("\nb. Number of elements in B that are not in A or C:", diff_B_AC, "\n")

print("c. Set operations results:")
print("i. Elements in C but not in A:", C - A)
print("ii. Common elements in A and C:", A & C)
print("iii. Elements in B that are also in A or C:", B & (A | C))
print("iv. Elements in both A and C but not in B:", (A & C) - B)
print("v. Elements common to A, B, and C:", A & B & C)
print("vi. Elements in B that are not in A or C:", B - (A | C))
