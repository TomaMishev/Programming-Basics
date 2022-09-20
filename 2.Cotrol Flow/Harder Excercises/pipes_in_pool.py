pool_volume = int(input())
first_pipe_flow = int(input())
second_pipe_flow = int(input())
worker_missing_hours = float(input())

first_pipe_fill = first_pipe_flow * worker_missing_hours
second_pipe_fill = second_pipe_flow * worker_missing_hours
total_fill = first_pipe_fill + second_pipe_fill

first_pipe_contributed = first_pipe_fill / total_fill * 100
second_pipe_contributed = second_pipe_fill / total_fill * 100
total_contributed = total_fill / pool_volume * 100
overflow = total_fill - pool_volume

if pool_volume >= total_fill:
    print(f"The pool is {total_contributed:.2f}% full. Pipe 1: {first_pipe_contributed:.2f}%. Pipe 2: {second_pipe_contributed:.2f}%.")
else:
    print(f"For {worker_missing_hours:.2f} hours the pool overflows with {overflow:.2f} liters.")
