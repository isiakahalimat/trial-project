def budget_remaining(budget, food, transport):
    return budget - food - transport

def budget_message(name, remaining):
    return f"{name} has {remaining} naira remaining."


remaining = budget_remaining(2000, 900, 600)

message = budget_message("Ada", remaining)
print(message)

remaining = budget_remaining(1500, 0, 0)
message = budget_message("halimat", remaining)
print(message)

remaining = budget_remaining(1000, 800, 500)
message = budget_message("Tobi",remaining)
print(message)
