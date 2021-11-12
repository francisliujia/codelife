def print_models(unprinted_models, completed_models):
    while unprinted_models:
        current_design = unprinted_models.pop()
        print(f"Printing model: {current_design.title()}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been completed: ")
    for completed_model in completed_models:
        print(completed_model)