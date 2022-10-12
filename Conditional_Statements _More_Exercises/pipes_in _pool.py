v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())
pipe1 = p1 * h
pipe2 = p2 * h
pipe_pool = pipe1 + pipe2

if pipe_pool <= v:
    pool_percent = (pipe_pool/v)*100
    p1_percent = (pipe1 / pipe_pool)*100
    p2_percent = (pipe2 / pipe_pool)*100
    print(f"The pool is {pool_percent:.2f}% full. Pipe 1: {p1_percent:.2f}%. Pipe 2: {p2_percent:.2f}%.")
elif pipe_pool > v:
    over_flow = pipe_pool - v
    print(f"For {h:.2f} hours the pool overflows with {over_flow:.2f} liters.")
