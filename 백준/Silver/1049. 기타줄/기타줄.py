n, m = map(int, input().split())
x, y = n//6, n%6
set_p, piece_p = [], []
for _ in range(m):
    s, p = map(int, input().split())
    set_p.append(s)
    piece_p.append(p)
sp = sorted(set_p)[0]
piece = sorted(piece_p)[0]
print(min((sp * x + min(p*y, sp), piece * n)) if x > 0 else min(sp, piece*y))